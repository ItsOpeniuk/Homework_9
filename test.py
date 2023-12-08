class Animal:
    color = "white"

    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight

    def change_color(self):
        Animal.color = 'red'

dog = Animal('jack', 33)
cat = Animal('Vasya', 6)
print(dog.color)
cat.change_color()
print(cat.color)