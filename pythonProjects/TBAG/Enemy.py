import Room

class Enemy:
    name = ""
    inventory = []
    location = Room.Room()
    wealth = 0
    held_item = ""
    health = 100

    def atk(self):
        "yeet"