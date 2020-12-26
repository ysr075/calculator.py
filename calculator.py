import sys
print("\nWelcome to my calculator project on python\n\nprogrammed by @ysr075 on GitHub");
while(True):
    def add(x, y):
        return x + y
    
    def substract(x, y):
        return x - y
    
    def multiply(x, y):
        return x * y
    
    def divide(x, y):
        return x / y

    choose = input("\n1.add / 2.substract / 3.multiply / 4.divide: ")
    if choose == '1':
        num1 = float(input("\nnum1: "))
        num2 = float(input("num2: "))
        total = num1 + num2
        print("\nresult is ", total)
    elif choose == '2':
        num1 = float(input("\nnum1: "))
        num2 = float(input("num2: "))
        total = num1 - num2
        print("\nresult is ", total)
    elif choose == '3':
        num1 = float(input("\nnum1: "))
        num2 = float(input("num2: "))
        total = num1 * num2
        print("\nresult is ", total)
    elif choose == '4':
        num1 = float(input("\nnum1: "))
        num2 = float(input("num2: "))
        total = num1 / num2
        print("\nresult is ", total)
    else:
        sys.exit()
