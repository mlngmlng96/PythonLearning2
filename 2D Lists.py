matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(matrix[0][1])

for row in matrix:
    for item in row:
        print(item)

numbers = [5,2,1,7,4]
numbers.append(20)
print(numbers)

numbers.insert(2,10)
print(numbers)

numbers.remove(5)
print(numbers)

numbers.pop()
print(numbers)

print(numbers.index(2))

print(50 in numbers)

print(numbers.count(2))

numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)

numbers2 = numbers.copy()
print(numbers2)

"""
Task: remove duplicates from the list
"""

List =[1,2,3,4,5,1,10,1,3,4,6,2,1,5]
Updated_list = []
for number in List:
    if number not in Updated_list:
        Updated_list.append(number)

print(Updated_list)




