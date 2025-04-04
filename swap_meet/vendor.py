class Vendor:
    def __init__(self, inventory=None):
        self.inventory = inventory if inventory is not None else []
    
    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        return False
    
    def get_by_id(self, id):
        for item in self.inventory:
            if item.id == id:
                return item
        return None
    
    def swap_items(self, other_vendor, my_item, their_item):
        if my_item in self.inventory and their_item in other_vendor.inventory:
            self.remove(my_item)
            other_vendor.remove(their_item)
            other_vendor.add(my_item)
            self.add(their_item)
            return True
        return False
    
    def swap_first_item(self, other_vendor):
        if not self.inventory or not other_vendor.inventory:
            return False
        
        my_first_item = self.inventory[0]
        their_first_item = other_vendor.inventory[0]
        
        return self.swap_items(other_vendor, my_first_item, their_first_item)
    
    def get_by_category(self, category):
        return [item for item in self.inventory if item.get_category() == category]
    
    def get_best_by_category(self, category):

        category_items = self.get_by_category(category)
        if not category_items:
            return None
        
        return max(category_items, key=lambda item: item.condition)
    
    def swap_best_by_category(self, other_vendor, my_priority, their_priority):

        my_best_item = self.get_best_by_category(their_priority)
        their_best_item = other_vendor.get_best_by_category(my_priority)
        
        if not my_best_item or not their_best_item:
            return False
        
        return self.swap_items(other_vendor, my_best_item, their_best_item)