from app.model.petrinet_model import PetriNetModel


class PetriNetModelRepository:
    def __init__(self):
        super().__init__()
        self._models = []
        self.selected_model = None

    def add_model(self, model: PetriNetModel):
        self._models.append(model)

    def get_all_models(self):
        return self._models

    def set_selected_model(self, model: PetriNetModel):
        self.selected_model = model