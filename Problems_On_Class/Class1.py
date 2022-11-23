# Program which contains one class named as Demo
# Demo class contains two instance variable as no1, no2
# That class contains one class variable as value
# There are tow instance variable as class fun and gun which displays values of instance variable


class Demo:
    Value = 0
    def __init__(self,A,B):
        
        self.no1 = A
        self.no2 = B
        

    def fun(self):
        
        print("value of fun no1 = ",self.no1)
        print("value of fun no2 = ",self.no2)

    def gun(self):
        
        print("value of gun no1 = ",self.no1)
        print("value of gun no2 = ",self.no2)    


def main():

    Obj1 = Demo(11,21)
    Obj2 = Demo(51,101)

    Obj1.fun()
    Obj2.fun()
    Obj1.gun()
    Obj2.gun()




if __name__ == "__main__":
    main()    