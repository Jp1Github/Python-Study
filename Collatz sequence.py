''' The collatz () has one parameter named number. If a number is even,
then collatz() should print number // 2 and return this value. If number
is odd, then collatz() should print and return 3 * number +1.
It keeps calling the collatz function on that number until the function returns
the value 1.
Amazingly this sequence actually works for any integer -- sooner or later
you'll arrive at 1!. Collatz sequence sometime called the 'simplest impossible
math problem'

Hint: An integer number is even if number % 2 == 0 (remainder) and odd if
number % 2 == 1.
'''


# This is the collatz sequence function.

import time
def collatz(num):
  # print(num)
  if num == 1:
    print(num)
    return 'end'

  if (num % 2) == 0:
    print(num)
    num = num // 2
    time.sleep(1)
    return collatz(num) # This is a recursion!

  else:
    print(num)
    num = 3 * num + 1
    time.sleep(1)
    return collatz(num) # This is a recursion!

# print(collatz(3))
# collatz(300)

# print(str.isdigit('5')) Return True.

# This function is to run the collatz sequence.
def collatz_run():
  print('Running collatz_run() ')
  num =input('Input a number ')

  '''Return True if all characters in the string are digits and there is 
  at least one character, False otherwise. Digits include decimal characters 
  and digits that need special handling, such as the compatibility 
  superscript digits. This covers digits which cannot be used to form numbers
  in base 10, like the Kharosthi numbers. Formally, a digit is a character 
  that has the property value Numeric_Type=Digit or Numeric_Type=Decimal.'''
  if str.isdigit(num) == True:
    # Calls the collatz sequence function.
    collatz(int(num))

  else:
    print('Input \'{}\' is not a valid input'.format(num))

collatz_run()

''' This is the collatz run function with the exception handling (Try - 
Exception'''
def collatz_run_try():
  print('Running collatz_run_try() ')
  num =input('Input a number ')

  try:
    # int(num) // 2
    # int(num)
    collatz(int(num))

  except (ValueError, TypeError):
   print('Input \'{}\' is not valid to run the collatz sequence. '
         'You must enter an whole integer'.format(num))

collatz_run_try()

''' This is collatz function that can handle decimal but can be a whole number
without rounding off'''
def collatz_run_float():
  print('Running collatz_run_float() ')
  num = input('Enter a whole number ')

  x = float(num)

  if x == round(x):
    collatz(round(x))

  else:
    print('Not a valid input')

collatz_run_float()
