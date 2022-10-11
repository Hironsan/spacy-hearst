from typing import List, Tuple

from spacy.matcher import Matcher

from .builder import build_np_such_as_np_patterns


class NPSuchAsNPExtractor:
    def __init__(self, nlp, n=5):
        self.nlp = nlp
        self.nlp.add_pipe("merge_noun_chunks")
        patterns = build_np_such_as_np_patterns(n)
        self.matcher = Matcher(nlp.vocab)
        self.matcher.add("NP such as NP", patterns)

    def extract(self, text) -> List[Tuple[str, str]]:
        doc = self.nlp(text)
        matches = self.matcher(doc, as_spans=True)
        if not matches:
            return []
        noun_chunks = list(max((span for span in matches), key=len).noun_chunks)
        return [(chunk.text, noun_chunks[0].text) for chunk in noun_chunks[1:]]
