# create an empty dictionary

adict = {}
print(type(adict))

adict = dict()
print(type(adict))

equipment = {
    "brand" : "Tata",  # key : value
    "year" : 2025,      # key : value
    "model": "X-553535" # key : value
}

print(equipment)
print(type(equipment))

print(len(equipment)) # length of dictionary

# Iterate on dictionary
# 1st approach
for key in equipment:
    print(key, equipment[key]) # key : key, value: equipment[key]


# 2nd approach
equipKeys = equipment.keys()
print(equipKeys) # dict_keys(['brand', 'year', 'model'])
print(type(equipKeys)) # class 'dict_keys'

for key in equipKeys:
    print("Key :", key)
    print("Value : ", equipment[key])
    print("{key} => {value}".format(key = key, value = equipment[key]))
    print("{} => {}".format(key, equipment[key]))


# 3rd approach

for key, value in equipment.items():
    print("{} => {}".format(key, value))


# 4th approach

equipKeys = equipment.keys()
equipValues = equipment.values()
print(equipKeys)
print(equipValues)

# equipKeys[0], equipValues[0] # TypeError: 'dict_keys' object is not subscriptable

keyList = list(equipKeys) # convert to list to use indexing
valuesList = list(equipValues) # convert to list to use indexing

for i in range(len(keyList)):
    print("{} => {}".format(keyList[i], valuesList[i]))



# update the dictionary

employeeDict = {
    "id" : 1001,
    "name" : "Ramesh",
    "address" : "Pune",
    "dept" : "IT",
    "isCertified" : True
}

print(employeeDict)

employeeDict['phone'] = 9898989898 # 'phone' key is not present, so adding a new key value pair

print(employeeDict)

employeeDict['phone'] = 9000000000 # alraedy present, so upadting the value of 'phone'

print(employeeDict)

employeeDict.update({'hobby' : "Football"})  # adding ne w key value pair
print(employeeDict)

employeeDict.update({'gender' : 'M'}) # adding ne w key value pair
print(employeeDict)

# check the presence of a key and then add if not available

if 'exp' in employeeDict:
    print("Key '{}' is already present with value '{}'. So, skipping the update..".format('exp',employeeDict['exp']))
else:
    print("Key not present. Adding new key: '{}' and value: '{}' ".format('exp', 10))
    employeeDict.update({'exp': 10})

print(employeeDict)


# Remove a key from dictionary

removedData = employeeDict.pop('gender') # pop(key)
print('removed Data : ', removedData)
print(employeeDict)
removedData = employeeDict.pop('gender', -1) # pop(key, default)
print('removed Data : ', removedData)


del employeeDict