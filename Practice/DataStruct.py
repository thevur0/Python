edward = ['Edward Gumby', 42]
print (edward)
john = ['John Smith', 50]
database = [edward, john]
print(database)

#索引
greeting = 'Hello'
print(greeting[0], greeting[-1])
#切片
months = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December'
]

print(months[3:5])  # ['April', 'May']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers[7:10])  # [8, 9, 10]
print(numbers[-3:-1])  # [8, 9]
print(numbers[-3:0])  # []
print(numbers[-3:])  # [8, 9, 10]
print(numbers[:3])  # [1, 2, 3]
print(numbers[:])  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers[0:10:1])  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers[0:10:2])  # [1, 3, 5, 7, 9]
print(numbers[::4])  # [1, 5, 9]
print(numbers[8:3:-1])  # [9, 8, 7, 6, 5]
print(numbers[::-2])  # [10, 8, 6, 4, 2]

print([1, 2, 3] + [4, 5, 6])  # [1, 2, 3, 4, 5, 6]
print([1, 2, 3] + ['World'])  # [1, 2, 3, 'World']

print([1, 2, 3]*3)  # [1, 2, 3, 1, 2, 3, 1, 2, 3]
print([None] * 10)  # [None, None, None, None, None, None, None, None, None, None]

print(1 in [1, 2, 3])# True
print([1, 2] in [1, 2, 3])  # False
print([1, 2] in [1, [1, 2], 3])  # True
numbers = [100, 34, 678]
print(len(numbers),max(numbers),min(numbers))

numbers.append(51)
numbers.remove(100)
numbers[0] = 10
del numbers[1]
numbers.extend([1,2,3])
numbers.pop()
print(numbers)

name = list('Hello')
name[len(name):] = ' World'
print(name)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers[0:4:1] = []
print(numbers, numbers.index(7))



