import spacy

from hearst.extractor import NPSuchAsNPExtractor


class TestNPSuchAsNP:
    @classmethod
    def setup_class(cls):
        cls.nlp = spacy.load("en_core_web_sm")
        cls.extractor = NPSuchAsNPExtractor(cls.nlp)

    def test_patterns(self):
        text = "Forty-four percent of patients with uveitis had one or more identifiable signs or symptoms, such as red eye, ocular pain, visual acuity, or photophobia, in order of decreasing frequency."
        hyponyms = self.extractor.extract(text)
        expected = [
            ("red eye", "symptoms"),
            ("ocular pain", "symptoms"),
            ("visual acuity", "symptoms"),
            ("photophobia", "symptoms"),
        ]
        assert hyponyms == expected
