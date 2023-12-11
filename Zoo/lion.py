from animals import Animals


class Lion(Animals):

    LionNames = []

    def __init__(self, name, age, mane_color, status, species="Lion" ):
        Animals.__init__(self, name, age, species)
        self.sound = "Roar"
        self.mane_color = mane_color
        self.status = status
        Lion.LionNames.append(self.name)


if __name__ == "__main__":
    pass 