class Dog:
    def __init__(self,name,color,species):
        self.name = name
        self.color = color
        self.species = species

    def __str__(self):
        return f"{self.name},{self.color},{self.species}"

    def bark(self, something):
        print('bow! bow!',something)

if __name__ == '__main__':

    Dog_1 = Dog('kiri','black','yolk')
    Dog_1.bark('shit')

    print(str(Dog_1))