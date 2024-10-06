class Dog:
    def __init__(self, breed = "Husky", size = "Medium", age = "4 years", color = "Light Brown"):
        self.breed = breed
        self.size = size
        self.age = age
        self.color = color
    
    def Eat(self):
        return f"The {self.breed} is eating."
    def Sleep(self):
        return f"The {self.breed} is sleeping."
    def Sit(self):
        return f"The {self.breed} is sitting."
    def Run(self):
        return f"The {self.breed} is running."

obj1 = Dog("Neapolitan Mastiff", "Large", "5 years", "Black")
obj2 = Dog("Maltese", "Small", "2 years", "White")
obj3 = Dog("Chow Chow", "Medium", "3 years", "Brown")
obj_default = Dog()

print(obj1.Eat())
print(obj1.Sleep())
print(obj1.Sit())
print(obj1.Run())

print(obj2.Eat())
print(obj2.Sleep())
print(obj2.Sit())
print(obj2.Run())

print(obj3.Eat())
print(obj3.Sleep())
print(obj3.Sit())
print(obj3.Run())

print(obj_default.Eat())
print(obj_default.Sleep())
print(obj_default.Sit())
print(obj_default.Run())