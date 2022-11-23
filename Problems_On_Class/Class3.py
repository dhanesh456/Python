# Write a program which contains one class named as Arithmetic.
# Arithmetic class contains three instance variables as Valuel, Value2.
# Inside init method initialise all instance variables to 0.
# There are three instance methods inside class as Accept(), Addition(), Subtraction (),
# Multiplication(), Division().
# Accept method will accept value of Value1 and Value2 from user.
# Addition() method will perform addition of Value1 , Value and return result.
# Subtraction() method will perform subtraction of Value1 ,Value and return result.
# Multiplication() method will perform multiplication of Valuel ,Value2 and return result.
# Division() method will perform division of Valuel ,Value and return result.
# After designing the above class call all instance methods by creating multiple objects.



class Arithmetic:

    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0

    def Accept(self):
        print("Enter the first value")
        self.Value1 = int(input())

        print("Enter the second value")
        self.Value2 = int(input()) 

        return self.Value1,self.Value2

    def Addition(self):
        self.Ans1 = self.Value1 + self.Value2
        return self.Ans1

    def Substraction(self):
        self.Ans2 = self.Value1 + self.Value2
        return self.Ans2

    def Multiplication(self):
        self.Ans3 = self.Value1 * self.Value2
        return self.Ans3

    def Division(self):
        self.Ans4 = self.Value1 / self.Value2
        return self.Ans4

    def Display(self):
        print("Addition of Value1 and Value2 = ",self.Ans1)
        print("Substraction of Value1 and Value2 = ",self.Ans2)
        print("Multiplication of Value1 and Value2 = ",self.Ans3)
        print("Division of Value1 and Value2 = ",self.Ans4)    



def main():

    obj = Arithmetic()
    obj.Accept()
    obj.Addition()
    obj.Substraction()
    obj.Multiplication()
    obj.Division()
    obj.Display()




if __name__ =="__main__":
    main()    


