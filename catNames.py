# catNames = []

# while True:
#     print('Enter cat ' + str(len(catNames) + 1) + ' name:')
#     name = input()
#     if name == 'exit':
#         break
#     catNames = catNames + [name]

# print(catNames)
##############################################


catNames = []

while True:
    print('Enter cat ' + str(len(catNames) + 1) + ' name:')
    name = input()
    if name == 'exit':
        break
    duplicateNameFound = False
    for i in catNames:
        if i == name:
            print('duplicate name!!!')
            duplicateNameFound = True
            break
    if duplicateNameFound == False:            
        catNames = catNames + [name]
    
print(catNames)



