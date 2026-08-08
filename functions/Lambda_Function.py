# Function
# def, name of function, arguments, body(logic)

def squared(num): return num ** 2

print(squared(10)) # Function call


# Lambda Function : Anonymous Function, having no names
# define the function : use lambda keyword

sq = lambda num : num ** 2  # lambda expression, but not the ideal way to use lambda(we shouldn't assigned it a variable)
print(sq(10))



# Gnereral Approach through 'map' function

# Operation
def squared(num): return num ** 2

# Function Call
x = [1,2,3,4,5]

output = list(map(squared, x)) # map (operation, collection)
print(output)


# Function Call : lambda
x = [1,2,3,4,5]
output = list(map(lambda num: num**2, x)) # map (operation, collection)
print(output)


# Using lambda with 'filter' to remove the odd numbers

numlist = [1, 2, 3, 4, 5, 6, 7, 8]

# General Approach
filteredList = []
for x in numlist:
    if x % 2 ==0 :
        print(filteredList.append(x))
print(filteredList)

# lambda approach - filter
output = list(filter(lambda num : num%2==0, numlist))
print(output)