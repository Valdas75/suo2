class Dog():

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
            print(self.name.title() + " PRISEDA")

    def jump(self):
            print(self.name.title() + " PASOKA")

    def gav(self):
        print("AU-AU")

    def urzgia(self):
        print("RRRRRRRRR")

my_dog = Dog('Reksas', 7)
my_dog_2 = Dog('Tobikas', 4)

print(my_dog.name)
print(my_dog.age)
print(my_dog_2.name)
print(my_dog_2.age)

my_dog.jump()
my_dog_2.sit()
my_dog.sit()
my_dog_2.jump()
lese = Dog('lese', 3)
bobikas = Dog('bobikas', 5)

lese.gav()
bobikas.urzgia()
