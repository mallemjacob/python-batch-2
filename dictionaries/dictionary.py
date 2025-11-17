# list = ['cat','bat','rat']
# #        0       1     2

# print(list[1])

# print('cat' in list)

# # dictionary
# spam = {'name':'mouse','age':23, 12345:'password'}

# print(spam['name'])
# print(spam['age'])
# print(spam[12345])

# # methods

# #keys()
# print(spam.keys())

# for i in spam.keys():
#     print(i)

# print('name' in spam.keys())

# #values()
# print(spam.values())

# for i in spam.values():
#     print(i)

# print('password' in spam.values())

# #items()
# print(spam.items())

# spam['age'] = 10

# print(spam.items())


# person1 = {
#            'name':'val',
#            'colors':[{"n1":"v1"},{"n2":"v2"},{"n3":"v3"},{"n4":"v4"}],
#            'langs':['english','french','german'],
#            'info':{
#                'number':56737362
#                   }
#             }

# print(person1['colors'][0]['n1'])
# print(person1['info']['number'])

# print(person1["colors"])

# for i in person1["colors"]:
#     # print(i.values())
#     # print(i.keys())
#     print(i.items())

# for i in person1["langs"]:
#     print(i)

# create an empty dictionary
# take user input
# check if the key exists in the dictionary
# then print that value
# if it dont exists, ask the value for that key
# Add that key and value to the dictionary.

# books = {}

# while True:
#     print('Enter a book name: ') 
#     book_title = input() #stranger
#     if book_title == '':
#         break
#     else:
#         if book_title in books.keys():
#             print("The books contains " + books[book_title] + " pages.")
#         else:
#             print('Book doesnt exists:')
#             print('Enter the number of pages to add to the dictionary: ')
#             book_pages = input() #96
#             books[book_title] = book_pages

# print("Books added: ")
# for i in books.keys():
#     print(i)

spam = {'num1':1,'num2':2,'num3':3}

#get
print(spam.get('num4',4))
print(spam)

#setdefault
print(spam.setdefault('num5',5))
print(spam)

#update
spam.update({'num5': 50})
print(spam)

#pop
spam.pop('num1')
print(spam)

#popitem
spam.popitem()
print(spam)

# del spam['num1']

#clear()
spam.clear()
print(spam)

import pprint

text = 'Browse the docs online or download a copy of your own. Pythons documentation, tutorials, and guides are constantly evolving'

count = {}

for i in text:
    count.setdefault(i, 0)  # {'B':0}
    count[i] = count[i] + 1 # {'B':1}

# print(count)
pprint.pprint(count)

####################################
students = {
    "student1": {
        "name": "Alice",
        "age": 20,
        "major": "Computer Science",
        "grades": {
            "math": 95,
            "physics": 88,
            "programming": 92
        }
    },
    "student2": {
        "name": "Bob",
        "age": 21,
        "major": "Engineering",
        "grades": {
            "math": 80,
            "physics": 90,
            "chemistry": 85
        }
    }
}

pprint.pprint(students)