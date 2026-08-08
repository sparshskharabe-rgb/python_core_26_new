# ISO
# ASCII
# UNICODE

name = "Raj"
print(type(name))
print(name)

name = 'Raj'
print(type(name))
print(name)

name = "Hello Everyone !"
print(type(name))
print(name)

name = ("Hello "
        "Everyone !")
print(type(name))
print(name)

name = "Hello " \
        "Everyone !" \
        "How are you ?"
print(type(name))
print(name)

name = """Hello  
        Everyone !
        How are you ?"""
print(type(name))
print(name)

name = '''Hello  
        Everyone !
        How are you ?'''
print(type(name))
print(name)


program = '''
if x > 0:
    print("Number is +ve")
else:
    if x < 0:
        print("Number is -ve")
    else:
        print("Zero value") '''

print(program)



name = "Hello !"
print(type(name))
print(name)

# Accessing the charcters, 0-indexed based
print(name[0]) # First character, Time complexity : O(1)
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])
print(name[6]) # Last character

# Length of the string
length = len(name)
print("Length of the string is ", length)

lastIndex = length - 1
print("Last Index Position ", lastIndex)

# Access last character
print(name[lastIndex]) # +ve indexing

# -ve indexing
print(name[-1]) # -ve indexing, last character
lastNegativeIndex = -1 * length
print("First Character ", name[lastNegativeIndex])



# String Slicing

greet = "Hello Ramesh !"
N = len(greet)
print("Length of the string ", N)

print("First Character ", greet[0])
print("Last Character ", greet[N-1])
print("Last Character ", greet[-1])

# Slicing Approach 1 : greet[start:stop:step]
# start => starting index position, default : 0
# stop => end index position, excluded from o/p, default : entire length
# step => increment, default 1

print(greet[0:3]) # start: 0, stop : 3, step: 1 (default as no value is provided)
print(greet[0:3:1]) # start: 0, stop: 3, step: 1
print(greet[0:3:2]) # start: 0, stop: 3, step: 2

print(greet[3:10]) # start:3, stop: 10, step: 1(default)
print(greet[:10]) # start:0(default), stop: 10, step: 1 (default)
print(greet[:10:]) # start:0(default), stop: 10, step: 1 (default)
print(greet[::]) # start:0, stop: length of string, step: 1
print(greet[::2]) # start:0, stop: length of string, step: 2

print(greet[-14:-8]) # start: -14, stop: -8, step: 1
print(greet[-4:]) # start: -4, stop: length, step: 1
print(greet[:-4]) # start: 0, stop: -4, step: 1

print(greet[:]) #

print(greet[-8:-14])


#print(greet[-15]) #IndexError: string index out of range
#print(greet[15])  #IndexError: string index out of range



# Inbuilt Functions

greet = "9wElcome to the event !"
print(greet)

# len : no of characters in string
nc = len(greet)
print("Length : ", nc)

# case operations

lw = greet.lower()
up = greet.upper()
cp = greet.capitalize()
tl = greet.title()

print("Original String :", greet )
print("Lower String :", lw )
print("Upper String :", up )
print("Capital String :", cp )
print("Title String :", tl )


# Split : breaks the string into multiple parts, based on some delimiter (separator)
greet = "Welcome to the event !"
print(greet)

splitGreet = greet.split(" ") # string => list, ['Welcome', 'to', 'the', 'event', '!']
print(splitGreet)
print(type(splitGreet))

print(splitGreet[0])
print(splitGreet[1])
print(splitGreet[2])
print(splitGreet[3])
print(splitGreet[4])
# print(splitGreet[5]) # IndexError: list index out of range

empRecord = "1001|Ramesh|21-06-2026|50000|IT|Developer"
empList = empRecord.split("|")
print(empList)
print(empList[0])
print(empList[1])
print(empList[2])
print(empList[3])
print(empList[4])
print(empList[5])


# strip : removes the whitespace characters from beginning/end of a string (leading/trailing)
# lstrip : removes from left
# rstrip : removes from right

empRecord = "   1001   |   Ramesh   |   21-06-2026     |     50000|IT|Developer   "
print(empRecord)
lstripped = empRecord.lstrip()
print(lstripped)

rstripped = empRecord.rstrip()
print(rstripped)

strippedEmp = empRecord.strip()
print(strippedEmp)


empList = empRecord.split("|")
print(empList)
print(empList[0].strip())
print(empList[1].strip())
print(empList[2].strip())
print(empList[3].strip())
print(empList[4].strip())
print(empList[5].strip())


empList = [empList[0].strip(), empList[1].strip(), empList[2].strip(), empList[3].strip(), empList[4].strip(), empList[5].strip()]
print(empList)


# String replacement, replace

weather = "The weather is good today !"
print(weather)
weather = weather.replace("good", "better")
print(weather)


# String Formatters, format

name = "Tushar"
course = "Python"

print("Hello, My name is ", name, ". I have enrolled for ", course, "course.") # Not Recommended

# no of placeholders must match number of arguments in format
greet = "Hello, My name is {}. I have enrolled for {} course.".format(name, course) # {} => placeholder
print(greet)

greet = "Hello, My name is {0}. I have enrolled for {1} course.".format(name, course) # {} => placeholder
print(greet)

greet = "Hello, My name is {0}. I have enrolled for {1} course. {1} is very popular language".format(name, course) # {} => placeholder
print(greet)

greet = "{1} is a programming language. {0} enrolled for it".format(name, course) # {} => placeholder
print(greet)

greet = "Hello, My name is {nm}. I have enrolled for {cs} course.".format(nm=name, cs=course) # {} => named based placeholder
print(greet)


# More inbulits

str = "hjfhfjhjkhjkhkf"
print(str.isalpha()) # only alphabets

str = "hjfhfjhjk2hjkhkf"
print(str.isalpha()) # only alphabets

str = "hjfhfjhjkh2jk2hkf"
print(str.isalnum()) # only alphabets + numbers

str = "hjfhfjhjkh@jk2hkf"
print(str.isalnum()) # only alphabets + numbers

str = "hjfhfjhjkh"
print(str.isdigit()) # only digits

str = "123456"
print(str.isdigit()) # only digits

str = "hjfhfjhjkh"
print(str.isupper())

str = "hjfhfjhjkh"
print(str.islower())

str = "hjfhfjhjkh"
print(str.isnumeric())

str = "hjfhfjhj2345kh"
print(str.isnumeric())

str = "2345"
print(str.isnumeric())

str = "41"
print(str.isnumeric())
print(str.isdigit())

str = "4.1"  # QQ
print(str.isnumeric())
print(str.isdigit())
print(str.isdecimal())


# Search Functionality

# find() => return -1 if string is not present  else gives the starting index of the search string
# index() => error out if string is not present else gives the starting index of the search string

temp = "The temperature on 21-06-2026 is 32 degrees"
searchString = "degrees"
print(temp.find(searchString))
print(temp.index((searchString)))

searchString = "amount"
print(temp.find(searchString))  # -1 since the string is not present
# print(temp.index((searchString))) # ValueError: substring not found


# Join

fname = "Raj"
lname = "Mehra"

mylist = [fname, lname]
print(" ".join(mylist))


name = 'Ramesh'
for i in name:
   print(i)



print ("Name : ", name + "faname: ", fname + "lname: ",lname)

print ("Name : {}, faname : {}, lname : {} ".format( name, fname,lname))