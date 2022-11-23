def Add(Value1 , value2):
    ans = Value1 + value2

    return ans

def main():
    print("Enter the first value :")
    No1 = float(input())
    print("Enter the secont value :")
    No2 = float(input())

    Sum = Add(No1 , No2)

    print("Output : ",Sum)


if __name__ == "__main__":
    main()
