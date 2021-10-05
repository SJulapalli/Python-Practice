import Enemy
import NPC
import Objects


class Room:
    name = ""
    description = ""
    enemies = []
    objects = []
    people = []
    dimensions = ""
    left_room = ""
    right_room = ""
    front_room = ""
    previous_room = ""

    def listObjects(self):
        print("The room contains:")
        count = 1
        for x in self.objects:
            print(str(count) + ". " + x.name)
            count = count + 1

    def cNicksRoom(self):
        temp = Objects.SmallObject()
        temp.cosbyPoster()
        self.objects.append(temp)
        temp = Objects.SmallObject()
        temp.cosbyDaikamakura()
        self.objects.append(temp)

    def cVedasRoom(self):
        temp = Objects.MassiveObject()
        temp.bigMassiveBed()
        self.objects.append(temp)
        temp = Objects.MassiveObject()
        temp.theWHOLEGamingSetup()
        self.objects.append(temp)
        temp = Objects.MassiveObject()
        temp.shelf()
        self.objects.append(temp)
        temp = Objects.MassiveObject()
        temp.mangaShelf()
        self.objects.append(temp)
        self.people.append("Veda")