class Car:
    def __init__(self, color, brand, model):
        self.color = color
        self.brand = brand
        self.model = model
    
    def __str__(self):
        return f"Color is {self.color}, brand is {self.brand}, model is {self.model}."
    
    def change_color(self, new_color):
        self.color = new_color
        return f"Car color has been updated to {self.color}."

obj1 = Car("red", "Ford", "Mustang")
obj2 = Car("blue", "Toyota", "Prius")
obj3 = Car("green", "Volkswagen", "Golf") 

print(obj1.__str__())
print(obj1.change_color("black"))

print(obj2.__str__())
print(obj2.change_color("grey"))

print(obj3.__str__())
print(obj3.change_color("gold"))