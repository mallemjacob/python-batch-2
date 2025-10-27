#Scopes
# You can access variable
# defined in the global scope
# from local scope.

# You can't access variables
# defined in the local scope
# from global scope.

#global scope
# name = 'hello'
# def hello(username):
#     #local scope
#     name = username
#     print(name)
#     return f"hi {name}"

# print(hello('ingrid'))

# you can't access a variable
# from another local scope
# def a():
#     b()
#     print(name)

# def b():
#     name = 'val'
# a()


# def spam():
#     eggs = 'spam local'
#     print(eggs)
# # prints 'spam local'
# def bacon():
#     eggs = 'bacon local'
#     print(eggs)
# # prints 'bacon local'
#     spam()
#     print(eggs)
# # prints 'bacon local'
# eggs = 'global'
# bacon()
# print(eggs)

name = 'hi'

def hello():
    global name
    name = 'hello'

hello()
print(name)
