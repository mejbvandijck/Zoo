class Animals:
    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species

    def Specs(self):
        return f"Name: {self.name}, Age: {self.age}, Species: {self.species}"
    
    def MakeSound(self):
        return f"{self.name} {self.sound}s!"

if __name__ == "__main__":
    pass 