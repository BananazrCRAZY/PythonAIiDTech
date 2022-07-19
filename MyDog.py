from Pet import Pet
class MyDog(Pet):
    def __init__(self, name, volume):
        self.name = name
        self.volume = volume

    def bark(self):
        if self.volume > 3:
            print("woof")
        else:
            print("yip")
