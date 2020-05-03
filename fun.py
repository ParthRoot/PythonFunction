#Create A function

def fun():
	print("Hello")
fun()

#Take argument to function
def fun1(name):
	print("Name:-",name)
fun1("Parth")

tup = ("Parth","Jaimin","Varshil","Tirth")
c = len(tup)
for i in range(c):
	fun1(tup[i])

A = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
a = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
for i in range(len(A) and len(a)):
	print(A[i]+ " =",a[i],end=",")

print("\n")	
def add(a,b):
	return a + b

print("Addition:-",add(10,20))
	