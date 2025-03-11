import unittest
from ner_client import NamedEntityCLient
from test_doubles import NerModelTestDouble


class TestEntityRecClient(unittest.TestCase):

    def test_get_ents_returns_dictionary_given_empty_string_causes_empty_spacy_doc_ents(self):
        model = NerModelTestDouble('eng')
        model.returns_doc_ents([])
        ner = NamedEntityCLient(model)
        ents = ner.get_ents("")
        self.assertIsInstance(ents, dict)


    def test_get_ents_returns_dictionary_given_nonempty_string_causes_empty_spacy_doc_ents(self):
        model = NerModelTestDouble('eng')
        model.returns_doc_ents([])
        ner = NamedEntityCLient(model)
        ents = ner.get_ents("Hanna is a girl")
        self.assertIsInstance(ents, dict)

    
    def test_get_ents_given_spacy_PERSON_is_resturned_serialized_to_Person(self):
        model = NerModelTestDouble('eng')
        doc_ents = [{'text': 'Eugene', 'label_': 'PERSON'}]
        model.returns_doc_ents(doc_ents)
        ner = NamedEntityCLient(model)
        ents = ner.get_ents('...')
        expected_resutl = { "ents": [{'ent': 'Eugene', 'label': 'Person'}] , "html": ''}
        self.assertListEqual(ents["ents"], expected_resutl["ents"])