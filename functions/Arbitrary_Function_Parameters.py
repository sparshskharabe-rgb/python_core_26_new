
def greetGuests(event_name, *name): # 0 or any number of arguments
    print(type(name)) # tuple
    print(name)

    for nm in name:
        print("Hello {}, welcome to the {}.".format(nm, event_name))



greetGuests("TechFest", "Ramesh")

greetGuests("TechFest", "Ramesh", "Mohan", "Raj", "Amit")
