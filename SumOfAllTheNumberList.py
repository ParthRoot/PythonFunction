#Sum Of All The Number Of List

# function to calculate the sum of all the number in list
def soatnl(lst):
	sum = 0
	mul = 1
	sub = 0
	l = len(lst)
	for i in range(l):
		sum = sum + lst[i]
		mul = mul * lst[i]
		sub = lst[i] - sub
	print("Sum:-",sum,"\nMul:-",mul,"\nSub:-",sub)
	
#Enter the in list by user
def inuser(n):
	for i in range(5):
		a = int(input("Enter the Number:-"))
		n.append(a)
	print("n =",n)

#define empty list
n = []
#call the function
inuser(n)
soatnl(n)

