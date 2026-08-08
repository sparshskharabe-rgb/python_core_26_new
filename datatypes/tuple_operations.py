# create an empty tuple
cityList = ()
print(type(cityList))

name = ('Ramesh')
print("Type of name :", type(name))

name = ('Ramesh',)
print("Type of name :", type(name))

# create a list with metro cities names
cityList = ('Mumbai', 'Pune', 'Delhi', 'Kolkatta', '')
print(type(cityList))
print(cityList)

numList = (10, 20, 30, 40, 50)
print(type(numList))
print(numList)

empList = ('Ramesh', 1001, 'Pune', True, 20.5) # Mixed Type
print(type(empList))
print(empList)

# Length of the list
size = len(empList)
print(size)


# Accessing the items
item1 = empList[0] # First Item
print(item1)
print(empList[1])
print(empList[2])
print(empList[3])
print(empList[4]) # Last Item
print(empList[size-1]) # Last Item
# print(empList[5]) #IndexError: list index out of range


# Nested List
empList = ('Ramesh', 1001, 'Pune', True, 20.5, ['ML', 'AI', 'DE', 'Python']) # Mixed Type
print(type(empList))
print(empList)
size = len(empList)
print('Size of tuple', size)

#Access
firstItem = empList[0] #First
print(firstItem)
print(type(firstItem))
print(empList[1])
print(empList[2])
print(empList[3])
print(empList[4])
lastItem = empList[size-1] # Last Item => ['ML', 'AI', 'DE', 'Python']
print(lastItem)
print(type(lastItem))

# Accessing the lastItem list's item
print(lastItem[0])
print(lastItem[1])
print(lastItem[2])
print(lastItem[3])



# Slicing
# [start:end:step] => defaults => start: 0, end: length, step: 1

print("Slicing starts....")
#             -6      -5     -4     -3    -2             -1
empList = ('Ramesh', 1001, 'Pune', True, 20.5, ('ML', 'AI', 'DE', 'Python')) # Mixed Type
#             0        1      2      3     4              5
print(type(empList))
print(empList)
size = len(empList)
print(size) # length = 6

print(empList[-1]) # ['ML', 'AI', 'DE', 'Python']
print(empList[1:3:1]) # [1001, 'Pune']
print(empList[1:3]) # [1001, 'Pune']
print(type(empList[1:3])) # list
print(empList[1:]) # [1001, 'Pune', True, 20.5, ['ML', 'AI', 'DE', 'Python']]
print(empList[:4]) # ['Ramesh', 1001, 'Pune', True]
print(empList[:]) # ['Ramesh', 1001, 'Pune', True, 20.5, ['ML', 'AI', 'DE', 'Python']]
print(empList[::]) # ['Ramesh', 1001, 'Pune', True, 20.5, ['ML', 'AI', 'DE', 'Python']]
print(empList[-1][-1]) # 'Python'
print(type(empList[-1][-1])) # <class 'str'>
print(empList[0:4:4]) # 'Ramesh'

print("Slicing ends.")

# point to remember : No support for Mutability in Tuples, so no insert/append methods


# iterate over the list
# name, id, city, isCertified, score, list of expertise
empList = ('Ramesh', 1001, 'Pune', True, 20.5, ('ML', 'AI', 'DE', 'Python')) # Mixed Type
for item in empList:
    print(item)


emplList : ('Ramesh', 1001, 'Pune', 'Aadhaar', '222222222222222', 50000, True, 20.5, ('ML', 'AI', 'DE', 'Python'), 'A birth mark on right hand', ('C-Pune City', 'P-Nagpur City'))
# check if an item is present or not in the list

item_to_remove = 'Pune'

if item_to_remove in empList:
    print("Item Found.")



# Tuple copy

empList = ('Ramesh', 1001, 'Pune', True, 20.5, ('ML', 'AI', 'DE', 'Python'))
print(empList)
finalCopiedList = tuple(empList) # Separate copy
print("Copied Tuple :", finalCopiedList)



del empList

print(empList)



tuple