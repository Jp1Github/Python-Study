# Object Oriented programming using class
class Employee:
  num_of_emps = 0
  raise_amt = 1.04

  #Initialize the attribute of a class
  def __init__(self, first, last, pay):
    self.first = first
    self.last = last
    self.pay = pay
    self.email = first+'.'+last+'@company.com'
    Employee.num_of_emps += 1

  def fullname(self):
    return '{} {}'.format(self.first, self.last)
  
  def apply_raise(self):
    self.pay = self.pay * self.raise_amt

  # Using a classmethod to change the attribute raise_amt of Employee class
  @classmethod
  def set_raise_amt(cls, amount):
    cls.raise_amt = amount
  
  # Use class method as an alternative constructor
  @classmethod
  def from_string(cls, emp_str):
    first, last, pay = emp_str.split('-')
    return cls(first, last, pay)

  def __str__(self):
    return '{} {}'.format(self.first, self.last)

  def __repr__(self):
    return ' This is {} {}'.format(self.first, self.last)

class Developer(Employee):
  raise_amt = 1.10

  # Sample of Inheritance.
  # Initialize and inherit the attributes of the Employee class
  def __init__(self, first, last, pay, prog_lang=None):
    super().__init__(first, last, pay)
    # Employee.__init__(self, first, last, pay) is same as above
    self.prog_lang = prog_lang

class Manager(Employee):
  def __init__(self, first, last, pay, employees=None):
    super().__init__(first, last, pay)
    # Employee.__init__(self, first, last, pay) is same as above
    if employees is None:
      self.employees = []
    else:
      self.employees = employees
  
  # Function to add an employee under the Manager class
  def add_emp(self, emp):
    if emp not in self.employees:
      self.employees.append(emp)
  
  # Function to remove an employee under the Manager class
  def remove_emp(self, emp):
    if emp in self.employees:
      self.employees.remove(emp)
      print('Removing {} from {}'.format(emp.fullname(),self.fullname()))
    else:
      # Print out that that an employee name is not under this Manager
      print('{} is not under {}'.format(emp.fullname(), self.fullname()))
  
  # Print out the list of employees under a Manager
  def print_emp(self):
    if self.employees == []:# Do not use None. If == None this will not be printed out.
      print('There is no employee to print under {}'.format(self.fullname()))
    
    else:
      print('Employees of {} are:'.format(self.fullname()))
      for emp in self.employees:
        print('-->',emp.fullname())


# Employee Class
emp1 = Employee('Jace','Bardon', 45000)

# Developer Class
dev1 = Developer('Corey','Schafer', 50000, 'Python')
dev2 = Developer('User','Test', 60000, 'Java')
dev3 = Developer('Jose', 'Marcus', 65000, 'Javascript')

# Manager Class
mgr1 = Manager('Sue','Smith',900000, [dev1,dev2, emp1])


print(mgr1.email)
mgr1.print_emp()
mgr1.remove_emp(dev3)
mgr1.remove_emp(dev1)
mgr1.print_emp()
mgr1.remove_emp(dev2)
mgr1.remove_emp(emp1)
mgr1.print_emp()

print(mgr1.__str__())
print(dev1.__str__())

print(mgr1.__str__())
print(str(mgr1))
print(repr(dev1))

# print(dev1.email)
# print(dev1.prog_lang)
# print(dev1.num_of_emps)

# print(help(Developer))
# emp1 = Employee('Corey','Schafer', 50000)
# emp2 = Employee('User','Test', 60000)

# emp_str_1 = 'John-Doe-70000'
# emp_str_2 = 'Steve-Smith-30000'
# emp_str_3 = 'Jane-Doe-90000'


# first, last, pay = emp_str_1.split('-')
# new_emp = Employee(first, last, pay)

# new_emp1 = Employee.from_string(emp_str_1)
# new_emp2 = Employee.from_string(emp_str_2)
# new_emp3 = Employee.from_string(emp_str_3)

# print(new_emp1.email)
# print(new_emp1.pay)
# print('\n')
# print(new_emp2.email)
# print(new_emp2.pay)
# print('\n')
# print(new_emp3.email)
# print(new_emp3.pay)



