#Find maximum number of three number
num1 = int(input("Enter the number 1:-"))
num2 = int(input("Enter the number 2:-"))
num3 = int(input("Enter the number 3:-"))
def MaxOfThree(num1,num2,num3):
	if num1 >= num2 and num1 >= num3:
		print(num1,"is Maximum")
	elif num2 >= num1 and num2 >= num3:
		print(num2,"is Maximum")
	else:
		print(num3,"is Maximum")
MaxOfThree(num1,num2,num3)
		
