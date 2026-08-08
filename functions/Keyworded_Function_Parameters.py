# Keyworded Arguments
# Same as arbitrary function arguments, but the arguments are passed as key-vale pairs

x = 0  # global variable

def getEventDetails(**kwargs):
    print(type(kwargs))
    print(kwargs)

    for key, value in kwargs.items():
        print("Booth : {}, Topic : {}".format(key, value))


getEventDetails(booth1='AI', booth2='ETL Tools', booth3='Agriculture')
