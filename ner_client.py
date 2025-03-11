
class NamedEntityCLient:

    def __init__(self, model):
        self.model = model


    def get_ents(self, sentence):
        doc = self.model(sentence)
        entities = [ { "ent": ent.text, "label": self.map_label(self, ent.label_)} for ent in doc.ents ]
        return { "ents": entities, "html": '' }


    @staticmethod
    def map_label(self, label):
        label_map = {
            'PERSON': 'Person'
        }

        return label_map.get(label)