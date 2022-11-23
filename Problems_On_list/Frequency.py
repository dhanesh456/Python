#A program which accepts N number from user and store it into List.
#And another number from user and retrun frequency of that number from the list



def frequency(list1,num):

    list2 = list()
    cnt = 0
    for value in list1:
        if(value == num):
            cnt+=1           
    return cnt

def main():

    lst = list()

    print("Enter number of elements you want to store in the list :")
    NOE = int(input())
    print("Enter values of list :")
    for i in range(0,NOE):
        input1 = int(input())
        lst.append(input1)
    print("Values of list :  ",lst)

    print("Enter a number from list to find its frequency : ")

    num = int(input())

    print("Frequency count of no is:",frequency(lst,num))

    













if __name__ == "__main__":
    main()    