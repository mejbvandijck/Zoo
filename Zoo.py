from lion import Lion
from elephant import Elephant
from monkey import Monkey


if __name__ == "__main__":
    Simba = Lion("Simba", 5, "Black", "Burger Zoo")
    Kitten = Lion("Kitten", 3, "Nearly Black", "Ouwehands Zoo")
    Dumbo = Elephant("Dumbo", 7, 1.80, "Beekse Bergen")
    George = Monkey("George", 2, "Braun", "Rotterdam Zoo")

    for x in [Simba, Kitten, Dumbo, George]:
        print(x.Specs(), x.MakeSound(), sep='\n') 
