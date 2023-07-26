print('hello')
type(2)
age = input('your age: ')
type(age)
int(age)
float(age)
a,b=6,7 #declare variables in one line
A = 6
B = 7
print(A)
print(B)
print(A == B)  # equal
print(A != B)  # notEqual
print(not A != B)  # reversed
print((3 > 4) and (4 > 1))
print((3 > 4) or (4 > 1))

if A > 10:
    print('it\'s big')
elif A % 2 == 0:
    print('it\'s even')
else:
    print('it\'s small')
input()


def salam(name):
    print('salam', name)


salam('maryam')


def sumTwo(a, b):
    return a+b


sumTwo(2, 5)
print(sumTwo(2, 5))


def salary(hour, per_hour):
    if hour > 8:
        return 'too much work!'
    return hour*per_hour


print(salary(7, 2))
print(salary(16, 2))

name = input('your name? ')
while name != 'end':
    print('hi', name)
    name = input('your name? ')

N = 3
while N >= 0:
    print(N)
    N = N+1
    if N == 10:
        break


# first hw
numbers = []
while True:
    value = int(input("Enter a number (-1 to stop): "))
    if value == -1:
        break
    numbers.append(value)

if len(numbers) > 0:
    average = sum(numbers) / len(numbers)
    print("Average:", average)
else:
    print("No numbers were entered.")