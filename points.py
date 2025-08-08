#when naming classes, we use capital cases
class Point:
    def __init__(self,x,y): #constructor method
        self.x = x
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print("draw")


point1 = Point(10,20) #calling the function and put it in a label
print(point1.x)
point1.draw()

point2 = Point(1,2)
print(point2.x)

#Exercise

class Person:
    def __init__(self,name): # constructor method
        self.name = name

    def talk(self):
        print(f"Hi, I am {self.name}")

John = Person("John")
print(John.name)
John.talk()
bob = Person("Bob Smith")
bob.talk()