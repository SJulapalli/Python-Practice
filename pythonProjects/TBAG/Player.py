import Room

class Player:
    name = ""
    inventory = []
    location = ""
    wealth = 0
    held_item = ""

    def init(self, location, wealth, name):
        self.name = name
        self.location = location
        self.wealth = wealth

    def changeWealth(self, amount):
        wealth = self.wealth + amount
        return wealth

    def move(self, room):
        location = room

    def collect(self, item):
        self.inventory.append(item)

    def drop(self, index):
        self.inventory.remove(index)

    def atk(self):
        "yeet"

    