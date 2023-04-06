class Vendor:
    
    def __init__(self, inventory=None):
        self.inventory = [] if inventory is None else inventory

    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False
        
    def get_by_id(self, id):
        for item in self.inventory:
            if item.id == id:
                return item
        return None
    
    def swap_items(self, other_vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in other_vendor.inventory :
            return False
        else:
            self.inventory.remove(my_item)
            other_vendor.inventory.append(my_item)
            other_vendor.inventory.remove(their_item)
            self.inventory.append(their_item)

            return True
        
    def swap_first_item(self, other_vendor):
        if not self.inventory or not other_vendor.inventory:
            return False
        else:
            other_vendor.inventory.append(self.inventory[0])
            self.inventory.remove(self.inventory[0])
            self.inventory.append(other_vendor.inventory[0])
            other_vendor.remove(other_vendor.inventory[0])

            return True
        
    def get_by_category(self, category):
        result = []
        for item in self.inventory:
            if item.get_category() == category:
                result.append(item)
        return result
    
    def get_best_by_category(self, category):
        filtered_items = {}

        for item in self.inventory:
            if item.get_category() == category:
                if item.condition in filtered_items:
                    continue
                filtered_items[item.condition] = item
        
        for item in filtered_items:
            return filtered_items[max(filtered_items)]
        

    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        my_best_item = self.get_best_by_category(their_priority)
        their_best_item = other_vendor.get_best_by_category(my_priority)

        if not my_best_item or not their_best_item:
            return False
        else:
            self.swap_items(other_vendor, my_best_item, their_best_item)
            return True
        
    def get_newest_by_category(self, category):
        filtered_items = {}

        for item in self.inventory:
            if item.get_category() == category:
                if item.age in filtered_items:
                    continue
                filtered_items[item.age] = item

        for item in filtered_items:
            return filtered_items[min(filtered_items)]
        
    def swap_by_newest(self, other_vendor, my_priority, their_priority):
        my_newest_item = self.get_newest_by_category(their_priority)
        their_newest_item = other_vendor.get_newest_by_category(my_priority)

        if not my_newest_item or not their_newest_item:
            return False
        else:
            self.swap_items(other_vendor, my_newest_item, their_newest_item)
            return True