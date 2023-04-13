class Circle():
  def __init__(self,radius,pi=3.14159):
    self.radius = radius
    self.pi = pi
  def Area(self):
    return self.radius**2*self.pi
  def Perimeter(self):
    return 2*self.radius*self.pi

radius = int(input("input radius:"))
circle = Circle(radius)
print(f"The area of the circle is {circle.Area()}")
print(f"the Perimeter of a circle is {circle.Perimeter()}")