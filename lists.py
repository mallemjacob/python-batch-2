                        #-3   #-2   #-1                     
# spam = ['cat','rat','bat','black','red']
         #0    #1     #2    #3

# print(spam[0])
# print(spam[1])
# print(spam[2])

#CRUD - Create, read, update and delete
#reading list item
# print(spam[-1])
# print(spam[len(spam) - 1])

# #updating list item
# spam[2] = 'elephant'

# print(spam)

# #deleting list item
# del spam[2]
# print(spam)

# #creating list
# colors = []

# colors = ['white'] + ['black']
# colors = colors + ['blue']

# print(colors)



# sclice

# spam = ['cat','rat','bat','black','red']
# print(spam[0:3])
# print(spam[-1:-6:-1])


# for i in range(len(spam)):
#     if spam[i] == 'bat':
#         spam[i] = 'new value'
#     print(spam[i])

# for i in spam:
#     print(i)

# catNames = []

# while True:
#     print('Enter cat ' + str(len(catNames) + 1) + ' name:')
#     name = input()
#     if name == 'exit':
#         break
#     elif name in catNames:
#         print('duplicate name!!!')    
#     else:
#         catNames = catNames + [name]
# print(catNames)


# def sum3(nums): #[1, 2, 3, 4, 5, 6]
#     sum = 0
#     for i in nums: #1, 2, 3, 4, 5, 6
#         if i == 3:
#             continue
#         sum = sum + i
#     print(sum)


# sum3([1, 2, 3, 4, 5, 6]) # 18
# sum3([1, 2]) #3
# sum3([1, 2, 3, 4, 5]) #12

#enumerate
spam = ['cat','rat','bat','black','red']

for index, item in enumerate(spam):
    print("Index :" + str(index) + " Item: " + item)

#Multiple assignment or Tuple unpacking

cat = ['black','loud','fast']
color = cat[0]
sound = cat[1]
speed = cat[2]

colors, sound, speed = cat
# print(colors)
# print(sound)
# print(speed)


#Index method
cat = ['black','loud','fast']
print(cat.index('fast'))

for i in cat:
    val = input()
    if val not in cat:
        print(cat.index(val))
    else:
        print('List item do not exist')