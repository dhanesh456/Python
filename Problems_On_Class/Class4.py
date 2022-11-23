# Write a program which contains one class named as BookStore. 
# BookStore class contains two instance variables as Name ,Author. 
# That class contains one class variable as NoOfBooks which is initialise to 0. 
# There is one instance methods of class as  
# Display which displays name, Author and number of books.
# Initialise instance variable in init method by accepting 
# the values from user as name and author.
# Inside init method increment value of NoOfBooks by one.


class BookStore:

    NoofBooks= 0
    
    def __init__(self ,A ,B):
        self.Name = A
        self.Author = B
        

    def Display(self):
        print(self.Name,"by",self.Author,".No of Books : ",self.NoofBooks+1)


def main():

    Obj = BookStore("Linux System programming","Robert Love")
    Obj.Display()

    obj2 = BookStore("C Programming","Dennis Ritchie")
    obj2.Display()


if __name__ == "__main__":
    main()    
        