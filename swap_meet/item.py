import uuid

class Item:
    def __init__(self, id=None, condition=0):
        if id is None:
            self.id = uuid.uuid4().int
        else:
            self.id = id

        self.condition = condition

    def __str__(self):
        return f"An object of type Item with id {self.id}."

    def get_category(self):
        return self.__class__.__name__
