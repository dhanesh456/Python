# Program which contains one class named as Circle.
# Circle class contains three instance variables as Radius ,Area, Circumference
# That class contains one class variable as PI which is initialise to 3.14
# Inside init method initialise all instance variables to 0.0
# There are three instance methods inside class as Accept(), CalculateArea(), CalculateCircumference(), Display.
# Accept method will accept value of Radius from user.
# CalculateArea() method will calculate area of circle and store it into instance variable Area.
# CalculateCircumference() method will calculate circumference of circle and store it into instance variable Circumference.
# And Display() method will display value of all the instance variables as Radius, Area, Circumference.
# After designing the above class call all instance methods by creating multiple objects.


class Circle:
    
    PI = 3.14
    def __init__(self):
        
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0

    def Accept(self):
        print("Enter Radius of a circle")
        self.Radius = float(input())
        return self.Radius

    def CalculateArea(self):
        self.Area = self.PI * self.Radius * self.Radius
        return self.Area 

    def CalculateCircumference(self):
        self.Cricumference = 2 * self.PI * self.Radius            
        return self.Cricumference

    def Display(self):
        print("Radius of circle = ",self.Radius)
        print("Area of circle = ",self.Area)
        print("Circumfarace of circle = ",self.Cricumference)

def main():

    obj = Circle()

    obj.Accept()
    obj.CalculateArea()
    obj.CalculateCircumference()
    obj.Display()

if __name__ =="__main__":
    main()    