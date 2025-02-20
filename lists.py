'''Imagine we recieived album recommendations from a friend and compiled all of 
the recommendations into a table, with specific information about each album.
We have one row for each movie and several columns including 
->Artist 
->Album
->Released year 
->length min sec
->Genre 
->Music recording saltes 
->Calimed sales 
->Release year 
->Soundtrack 
->Rating of friend 
'''

# create a list 
list = ['The Body Guard','7.0','1992']
print(list)
# Using negative indexing to print the elements in asscending order 
print(f"The first lement of the list \nusing negative index {list[-3]} \nusing positive indexing {list[0]}")
print(f"The second lement of the list \nusing negative index {list[-2]} \nusing positive indexing {list[1]}")
print(f"The third lement of the list \nusing negative index {list[-1]} \nusing positive indexing {list[2]}")
# Lists can also contain lists and tuples inside them 
list =['The body guard ','7.0','1992',("A1",23),[0,2]]
print (list)
# We can also use slicing in lists for example 
print(list[3:len(list)])
# len(x) will give us length of x ? here lenght of x is for we slice mostly from starting index ? 
# to 1 more then last index 

# Adding elements to a list 
# Two main ways using .append() or .extend 

# Using .extend 

list.extend(['Zulqarnain',[1,0]])
print(list)

# using .append()

list.append(['Sir Irfan Ishaq',[9,0],(1)])
print(list)

# ALl lists are mutable
# Lets mutate the first element of the list  
list[0]='Sajid Iqbal'
print(list)

# converting a string into a list using the split function

str = 'Dr. Adil Eng. Sajid Eng. Irfan'
print (str.split())
# We can use split function to split the string into a list using our own splitting character 
print(str.split("Eng."))