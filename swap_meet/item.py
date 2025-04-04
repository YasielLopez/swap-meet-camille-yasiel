import uuid

class Item:
    def __init__(self, id=None, condition=0):
        self.condition = condition
        if id is None:
            self.id = uuid.uuid4().int
        else:
            self.id = id
    
    def get_category(self):
        return "Item"
    
    def __str__(self):
        return f"An object of type {self.__class__.__name__} with id {self.id}."
    
    def condition_description(self):
        descriptions = [
            "Poor condition", 
            "Used condition", 
            "Fair condition", 
            "Good condition", 
            "Excellent condition", 
            "Mint condition"
        ]
        return descriptions[min(self.condition, 5)]
