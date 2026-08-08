# 1st way : using set() constructor

aset = set() # Empty set
print(type(aset))
print(aset)


# 2nd way, creating set with elements initialized
aset = {1001, 'Ramesh', 'Pune', True}
print(type(aset))
print(aset)

# Creating a set with 'set()' constructor and add items to it using 'add()'
aset = set()
print(type(aset))
print(aset)
aset.add(1001)  # adding an item to set
aset.add('Ramesh')
aset.add('Pune')
aset.add(True)
print(aset)

# Size of set
length = len(aset)
print(length)

# print(aset[0]) # error, indexing is not allowed (TypeError: 'set' object is not subscriptable)

for item in aset:
    print(item)


# Mutability
# add => adds an item to the set
# remove => removes an item from set if it is present, else it will throw an error
# discard => removes an item from set if it is present, No error if item is not present
# update => update the set with given items. It takes an iterable i.e, string, list, tuple, set, dictionary as a value

# add
aset = {1001, 'Ramesh', 'Pune', True, 'Pune'} # Duplicate entry for 'Pune', only first entry will be considered
print("Original set : ", aset)
aset.add(50000)    # adding an item
print("Added set : ", aset)

# remove/discard
aset.remove('Pune') # removing an item from set
print("Removed set : ", aset)
#aset.remove('Pune') # Error, removing an item which is already removed
aset.discard('Pune') # No error if item is not present
print("Discarded set :", aset)

# update

aset.update(['Pune'])
print("Updated set with an item:", aset)

aset.update((10.5,))
print("Updated set with tuple:", aset)

aset.update('TEST')
print("Updated set with an string:", aset)


# pop
print(aset)
return_value = aset.pop()
print("Return value : ", return_value)

aset.clear()

print(aset)

del aset

# print(aset) # Error



