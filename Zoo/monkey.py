from animals import Animals


class Monkey(Animals):

    MonkeyNames = []

    def __init__(self, name, age, skin_color, status, species="Monkey" ):
        Animals.__init__(self, name, age, species)
        self.sound = "Chat"
        self.skin_color = skin_color
        self.status = status
        Monkey.MonkeyNames.append(self.name)


if __name__ == "__main__":
    pass 