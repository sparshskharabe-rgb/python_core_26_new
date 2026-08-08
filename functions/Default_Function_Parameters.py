# Function Definition
# two parameters - name, event_name
# name => non-default parameter, event_name => default parameter
# Important Note :
#     default parameters must come after non-default parameters

def greetGuests(name, event_name = 'FashionHub'):
    print("Hello {}, welcome to the {}.".format(name, event_name))


# Function Call
greetGuests('Ramesh', 'TechFest')

greetGuests('Ram')

greetGuests('Mohan', 'AgriTech')

#greetGuests()