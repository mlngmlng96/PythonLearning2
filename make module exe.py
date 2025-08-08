class dice():

    def roll(self):
        import random


        from random import randint

        a = 1
        b = 6
        output1 = randint(a,b)
        output2 = randint(a,b)
        return (output1,output2)


dice1 = dice()
print(dice1.roll())

