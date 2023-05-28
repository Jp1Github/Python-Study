'List enclosed by []'
'''
list.append(x) Adds item x to the end of the list
list.extend(L) Adds all items in list L to the end of the list
list.insert(i,x) Insert item x at index position i
list.remove(x) Removes first item x from the list
list.pop(i) Removes items x from the list
list.index(x) Returns the index position in the list of first item x
list.count(x) Returns the  number of times x appears in the list
list.sort() Sort all list items in place
list.reverse() Reverse all list items in place.

len(L) function returns the length of the list L.
del list [range value] ex [1] or [1:3] ex. del list[1] or del list[0:3] - this is called slicing
print (type(list))


'''

chars =['A','B','C','D','E','F','G']

names = ['Mark','Kevin','Ivan','Ely','John','Mohan']
        
days = ['Mon','Tues','Wed','Thurs','Fri','Sat','Sun']
        
months = ['January','February','March','April','May','June']

coords = [[1,2,3,4,5],[2,3,4,5,6],[3,4,5,6,7]]

# Practice below this line
print (type(chars)) #<class 'list'>

print (len(names)) # 6

print (names[1:4])# ['Kevin', 'Ivan', 'Ely'] 

print (months[0:2]) # 'January' , 'February'

print (months[0][3])# u

print (months[0][0:5])# Janua zero index up to four (4) excluding five (5)

print (type(coords))# <class 'list'>

print (coords)#[[1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [3, 4, 5, 6, 7]]

print(coords[1])# [2, 3, 4, 5, 6]

print (coords[2][0:3])# [3, 4, 5]


# enumerate () function to display each element's index number and its associate value.
for item in enumerate(chars):# Dont forget the : using the "for" keyword
    
        print (item, end= ' ') 
        #(0, 'A') (1, 'B') (2, 'C') (3, 'D') (4, 'E') (5, 'F') (6, 'G')
    
print('\n')

    
for item in enumerate(months):# Dont forget the : using the "for" keyword

        print (item, end= ' ')
        #(index , value)=(0, 'January') (1, 'February') (2, 'March') (3, 'April') (4, 'May') (5, 'June')
    
print('\n')



# zip () function when looping through multiple list simultaneously the
#elements values of the same index number in each list can be displayed.

for item in zip(chars,months):# Dont forget the : using the "for" keyword
        
        print(item,end = ' ')
        #(value of chars, value of  months)=('A', 'January') ('B', 'February') ('C', 'March') ('D', 'April') ('E', 'May') ('F', 'June
