names = ["John", "Bob","Mosh","Sarah","Maya"]
print(names[1])
print(names[-1])
print(names[2:])
print(names[:])

numbers = [100,20,3,14,25]
max = numbers[0]
for number in numbers:
    if max < number:
        max = number

print(max)
