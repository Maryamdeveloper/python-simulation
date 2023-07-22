print('hello')
type(2)
age = input('your age: ')
type(age)
int(age)
float(age)
# a,b=6,7 #declare variables in one line
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
# input()


def salam(name):
    print('salam', name)


salam('maryam')


def sum(a, b):
    return a+b


sum(2, 5)
print(sum(2, 5))


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

N=3
while N>=0:
    print(N)
    N=N+1
    if N==10:
        break
