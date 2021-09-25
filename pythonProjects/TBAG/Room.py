class Room:
    description = ""
    enemies = []
    items = []
    objects = []
    people = []
    dimensions = ""
    left_room = ""
    right_room = ""
    front_room = ""
    previous_room = ""

    def cNicksRoom(self):
        self.objects.append("Cosby poster")
        self.objects.append("Cosby Daikimura")

    def cVedasRoom(self):
        self.objects.append("big massive bed")
        self.objects.append("The WHOLE gaming setup")
        self.objects.append("A whole shelf")
        self.objects.append("A whole shelf of manga")
        self.people.append("Veda")
        self.description = "The rooom's a fuckin circle bruh. And all the walls are constantly changing color."
