import spacy

from hearst.extractor import (
    NPEspeciallyNPOrAndNPExtractor,
    NPIncludingNPOrAndNPExtractor,
    NPOrAndOtherNPExtractor,
    NPSuchAsNPExtractor,
    SuchNPAsNPExtractor,
)


class TestExtractor:
    @classmethod
    def setup_class(cls):
        cls.nlp = spacy.load("en_core_web_sm")

    def test_np_such_as_np(self):
        text = "Forty-four percent of patients with uveitis had one or more identifiable signs or symptoms, such as red eye, ocular pain, visual acuity, or photophobia, in order of decreasing frequency."
        extractor = NPSuchAsNPExtractor(self.nlp)
        hyponyms = extractor.extract(text)
        expected = [
            ("red eye", "symptoms"),
            ("ocular pain", "symptoms"),
            ("visual acuity", "symptoms"),
            ("photophobia", "symptoms"),
        ]
        assert hyponyms == expected

    def test_such_np_as_np(self):
        text = "There are works by such authors as Herrick, Goldsmith, and Shakespeare."
        extractor = SuchNPAsNPExtractor(self.nlp)
        hyponyms = extractor.extract(text)
        expected = [("Herrick", "authors"), ("Goldsmith", "authors"), ("Shakespeare", "authors")]
        assert hyponyms == expected

    def test_np_or_other_np(self):
        text = "There were bruises, lacerations, or other injuries were not prevalent."
        extractor = NPOrAndOtherNPExtractor(self.nlp)
        hyponyms = extractor.extract(text)
        expected = [("bruises", "injuries"), ("lacerations", "injuries")]
        assert hyponyms == expected

    def test_np_and_other_np(self):
        text = "temples, treasures, and other artifacts were looted."
        extractor = NPOrAndOtherNPExtractor(self.nlp)
        hyponyms = extractor.extract(text)
        expected = [("temples", "artifacts"), ("treasures", "artifacts")]
        assert hyponyms == expected

    def test_np_including_np_or_and_np(self):
        text = "common law countries, including Canada, Australia, and England enjoy toast."
        extractor = NPIncludingNPOrAndNPExtractor(self.nlp)
        hyponyms = extractor.extract(text)
        expected = [
            ("Canada", "common law countries"),
            ("Australia", "common law countries"),
            ("England", "common law countries"),
        ]
        assert hyponyms == expected

    def test_np_especially_np_or_and_np(self):
        text = "Many countries, especially France, England and Spain also enjoy toast."
        extractor = NPEspeciallyNPOrAndNPExtractor(self.nlp)
        hyponyms = extractor.extract(text)
        expected = [("France", "Many countries"), ("England", "Many countries"), ("Spain", "Many countries")]
        assert hyponyms == expected
