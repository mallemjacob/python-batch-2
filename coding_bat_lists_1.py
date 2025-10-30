#sum3
# def sum3(nums):
#   final_count = 0
#   for i in nums:
#     if i == 3:
#       continue
#     final_count = final_count + i
#   print(final_count)

# sum3([1, 2, 3, 4, 5]) #12
# sum3([5, 11, 2, 10, 3, 5]) #33
# sum3([5, 11,3]) #16

#reverse3
# def reverse3(nums):
#     new_list = []
#     for i in nums:


# reverse3([1, 2, 3])
# reverse3([5, 11, 9])
# reverse3([7, 0, 0])


#make pi
#take user input, and only add value to list if it has 1,3,4
def make_pi():
    final_list = [] #0
    check_flag = True
    while True:
        print('Enter number 1 or 3 or 4: ')
        if len(final_list) == 3:
            break
        else:
            user_input = int(input()) #4

            if len(final_list) == 0 and user_input == 3:
                if user_input not in final_list:            
                    if user_input == 1 or user_input  == 3 or user_input == 4:
                        final_list = final_list + [user_input]
                    else:
                        print('Wrong answer!')
                else:
                    print('  item!')
            else:
                continue
    print(final_list)
make_pi()