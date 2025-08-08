def greet_user(name):
    print(f"Hi {name}")
    print("Welcome aboard!")


def calc_cost(materials,shipping,discount):
    cost = (materials+shipping)*discount
    print(f"{cost}$")


print("Whasssssup")
greet_user("Ming")
print("Have the time of your life")

"""
you can add key arguments to help ppl to understand your code better"""
calc_cost(materials=50,shipping=20,discount=0.1)