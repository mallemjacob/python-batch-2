# Sequence data types
# 1.Lists -> Mutable
# 2.Strings -> Immutable
# 3.Tuples -> Immutable


# colors = ['black','red']
# cc = colors
# colors.append('blue')
# print(colors)
# print(cc)

# print(id(colors))
# print(id(cc))



# spam = 'It is a cat'

# It is the cat
# new_spam = spam[0:6] + 'the' + spam[7:]
# print(spam)
# print(new_spam)

# print(id(spam))
# print(id(new_spam))
# for i in spam:
#     print(i)


# def centered_average(nums):
#     nums.pop(nums.index(min(nums)))
#     nums.pop(nums.index(max(nums)))

#     total = 0
#     count = 0
#     for i in nums:
#         count = count + 1
#         total = total + i

#     return total // count

    

# print(centered_average([1, 2, 3, 4, 100]))
# print(centered_average([1, 1, 5, 5, 10, 8, 7]))
# print(centered_average([-10, -4, -2, -4, -2, 0]))

# def sum13(nums):
#     total = 0
#     if len(nums) == 0:
#         total = 0
#     for i in range(len(nums)):  
#         if nums[i] == 13 and nums[i+1]:
#             continue
#         else:
#             total = total + nums[i]
#             continue
            
#     return total



spam = ['cat','bat','ft','mm']

for i in range(len(spam) - 1):
    print(i)

# def sum13(nums):
#   total = 0
#   if len(nums) == 0:
#     total = 0
#   for i in range(len(nums) -1):
#     if nums[-1] == 13:
#       nums[-1] = 0
#     if nums[i] == 13:
#         nums.pop(i)
#         pass
#     else:
#       total = total + nums[i]
#   return total

# print(sum13([1, 2, 2, 1, 13, 6, 4, 5])) #15
# print(sum13([1, 2, 2, 1, 13])) #6