# Memoization
''' Memoization is an optimization technique used
primarily to speed up computer programs by storing the 
results of expensive function calls and returning the cache
result when the same inputs occur again'''

import time

def expensive_funct(num):
    print('Computing {}...'.format(num))
    time.sleep(1)
    return num * num

# results = expensive_funct(5)
# print (results)

# results = expensive_funct(10)
# print (results)

# results = expensive_funct(5)
# print (results)

# results = expensive_funct(10)
# print (results)

'''Computing 5...
25
Computing 10...
100
Computing 5...
25
Computing 10...
100 '''

# Create a dictionary to cache that is already computed

ef_cache ={}

def expensive_funct(num):
    if num in ef_cache:
        print('{} is already computed giving results'.format(num))
        return ef_cache[num]

    print('Computing {}...'.format(num))
    time.sleep(1)
    result = num * num
    ef_cache[num] = result
    return result

results = expensive_funct(5)
print (results)

results = expensive_funct(10)
print (results)

results = expensive_funct(5)
print (results)

results = expensive_funct(10)
print (results)