from animals import Animals


class Elephant(Animals):

    ElephantNames = []

    def __init__(self, name, age, trunc_length, status, species="Elephant" ):
        Animals.__init__(self, name, age, species)
        self.sound = "Trumpet"
        self.trunc_length = trunc_length
        self.status = status
        Elephant.ElephantNames.append(self.name)


if __name__ == "__main__":
    pass 