#Count the uppercase latter and lower case latter
def str_test(s):
	d = {"Upper_Case":0,"Lower_Case":0}
	for i in s:
		if i.isupper():
			d["Upper_Case"] += 1
		elif i.islower():
			d["Lower_Case"] += 1
		else:
			pass
	print("Original String:", s)
	print("Upper case later is:-", d["Upper_Case"])
	print("Lower case later is:-", d["Lower_Case"])
str_test("Parth BharatBhai Patel")














