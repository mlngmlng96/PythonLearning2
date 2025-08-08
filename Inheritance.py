class Mammal:
    def walk(self):
        print("walk")

class Dog(Mammal):
    pass #means nothing so it doesnt have empty class that pyhton doesnt like


class Cat(Mammal):
    def meow(self):
        print("meow")


dog1 = Dog()
dog1.walk()

cat1 = Cat()
cat1.meow()