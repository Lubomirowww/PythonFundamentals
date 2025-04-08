


class Inventory:

    __capacity = 3

    def __init__(self,capacity):

        self.capacity = capacity
        self.items = []


    def add_items(self, item:str):
        if self.capacity > len(self.items):
            self.items.append(item)

        else:
            return "not enough room in inventory"


    def get_capacity(self):
        return self.capacity


    def __repr__(self):
        current_capacity = len(self.items) - self.__capacity
        return f"items: {'. '.join(self.items)}.\nCapacity left: {current_capacity}"













inventory = Inventory (3)
inventory.add_items("Potion")
inventory.add_items("Sword")
print(inventory.add_items("Bottle"))
print(inventory.get_capacity())
print(inventory)