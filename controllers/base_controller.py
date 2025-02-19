class BaseController:
    def __init__(self, model):
        self.model = model

    def add(self, *args):
        self.model.add(*args)

    def view_all(self):
        return self.model.get_all()

    def delete(self, item_id):
        self.model.delete(item_id)