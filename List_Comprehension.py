'''List comprehension samples'''
# Create a list of numbers
nums =[]
for i in range(1, 11):
    nums.append(i)
# print(nums)

# Want 'n*n' for each 'n' in nums
my_list =[]
# for n in nums:
#     my_list.append(n*n)

# List comprehension equivalent
# my_list1 =[n*n for n in nums]

# Using map and lambda
# Without the list function it will only return a map object
# my_list2 = list(map(lambda n: n*n, nums))

# print(my_list)
# print(my_list1)
# print(my_list2)

# Want n in nums if the n is even
# for n in nums:
#     if n%2 == 0:
#         my_list.append(n)

# Using filter and lambda function
my_list = list(filter(lambda x: x%2 == 0, nums))
print(my_list)


# List comprehension equivalent
my_list = [n for n in nums if n%2 == 0]
print(my_list)


# Tuple
# my_list =[]
# for letter in 'abcd':
#     for n in range(4):
#         my_list.append((letter, n))

# List Comprehension equivalent
# my_list = [(letter, n) for letter in 'abcd' for n in range(4)]
# print(my_list)


# Dictionary comprehension
# names = ['Clark', 'Bruce', 'Wally', 'Hall', 'Billy']
# heroes = ['Superman', 'Batman', 'Flash', 'GreenLantern', 'Shazam']

# print(list(zip(names,heroes)))

# heroes_dict ={}
# for name, hero in zip(names, heroes):
#     heroes_dict[name] = hero
# print(heroes_dict)

# List comprehension of Dictionary
# heroes_dict = {name:hero for name, hero in zip(names, heroes)}
# heroes_dict = {name:hero for name, hero in zip(names, heroes) if name != "Billy"}
# print(heroes_dict)


# Set Comprehension
# nums1 = [1,1,3,2,3,3,4,7,9,7,7,5,8,9,5,9,10]
# Create an empty set
# my_set = set()

# for n in nums1:
#     my_set.add(n)

# List comprehension equivalent use {} for set comprehension
# my_set1 = {n for n in nums1}
# print(my_set) #{1, 2, 3, 4, 5, 7, 8, 9, 10}
# print(my_set1) #{1, 2, 3, 4, 5, 7, 8, 9, 10}


# Generator comprehension
# def gen_func(nums):
#     for n in nums:
#         yield n * n

# my_genFunc = gen_func(nums)
# my_genFunc = (n*n for n in nums)

# for x in my_genFunc:
#     print(x, end='\t')
