import uuid

class Item:
    def __init__(self, id=None, condition=0):
        self.id = id if id is not None else uuid.uuid4().int
        self.condition = condition

    def __str__(self):
        return f"An object of type Item with id {self.id}."

    def get_category(self):
        return "Item"
    
    def condition_description(self):
        if self.condition == 0:
            return "poor"
        elif self.condition == 1:
            return "fair"
        elif self.condition == 2:
            return "acceptable"
        elif self.condition == 3:
            return "good"
        elif self.condition == 4:
            return "like new"
        else:
            return "brand new"
