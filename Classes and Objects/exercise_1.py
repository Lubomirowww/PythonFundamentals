class Storage:

    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []


    def add_product(self, product: str):
        if self.capacity > len(self.storage):
            self.storage.append(product)


    def get_product(self):
        return self.storage


storage = Storage(5)
storage.add_product("Apple")
storage.add_product("banana")
storage.add_product("potato")
storage.add_product("bread")
storage.add_product("tomato")
print(storage.get_product())