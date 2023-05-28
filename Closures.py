# Closures

''' Wikipedia says, "A closure is a record storing a function together with an
environment: a mapping associating each free variable of the function with the
value or storage location to which the name wa bound when the closure was created.
A closure, unlike a plain function, allows the function to access those captured
variables through the closure's reference to them, even when the function is invoked
outside their scope '''

###
def outer_function():
    message = 'Hi'
    def inner_function():
        print (message)
    # return inner_function()

outer_function()

###
def outer_function(msg):
    def inner_function():
        print (msg)
    return inner_function()

# outer_function('Hello')

###
''' Below is similar to the Decorator function '''

def decorator_function(message):
    def wrapper_function():
        print (message)
    # Return the wrapper_function not executed. No "()"
    return wrapper_function 

# hello_function = decorator_function('Hello there!')
# hello_function()

### Decorator function passing a function.
# def decorator_function(original_function):
#     def wrapper_function():
#         return original_function()
#     return wrapper_function

# def display ():
#     print('display function ran')

# decorated_display = decorator_function(display)
# decorated_display()

### Putting argument or keywords argument
def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print('wrapper executed this before {} function'.format(original_function.__name__))
        return original_function(*args, **kwargs)
    return wrapper_function

@decorator_function
def display ():
    print('display function ran')

''' The @decorator function is equivalent to 
display = decorator_function(display) '''

# display()
# print('\n')

@decorator_function
def display_info(name, age):
    print('display_info ran with arguments ({},{})'.format(name, age))

# display_info('Jamie', 30)

### Using a class decorator

class decorator_class(object): # Still works without the 'object' word.
    def __init__(self,original_function ):
        self.original_function = original_function
    
    def __call__(self,*args, **kwargs):
        print(('call method executed this before {} function'.format(self.original_function.__name__)))
        return self.original_function(*args, **kwargs)

@decorator_class
def display_info(name, age):
    print('display_info ran with arguments ({},{})'.format(name, age))

# display_info('Jordan', 25)

###
### Importing wraps from functools

from functools import wraps
import time

def my_logger(original_function):
  import logging
  logging.basicConfig(filename='{}.log'.format(original_function.__name__), level=logging.INFO)

  @wraps(original_function)
  def wrapper(*args, **kwargs):
    logging.info('Ran with args: {}, and kwargs: {}'.format(args, kwargs))
    return original_function(*args,**kwargs)

  return wrapper

def my_timer(original_function):
  import time

  @wraps(original_function)
  def wrapper (*args, **kwargs):
    t1 = time.time()
    result = original_function(*args, **kwargs)
    t2 = time.time() - t1
    print('{} ran in: {} sec'.format(original_function.__name__, t2))
    return result

  return wrapper

# Stack version is display_info = my_logger(my_timer(display_info))
@my_logger
@my_timer
def display_info(name, age):
  time.sleep(1)
  print('display_info ran with arguments({}, {})'.format(name, age))

# @my_timer
# @my_logger
# def display_info(name, age):
#   time.sleep(1)
#   print('display_info ran with arguments({}, {})'.format(name, age))

display_info('Pym', 35)
display_info('Terry', 42)