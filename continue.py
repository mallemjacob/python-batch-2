while True:
    print('Who are you?')
    name = input()
    if name != 'julia':
        continue
    print('Hello, Julia. What is the password? (It is a fish.)')
    password = input()
    if password == 'swordfish':
        break

print('Access Granted!')