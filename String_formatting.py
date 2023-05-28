#String formating
'''Str.upper(), Str.lower(), Str.title(), Str.swapcase()
Str.find('string word'), Str.replace('string that will be replaced', string to replace')'''


greeting = 'Hello Ola'
name = 'mitch Leaving'

# # Will print out the same thing
# print(f'{greeting}, {name}. Welcome!')
# print('{}, {}. Welcome!'.format(greeting,name))
# print('%s, %s. Welcome!'%(greeting,name))

# print('\n')

#print(f'{greeting}, {name}. Welcome!') can use upper lower
# print(f'{greeting.upper()}, {name}. Welcome!')
#print(f'{greeting.replace('Hello','Hi')}')# will not work!!!

# Should assign with a new greeting or another assignment
greeting = greeting.replace('Hello','Hi')
# print(f'{greeting.upper()}, {name}. Welcome!')

# name = name.swapcase()
# print(name)

# name = name.title()
# print(name)

#getting attribute of variables
#print(dir(name))# just print out information.
#give more details
#print(help(str))

#for specific detail
#print(help(str.title))

''' Advance String Formatting'''

# Using a Dictionary in string formatting

# info = {'first_name':'Romanov', 'last_name': 'Dmitrey', 'age':26}

# print('The student name is {} {} and he is {} years old'.format(info['first_name'], info['last_name'], info['age']))

# Can explicit to place numbered place holders
# print('The student name is {0} {1} and he is {2} years old'.format(info['first_name'], info['last_name'], info['age']))

# Can use key values of the dictionary in the place holders
# print('The student name is {0} {1} and he is {2} years old'.format(info['first_name'], info['last_name'], info['age']))

# Alternative if placed in place holder the key values does not need '' quotation marks
# print('The student name is {0[first_name]} {0[last_name]} and he is {0[age]} years old'.format(info))

# When it is in a class
# class Person():
#     def __init__(self, first_name, last_name, age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age

# p1 = Person('Jenny', 'Holland', 23)
# Treat it like an attribute eg.p1.first_name
# print('The student name is {0.first_name} {0.last_name} and she is {0.age} years old'.format(p1))

# print(p1.first_name, 'first name')


# Can be used in repeating situation
# tag = 'h1'
# text = 'This is a headline'
# print('<{0}>{1}</{0}>'.format(tag, text))

# Padding zero
# for i in range(1, 11):
    # Padding zero to make it 2 digits
    # print('The vaule is {:02}'.format(i))
    # Padding zero to make it 3 digits
    # print('The vaule is {:03}'.format(i))

'''If want formatting in place holder just put a colon {:}'''
# Decimal formatting
# pi = 3.14159265
# To only 3 decimal number .3f
# print('Pi is equivalent to {:.3f}'.format(pi))
# To put a comma separator
print('1 MB is equivalent to {:,}'.format(1000**2))
print('1 MB is equivalent to {:,.2f}'.format(1000**2))

import datetime

find_day = datetime.datetime(2023,11, 3, 12, 20, 23)
print(find_day)
print('{: %B %d, %Y}'.format(find_day)) #May 20, 2023

# Without the index it will not work {:%B, %d, %Y}. Correct {0:%Y}
sentence = '{0:%B %d, %Y} fell on a {0:%A} and was the {0:%j} of the year'.format(find_day)
print(sentence)