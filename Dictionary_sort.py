# Sorting a dictionary
'''Dictionaries can't be sorted directly, so you need to instead sort the items(), the list
 of tuples containing key/value pairs.

 Since you want to sort by the value field, then the keys fields, it is necessary to extract
 those field.

 Lastly to sort descending on one field and descending on another, do two passes, first sorting
 by the secondary key ascending, and then another pass sorting by the primary key descending.'''

# sorted (obj, key ='', reverse = False(by default))

import operator

# Example dictionary
fruits = {'banana': 3, 'orange': 5, 'apple': 5, 'avocado': 3}


# A. Sort by keys
#  Same thing like sorted_fruit_keys = sorted(fruits.keys())
sorted_fruit_keys = sorted(fruits)
print('A. ', sorted_fruit_keys) #  ['apple', 'avocado', 'banana', 'orange']


# B. Sort by values
sorted_fruit_values = sorted(fruits.values())
print('B. ', sorted_fruit_values, '\n')# [3, 3, 5, 5]


# C. List comprehension. item function convert a dict to tuples.
a = [(k, v) for k, v in fruits.items()]
#print(a) #  [('banana', 3), ('orange', 5), ('apple', 5), ('avocado', 3)]
b = sorted(a)
print('C. Sorted  ', b)# [('apple', 5), ('avocado', 3), ('banana', 3), ('orange', 5)]

b = sorted(a, key=lambda x: -x[1], reverse = False)
print('C1 reverse False', b)# [('orange', 5), ('apple', 5), ('banana', 3), ('avocado', 3)]

b = sorted(a, key=lambda x: -x[1], reverse=True)
# Same as b = sorted( a, key = lambda x : x[1], reverse = False)
print('C1 reverse True', b)# [('banana', 3), ('avocado', 3), ('orange', 5), ('apple', 5)]

b.reverse()
print('C1 b.reverse ', b, '\n')# [('apple', 5), ('orange', 5), ('avocado', 3), ('banana', 3)]


# D. Sort by value then keys. Highest values put -x[1] but string lowest
a = sorted(fruits.items(), key=lambda x:(-x[1], x[0]))
print('D. ', a,'\n')# [('apple', 5), ('orange', 5), ('avocado', 3), ('banana', 3)]

# E. Results if a reverse is True
a = sorted(fruits.items(), key=lambda x: (-x[1], x[0]), reverse=True)
print('E ', a, '\n') #[('banana', 3), ('avocado', 3), ('orange', 5), ('apple', 5)]


#  F. If want to sort values from lowest to highest  do not put (-) in x[1]
a = sorted(fruits.items(), key= lambda x : (x[1], x[0]))
print('F. ', a,'\n')#  [('avocado', 3), ('banana', 3), ('apple', 5), ('orange', 5)]


# G. Results if a reverse is True
a = sorted(fruits.items(), key= lambda x : (x[1], x[0]), reverse=True)
print('G. ', a)#  [('orange', 5), ('apple', 5), ('banana', 3), ('avocado', 3)]
print('G. dict ', dict(a), '\n')# Convert tuple to a dictionary.


# H. Using itemgetter. Should import the operator otherwise 'operator' not defined
# Same as " sorted_fruit_keys = sorted(fruits) "
a = sorted(fruits, key=operator.itemgetter(0))
print('H. ', a, '\n')# ['apple', 'avocado', 'banana', 'orange']


# I. Two sort passes
first_sort_pass = sorted(fruits.items(), key=operator.itemgetter(0))
print('I. First sort results \n', first_sort_pass, '\n')# [('apple', 5), ('avocado', 3), ('banana', 3), ('orange', 5)] converted into a list (from dict)


second_sort_pass = sorted(first_sort_pass, key=operator.itemgetter(1))
print('I. Second sort results \n', second_sort_pass, '\n')# [('avocado', 3), ('banana', 3), ('apple', 5), ('orange', 5)]
# Will not work if first_sort_pass.items() because it is no longer a dictionary!


#  J.Can use itemgetter (x1, x2)
a = sorted(fruits.items(), key=operator.itemgetter(1, 0))
print('J. Using itemgetter with 2 args \n', a, '\n') # [('avocado', 3), ('banana', 3), ('apple', 5), ('orange', 5)]

a = sorted(fruits.items(), key=operator.itemgetter(1, 0), reverse=True)
print('J. Using itemgetter with 2 args reverse True \n', a, '\n') # [('orange', 5), ('apple', 5), ('banana', 3), ('avocado', 3)]


#  K. Then sort the keys!
b = sorted(a, key=operator.itemgetter(0))
print('K. ', b, '\n')#  [('apple', 5), ('avocado', 3), ('banana', 3), ('orange', 5)]


# L. Inside sorted
x =  [(k, v) for k, v in sorted(fruits.items(), key=operator.itemgetter(1))]
print('L. Inside sorted', x)#  [('banana', 3), ('avocado', 3), ('orange', 5), ('apple', 5)]
# Putting a reverse
x =  [(k, v) for k, v in sorted(fruits.items(),key=operator.itemgetter(1), reverse=True)]
print('L. Inside sorted reverse True ', x,'\n') # [('orange', 5), ('apple', 5), ('banana', 3), ('avocado', 3)]


# M. Sorted in sorted
x = [(k, v) for k, v in sorted(fruits.items(),key=operator.itemgetter(0))]
print('M. ', x)# [('apple', 5), ('avocado', 3), ('banana', 3), ('orange', 5)]


# Same as above the (-1) has no effect
# a = sorted(fruits.items(), key = operator.itemgetter(-1, 0), reverse = True)
# print('Using itemgetter with 2 args reverse True \n', a)# [('orange', 5), ('apple', 5), ('banana', 3), ('avocado', 3)]

# lambda does not work with itemgetter(0)
# Error!!!  first_sort_pass = sorted(fruits, key = lambda x: x.itemgetter(0))
# AttributeError: 'str' object has no attribute itemgetter

# first_sort_pass = sorted(fruits, key = lambda x: x.itemgetter(0))
# print('First sort results', first_sort_pass)

# Error!!! first_sort_pass = sorted(fruits.items(), key = lambda x: x.itemgetter(0))
# AttributeError: 'tuple' object has no attribute itemgetter
