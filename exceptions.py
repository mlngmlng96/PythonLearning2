try:
    age = int(input('Age: '))
    print(age)
    income = 2000
    risk = income/age

except ValueError:
    print('Invalid Value')

except ZeroDivisionError:
    print('Age cannot be 0')

#exceptions prevent the code from stopping even if the wrong value/etc are added, provided all the exceptions are captured like the two above