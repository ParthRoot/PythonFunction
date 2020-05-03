#multiple argument
def fun(fname,lname):
	print("Fname:-",fname,"Lname:-",lname)
fun("Parth","Patel")

#Arbitray Argument (*)

def arb(*kind):
	print(kind[1])
arb("Parth","lopy")

#KeyWord Argument

def ka(name1,name2,name3):
	print("Name1-:",name1,"Name-:2",name2,"name3-:",name3)
ka(name1="Parth",name2="Lopy",name3="Flopy")

#Arbitray Keyword Argument (**)
def aka(**name):
	for x in (name):
		print(name)
	print(name["s2"])
aka(s1="Parth",s2="Nobita")