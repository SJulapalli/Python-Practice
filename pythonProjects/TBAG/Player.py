import Room
import Objects

class Player:
    name = ""
    inventory = []
    location = ""
    wealth = 0
    held_item = ""
    health = 100
    FistAtkMult = 1;
    RangeAtkMult = 1;

    def init(self, location, wealth, name):
        self.name = name
        self.location = location
        self.wealth = wealth

    def changeWealth(self, amount):
        wealth = self.wealth + amount
        return wealth

    def move(self, direction):
        ""

    def showInventory(self):
        for x in self.inventory:
            print(self.inventory.index())

    def collect(self, item):
        if isinstance(item, Objects.SmallObject):
            self.location.objects.remove(item)
            self.inventory.append(item)
        elif isinstance(item, Objects.MediumObject):
            self.location.objects.remove(item)
            if self.held_item != "":
                held_item = item
                print("You pick up the " + item.name)
            else:
                print("You pick up the " + item.name + ", putting the "
                      + self.held_item.name + " away")
                held_item = item
        else:
            print("You cannot pickup this object")

    def drop(self, item):
        print("You drop " + item.name)
        self.location.objects.append(item)
        self.inventory.remove(self.inventory.index(item))

    def atk(self):
        ''

