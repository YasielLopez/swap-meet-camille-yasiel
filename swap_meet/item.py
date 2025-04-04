import uuid

class Item:
    def __init__(self, id=None, condition=0):
        # stores the items condition on a 0 to 5 scale
        self.condition = condition
        if id is None:
            # this generates a unique integer id using uuid unless it already has one
            self.id = uuid.uuid4().int
        else:
            self.id = id
    
    def get_category(self):
        return "Item"
    
    def __str__(self):
        return f"An object of type {self.__class__.__name__} with id {self.id}."
    
    def condition_description(self):
        descriptions = [
            "Poor condition",  # 0
            "Used condition",  # 1
            "Fair condition",  # 2
            "Good condition",  # 3
            "Excellent condition",  # 4
            "Mint condition"   # 5
        ]
        return descriptions[min(self.condition, 5)]
