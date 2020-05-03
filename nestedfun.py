
def fun(a,b):
    if a > b:
        return a
    return b


num1 = int(input("Enter the num1:-"))
num2 = int(input("\nEnter the num2:-"))
num3 = int(input("\nEnter the num3:-"))

# nested function
def fun1(a,b,c):
    bigger = fun(a,b)
    return fun(bigger,c)
print(f"Greater number:-{fun1(num1,num2,num3)}")


