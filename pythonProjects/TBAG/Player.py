import Room

class Player:
    name = ""
    inventory = []
    location = Room.Room()
    wealth = 0
    held_item = ""
    health = 100

    def init(self, location, wealth, name):
        self.name = name
        self.location = location
        self.wealth = wealth

    def changeWealth(self, amount):
        wealth = self.wealth + amount
        return wealth

    def move(self, direction):
        ""

    def collect(self, item):
        self.inventory.append(item)

    def drop(self, index):
        self.inventory.remove(index)

    def atk(self):
        "yeet"

