# Task : Get a number from user and return the remainder ( modulo by any number ). Print the remainder
# parameter + return value


# Function Definition
def getModulo(number, modulobase):
    rem = number % modulobase
    return rem



# Task : Accept two numbers from user and print the sum
def calculateSum(numA, numB):
    return numA + numB



# Task : Get salary of two person's from user
# Compare the salary and display the message accordingly.

def salaryComparator(salA, salB):
    if salA > salB:
        print("Salary of A is more than B")
    elif salB > salA:
        print("Salary of B is more than A")
    else:
        print("Salaries are equal")



# Task : Compute the sum of numbers in the list
# [1, 2, 3, 4, 5, 6]

def computeSum(numlist):
    sum = 0
    for x in numlist:
        sum = sum + x

    return sum





if __name__ == '__main__':
    num = int(input("Please enter a number : "))
    mb = int(input("Please enter a modulo base : "))

    # Function Call with two parameters
    remainder = getModulo(num, mb)
    print("Remainder :", remainder)


    # Function Call - calculateSum

    sum = calculateSum(10, 20)
    print("Sum :", sum)


    # salaryComparator
    salA = int(input("Please enter the salary of A : "))
    salB = int(input("Please enter the salary of B : "))
    salaryComparator(salA, salB)

    # computeSum
    numList = [1, 2, 3, 4, 5, 6]
    sum = computeSum(numList)
    print("List Sum : ", sum)