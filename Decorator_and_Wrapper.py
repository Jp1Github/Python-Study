# Python Decorators

def outer_function(msg):
  def inner_function():
    print(msg)
  return inner_function

hi_func = outer_function('Hi')
bye_func = outer_function('Bye')

# hi_func()
# bye_func()

# Import the wraps module from the functools library.
from functools import wraps

def decorator_function(original_function):
  # @wraps(original_function)
  def wrapper_function(*args, **kwargs):
    print('wrapper executed before {}'.format(original_function.__name__))
    return original_function(*args,**kwargs)
  return wrapper_function

'''decorated_display = decorator_function(display)
decorated_display == wrapper_function w/o executing!
decorated_display()'''

# Decorator class
class decorator_class(object):

  def __init__(self, original_function):
    self.original_function = original_function
  
  def __call__(self, *args,**kwargs):
    print('call method executed before {}'.format(self.original_function.__name__))
    return self.original_function(*args, **kwargs)

# @decorator_function
@decorator_class
def display():
  print('display function ran')

# @decorator_function same as 
# display = decorator_function(display)
# display()
'''wrapper executed before wrapper_function
wrapper executed before display
display function ran'''

# @decorator_function
@decorator_class
def display_info(name, age):
  print('display_info ran with arguments({}, {})'.format(name, age))

display()
print('\n')
display_info('John', 25)

# from functools import wraps
# import time

# def my_logger(original_function):
#   import logging
#   logging.basicConfig(filename='{}.log'.format(original_function.__name__), level=logging.INFO)

#   @wraps(original_function)
#   def wrapper(*args, **kwargs):
#     loggin.info('Ran with args: {}, and kwargs: {}'.format(args, kwargs))
#     return original_function(*args,**kwargs)

#   return wrapper

# def my_timer(original_function):
#   import time

#   @wraps(original_function)
#   def wrapper (*args, **kwargs):
#     t1 = time.time()
#     result = original_function(*args, **kwargs)
#     t2 = time.time() - t1
#     print('{} ran in: {} sec'.format(original_function.__name__, t2))
#     return result

#   return wrapper

# # @my_logger
# # @my_timer
# def display_info(name, age):
#   time.sleep(1)
#   print('display_info ran with arguments({}, {})'.format(name, age))

# display_info('Pym', 35)