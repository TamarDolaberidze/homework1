class Rectangle:
    def __init__(self, width, length, color):
        self.width = width
        self.length = length
        self.color = color
    
    def perimeter(self):
        return 2 * (self.width + self.length)
    def area(self):
        return(self.width * self.length)

obj1 = Rectangle(5, 1, "blue")
obj2 = Rectangle(3, 3, "green")
obj3 = Rectangle(7, 3, "purple")    

print(obj1.area())