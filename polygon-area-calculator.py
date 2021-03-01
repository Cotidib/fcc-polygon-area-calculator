from math import sqrt

class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        area = self.width * self.height
        return area      

    def get_perimeter(self):
        peri = (self.width * 2) + (self.height * 2)
        return peri

    def get_diagonal(self):
        diag = sqrt( self.width**2 + self.height**2 )
        return diag
  
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        else:            
            picture = ""
            for j in range(0, self.height):
                for i in range (0, self.width):
                    picture += "*"
                picture += "\n"
            return picture
        

    def get_amount_inside(self, othershape):
        actual_area = self.get_area()
        other_area = othershape.width * othershape.height
        amount_inside = actual_area/other_area
        max_amount = int(amount_inside)
        return max_amount

    def __str__(self):
        stringform = f"Rectangle(width={self.width}, height={self.height})"
        return stringform


class Square(Rectangle):

    def __init__(self, side):
        self.width = side
        self.height = side

    def set_side(self, newside):
        self.width = newside
        self.height = newside

    def __str__(self):
        stringform = f"Square(side={self.width})"
        return stringform
                

        
#TEST
rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))

