from typing import List, Tuple

from spacy.matcher import Matcher

from .builder import (
    build_np_especially_np_or_and_np_patterns,
    build_np_including_np_or_and_np_patterns,
    build_np_or_and_other_np_patterns,
    build_np_such_as_np_patterns,
    build_such_np_as_np_patterns,
)


class NPSuchAsNPExtractor:
    def __init__(self, nlp, n=5):
        self.nlp = nlp
        patterns = build_np_such_as_np_patterns(n)
        self.matcher = Matcher(nlp.vocab)
        self.matcher.add("NP such as NP", patterns)

    def extract(self, text) -> List[Tuple[str, str]]:
        doc = self.nlp(text)
        with doc.retokenize() as retokenizer:
            for span in doc.noun_chunks:
                retokenizer.merge(span)
        matches = self.matcher(doc, as_spans=True)
        if not matches:
            return []
        noun_chunks = list(max((span for span in matches), key=len).noun_chunks)
        return [(chunk.text, noun_chunks[0].text) for chunk in noun_chunks[1:]]


class SuchNPAsNPExtractor:
    def __init__(self, nlp, n=5):
        self.nlp = nlp
        patterns = build_such_np_as_np_patterns(n)
        self.matcher = Matcher(nlp.vocab)
        self.matcher.add("such NP as NP", patterns)

    def extract(self, text) -> List[Tuple[str, str]]:
        doc = self.nlp(text)
        # merge tokens into noun chunks
        with doc.retokenize() as retokenizer:
            for span in doc.noun_chunks:
                if span[0].lower_ == "such":
                    continue
                retokenizer.merge(span)
        matches = self.matcher(doc, as_spans=True)
        if not matches:
            return []
        match = max((span for span in matches), key=len)
        hypernym = match[1].text
        noun_chunks = list(match[3:].noun_chunks)  # skip "such NP as"
        return [(chunk.text, hypernym) for chunk in noun_chunks]


class NPOrAndOtherNPExtractor:
    def __init__(self, nlp):
        self.nlp = nlp
        patterns = build_np_or_and_other_np_patterns()
        self.matcher = Matcher(nlp.vocab)
        self.matcher.add("NP or other NP", patterns)

    def extract(self, text) -> List[Tuple[str, str]]:
        doc = self.nlp(text)
        with doc.retokenize() as retokenizer:
            for span in doc.noun_chunks:
                if span[0].lower_ == "other":
                    continue
                retokenizer.merge(span)
        matches = self.matcher(doc, as_spans=True)
        if not matches:
            return []
        match = max((span for span in matches), key=len)
        hypernym = match[-1].text
        noun_chunks = list(match[:-1].noun_chunks)  # skip "other NP"
        return [(chunk.text, hypernym) for chunk in noun_chunks]


class NPIncludingNPOrAndNPExtractor:
    def __init__(self, nlp):
        self.nlp = nlp
        patterns = build_np_including_np_or_and_np_patterns()
        self.matcher = Matcher(nlp.vocab)
        self.matcher.add("NP including NP or/and NP", patterns)

    def extract(self, text) -> List[Tuple[str, str]]:
        doc = self.nlp(text)
        with doc.retokenize() as retokenizer:
            for span in doc.noun_chunks:
                retokenizer.merge(span)
        matches = self.matcher(doc, as_spans=True)
        if not matches:
            return []
        match = max((span for span in matches), key=len)
        hypernym = match[0].text
        noun_chunks = list(match[1:].noun_chunks)  # skip first NP
        return [(chunk.text, hypernym) for chunk in noun_chunks]


class NPEspeciallyNPOrAndNPExtractor:
    def __init__(self, nlp):
        self.nlp = nlp
        patterns = build_np_especially_np_or_and_np_patterns()
        self.matcher = Matcher(nlp.vocab)
        self.matcher.add("NP especially NP or/and NP", patterns)

    def extract(self, text) -> List[Tuple[str, str]]:
        doc = self.nlp(text)
        with doc.retokenize() as retokenizer:
            for span in doc.noun_chunks:
                if span[0].lower_ == "especially":
                    continue
                retokenizer.merge(span)
        matches = self.matcher(doc, as_spans=True)
        if not matches:
            return []
        match = max((span for span in matches), key=len)
        hypernym = match[0].text
        noun_chunks = [
            span[1:] if span[0].lower_.startswith("especially") else span for span in match[1:].noun_chunks
        ]  # skip especially
        return [(chunk.text, hypernym) for chunk in noun_chunks]
