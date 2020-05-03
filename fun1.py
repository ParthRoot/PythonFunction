def fun(a,b):
    if a > b:
        print(f"Greater number is -:{a} ")
    else:
        print(f"greater number is -:{b}")
num1 = int(input("Enter the num1:-"))
num2 = int(input("\nEnter the num2:-"))
fun(num1,num2)

def fun1(a,b):
    if a > b:
        return a
    return b 
       
num3 = int(input("Enter the num1:-"))
num4 = int(input("\nEnter the num2:-"))
gnum = fun1(num3,num4)
print("greater number:-"+str(gnum))




