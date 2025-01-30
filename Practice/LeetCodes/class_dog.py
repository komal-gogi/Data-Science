class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says woof")

    def get_older(self):
        self.age += 1

dog1 = Dog("Rio", 12)
print(dog1.name, dog1.age)
dog1.bark()
dog1.get_older()
print(dog1.age)