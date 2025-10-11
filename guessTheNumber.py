import random
#import sys

#my version
print('I am thinking of a number between  1 and 20')
guessCounter = 0
randomNumber = random.randint(1, 20)
while True:
    print('Take a guess.')
    userNumber = int(input())
    if userNumber == randomNumber:
        guessCounter = guessCounter + 1
        print('Good job! you guessed my number in ' +
              str(guessCounter) + ' guesses.')
        sys.exit()
    elif userNumber > randomNumber:
        guessCounter = guessCounter + 1
        print('Your guess is too high')
    elif userNumber < randomNumber:
        guessCounter = guessCounter + 1
        print('Your guess is too low')

# secretNumber = random.randint(1, 20)
# print('I am thinking of a number between  1 and 20')

# for guessesTaken in range(1, 7):
#     print('Take a guess.')
#     guess = int(input())

#     if guess < secretNumber:
#         print('Your guess is too low')
#     elif guess > secretNumber:
#         print('Your guess is too high')
#     else:
#         break

# if guess == secretNumber:
#     print('Good job! you guessed my number in ' +
#           str(guessesTaken) + ' guesses.')
# else:
#     print('Nope. The number i was thinking  of was ' + str(secretNumber) + ' .')
