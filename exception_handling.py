# def spam(divideBy):
#     try:
#         return 42 / divideBy
#     except ZeroDivisionError:
#         return spam(14)

# print(spam(2))
# print(spam(12))
# print(spam(0))
# print(spam(1))

import sys

def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    else:
        print(3 * number + 1)
        return 3 * number + 1

while True:
    try:
        user_input = int(input()) #10
        while True:
            user_input = collatz(user_input) #5
            if user_input == 1:
                break
        break
    except ValueError:
        print('Must be interger:')
    except KeyboardInterrupt:
        print('Program exited!')
        sys.exit()