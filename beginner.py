import random
print('hello')
type(2)
age = input('your age: ')
type(age)
int(age)
float(age)
a, b = 6, 7  # declare variables in one line
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


def salam(namef):
    print('salam', namef)


salam('maryam')


def sumTwo(asf, bsf):
    return asf+bsf


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

# game
randNumber = random.randint(1, 99)
guessedNumber = input('guess a number: ')
while int(guessedNumber) != randNumber:
    if int(guessedNumber) > randNumber:
        print('mine is smaller')
    else:
        print('mine is larger')
    guessedNumber = input('guess a number: ')
print('you guessed right')

# second hw
a = 1
b = 99
computerGuessed = random.randint(a, b)
print(computerGuessed)
userRandNumber = input(
    'choose the state b for bigger, s for smaller, c for correct: ')
while userRandNumber != 'c':
    if userRandNumber == 'b':
        b = computerGuessed
    elif userRandNumber == 's':
        a = computerGuessed
    else:
        print('the input value is not valid')
        userRandNumber = input(
            'choose the state b for bigger, s for smaller, c for correct: ')
    computerGuessed = random.randint(a, b)
    print(computerGuessed)
    userRandNumber = input(
        'choose the state b for bigger, s for smaller, c for correct: ')
print('i finally guessed right')

hi='salam'
print(hi)
print(hi[0])
print(hi[4])
print(len(hi)) #length of string
for i in range(0,len(hi)): #moving on string array method 1
    print(i,hi[i])
count_a=0
for letter in 'salam maryam': #moving on string array method 2
    print(letter)
    if letter=='a':
        count_a=count_a+1

print(count_a)

s='man daram miram'
print(s[:3]) #from start till s[2](s[3] not included)
print(s[3:]) #from s[3] till end
print(s[3:8]) #from s[3] till s[8]
print(s[-1]) #the last item
# s[0]='M' #want to change but wrong!!(py is not immutable) correct way👇
s='M'+s[1:]

# search a character
print('a' in 'maria')
print('am' in 'maria')
print('b'>'B')
print('mary'.upper())
# list of available methods on specific type
print(dir('mary'))
print(help(str.count))
print('mary'.count('y'))
print('mary'.find('y'))
print('maryam'.find('a',2)) #find a that are after 2nd position
print('mary'.lower()) 
print(' mary    '.strip()) #removes space and tabs from right&left
print('mary'.startswith('b'))
print('Mary'.startswith('M'))
print('Mary'.lower().startswith('M'))
REST_OF_NAME='am'
print('Mary{%s} how are you? do you know you\'re %s years old!'%(REST_OF_NAME,age))