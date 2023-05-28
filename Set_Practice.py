'''Set enclosed by {}

The values in a regular list or a fixed list tuple can be repeated in its elements, but a list
of unique values can be created where duplication is not allowed. A restrictive Python list of unique
values is known as a "set" and is created by assigning values as a comma-separated list between curly
bracket(braces) like this:
code_set = {'Alph','Bravo','Charlie','Delta','Foxtrot'}

Unlike regular list or tuples, individual elements in a set cannot be referenced using the set name followed
by square brackets containing an index number. Instead, set have powerful methods that can be dot-suffixed to
the set name for manipulating and comparison


Set Method:

set.add(x) Adds item x to the set
set.update(x,y,z) Adds multiple items to the set
set.copy() Returns a copy of the set
set.pop() Removes one random item from the set
set.discard(i) Removes item at position i form the set
set1.intersection(set2) Returns items that appear in both sets
set1.difference(set2) Returns items in set 1 but not in set 2
'''

'Set samples:'

chars ={'A','B','C','D','E','F','G'}

names = {'Mark','Kevin','Ivan','Ely','John','Mohan'}
        
days = {'Mon','Tues','Wed','Thurs','Fri','Sat','Sun'}
        
months = {'January','February','March','April','May','June'}

#colors_set = ('Red','Green','Red','Blue','Red','Yellow')#This is not a set because Red appears many times & ()
colors_set = {'Red','Green','Red','Blue','Red','Yellow'}

#coords = {[1,2,3,4,5],[2,3,4,5,6],[3,4,5,6,7]}#TypeError: unhashable type: 'list'
#coords = {{1,2,3,4,5},{2,3,4,5,6},{3,4,5,6,7}}#TypeError: unhashable type: 'set'

# Practice below this line

print (type(chars)) #<class 'set'>

print ('Length of names : '+ str(len(names))) # 6 when using len starts at one(1) not zero

print (colors_set)#{'Blue', 'Yellow', 'Green', 'Red'}-Only printed one "Red"

colors_set.add('Purple')
print(colors_set)#{'Purple', 'Yellow', 'Green', 'Red', 'Blue'}-Output changes everytime it is runned!!!!


colors_set.update('Brown','Orange','Black')#('Violet','Red') Scrambled!!!!!
print(colors_set)#{'V', 'i', 'e', 'r', 'w', 'B', 'Blue', 'n', 'O', 'g', 'Purple', 'l', 'k', 'c', 'd', 'Red', 'Green', 'o', 'Yellow', 't', 'R', 'a'}
                # {'Green', 'n', 'a', 'Yellow', 'O', 'Red', 'B', 'g', 'e', 'c', 'Blue', 'r', 'k', 'o', 'l', 'w', 'Purple'}

colors_set.copy()# nothing happens!


###
colors_set = {'Red','Green','Red','Blue','Red','Yellow'}
colors_set.pop()
print (colors_set)#{'Blue', 'Yellow', 'Red'}
###


###
colors_set = {'Red','Green','Red','Blue','Red','Yellow'}
colors_set.discard(2)
print (colors_set)#{'Green', 'Blue', 'Red', 'Yellow'}
colors_set.discard(1)
print (colors_set)#{'Green', 'Blue', 'Red', 'Yellow'} nothing has been removed!!!!
###


### intersection and difference method
party_class = {'Mandy','Eddie','Stuart','Kelvin','Sam'}
students = {'Andrew','Kelly','Lyn','David','Kelvin','Mandy'}

print(type(party_class))#<class 'set'>
print(party_class)#{'Mandy', 'Sam', 'Eddie', 'Kelvin', 'Stuart'}
print('Did Mandy go? ', 'Mandy' in party_class)#Did Mandy go?  True
print('Did Mark go? ', 'Mark' in party_class)#Did Mark go?  False

commons = party_class.intersection(students)
print(commons)#{'Mandy', 'Kelvin'}
' Initialize a regular list (set) of the common values so that elements can be individually accessed.'
party_students = list(commons)
print('Student at the party : ',party_students)#
print('First student at the party: ',party_students[0])#First student at the party:  Kelvin

#print (names[1:4])#print (names[1:4])# ['Kevin', 'Ivan', 'Ely']
#TypeError: 'set' object is not subscriptable


#print (months[0:2]) #print (months[0:2]) # 'January' , 'February'
#TypeError: 'set' object is not subscriptable


#print (colors_tuple[1][4])# print (months[0][0:5])# Janua zero index up to four (4) excluding five (5)
#TypeError: 'set' object does not support indexing

#print (months[0][0:5])#   print (months[0][0:5])# Janua zero index up to four (4) excluding five (5)
#TypeError: 'set' object does not support indexing

#print (coords)#    print (coords)#[[1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [3, 4, 5, 6, 7]]
#NameError: name 'coords' is not defined

#print(coords[1])#print(coords[1])# [2, 3, 4, 5, 6]
#NameError: name 'coords' is not defined

#print (coords[2][0:3])# print (coords[2][0:3])# [3, 4, 5]
#NameError: name 'coords' is not defined


# enumerate () function to display each element's index number and its associate value.
#for item in enumerate(chars): # Dont forget the : using the "for" keyword - In set invalid syntax
    
        #print (item, end= ' ') Invalid Syntax
        # Results(0, 'E') (1, 'A') (2, 'G') (3, 'D') (4, 'B') (5, 'F') (6, 'C')-Not in the same order as they
        #appear in the set chars ={'A','B','C','D','E','F','G'}
    
#print('\n')

    
#for item in enumerate(months): # Dont forget the : using the "for" keyword

        #print (item, end= ' ')
        #(0, 'February') (1, 'March') (2, 'January') (3, 'April') (4, 'June') (5, 'May')-Not in the same order
        #(index , value)=(0, 'January') (1, 'February') (2, 'March') (3, 'April') (4, 'May') (5, 'June')
    
#print('\n')



# zip () function when looping through multiple list simultaneously the
#elements values of the same index number in each list can be displayed.

#for item in zip(chars,months):# Dont forget the : using the "for" keyword
        
        #print(item,end = ' ')
        #('E', 'February') ('A', 'March') ('G', 'January') ('D', 'April') ('B', 'June') ('F', 'May')-Not in the same order
        #(value of chars, value of  months)=('A', 'January') ('B', 'February') ('C', 'March') ('D', 'April') ('E', 'May') ('F', 'June
