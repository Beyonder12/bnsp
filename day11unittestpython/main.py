class Rectangle:

    # attribute and constructor
    def __init__(self, width = 0, height = 0) -> None:
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height
    
    def set_width(self, width):
        self.width = width
    
    def get_width(self):
        print(self.width)

    def set_height(self, height):
        self.height = height
    
    def get_height(self):
        print(self.height)
    

# rectangle = Rectangle()
# rectangle.get_height()

def test_normal_case():
    rectangle = Rectangle(3, 5)
    assert not rectangle.get_area() == 16, "Incorrect function"

def test_normal_case1():
    rectangle = Rectangle(3, 5)
    assert rectangle.get_height() == print(3), "Incorrect function"
