#if statements

print('Enter your name:')
name = input() #bill

if name == 'hello':
    print('this is hello')
    print('welcome')
elif name == 'bye':
    print('this is hello')
else:
    print('False')
    age = int(input()) # '18' ---> 18
    if age == 18:
        print('you are an adult')
        print('you can vote')


if 2 > 1:
    if 2 == 3:
        print('nested if')
    else:
        print('inner false')
else:
    print('false')

name = 'Carol'
age = 3000
if age == 4000: #3000 == 4000
    print('Hi, Alice.')
elif age == 5000: # 3000 == 5000
    print('vampire')
else:
    print('hi grannie')

#This program says hello and asks for my name.
print('Hello, world!')
print('What is your name?')
#ask for their name
myName = input() #helloworld --> 10
if myName == 'valkyrie':
    print('It is good to meet you, ' + myName)
    print('The length of your name is:')
    print(len(myName))
    if len(myName) > 5:
        print('What is your age?')
        myAge = input() #'19' ---> 19
        print('You will be ' + str(int(myAge) + 1) + ' in a year.')
    else:
        print('The length of name must be greater than 5 characters.')