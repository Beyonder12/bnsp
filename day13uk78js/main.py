

class Car:

    # Attribute
    name = 'Unknown'
    wheel = 2
    etc = 'Other'

    # Constructor
    def __init__(self, nameParam = name, wheelParam = wheel) -> None:
        self.nameParam = nameParam
        self.wheel = wheelParam
    
    # Method
    def move(self):
        print('Moving...')

# Instantiate!

bmw = Car()
bmw.move()
print(bmw.name)
print(bmw.nameParam)
print(bmw.etc)
        