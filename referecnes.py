# Strings = Immutable
spam = 'hi'
b = spam

print(id(spam))
print(id(b))

spam = 'bye'
print(id(spam))

# Lists = Mutable
# spam = ['cat','bat','rat','mat']
# print(id(spam))
# cheese = spam
# cheese[0] = 'hi'

# print(spam)
# print(cheese)

# spam.append('bye')
# print(spam)



# print(spam)
# spam = [1,2,3,4]

# spam.clear()
# print(spam)
# spam.append(1)
# print(spam)

# print(id(spam))
# print(id(cheese))



def greet(p):
    print(id(p))
    p.append('hi')

spam = ['cat','bat','rat','mat']
greet(spam)
print(id(spam))
print(spam)

# copy modules

import copy

spam = ['cat','bat','rat','mat',[1,2,3]]

#copy list values instead of references.
# cheese = copy.copy(spam) 

#copies inner lists as well.
cheese = copy.deepcopy(spam) 

print(id(spam))
print(id(cheese))

cheese[0] = 'hi'
print(spam)
print(cheese)

