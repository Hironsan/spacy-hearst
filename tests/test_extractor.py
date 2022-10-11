import spacy

from hearst.extractor import NPSuchAsNPExtractor, SuchNPAsNPExtractor


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
