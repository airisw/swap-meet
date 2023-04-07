import uuid

class Item:
    
    def __init__(self, id=None, condition=0, age=0):
        self.id = uuid.uuid4().int if id is None else id
        self.condition = condition
        self.age = age

    def get_category(self):
        return "Item"
    
    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}."
    
    def condition_description(self):
        DESCRIPTIONS = ["as-is", "scratched", "used", "slightly used", "like new", "brand new"]
        return DESCRIPTIONS[self.condition]