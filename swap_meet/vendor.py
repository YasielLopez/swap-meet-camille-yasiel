class Vendor:
    def __init__(self, inventory=None):
        self.inventory = inventory if inventory is not None else []

    # add items to people's inventory
    def add(self, item):
        self.inventory.append(item)
        return item

    # remove items from inventory
    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        return False

    # return the matching item. if the item doesn't exist return none.
    def get_by_id(self, item_id):
        for item in self.inventory:
            if item.id == item_id:
                return item
        return None

    # this swaps the items
    def swap_items(self, other_vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False
        
        other_vendor.add(self.remove(my_item))

        self.add(other_vendor.remove(their_item))

        return True

    # swaps the first item in inventory
    def swap_first_item(self, other_vendor):
        if not self.inventory or not other_vendor.inventory:
            return False
        
        return self.swap_items(other_vendor, self.inventory[0], other_vendor.inventory[0])

    # shows the items in the category 
    def get_by_category(self, category):
        return [item for item in self.inventory if item.get_category() == category]

    def get_best_by_category(self, category):
        matching_items = self.get_by_category(category)
        if not matching_items:
            return None
        
        return max(matching_items, key=lambda item: item.condition)

    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        if not my_best or not their_best:
            return False
        
        return self.swap_items(other_vendor, me_best, their_best)