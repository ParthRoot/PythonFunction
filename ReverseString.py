#Reverse String

def rstr(str):
	str1 = ""
	l = len(str)
	while l > 0:
		str1 += str[l - 1]
		l = l - 1
	print(str1)
	
rstr("Parth Bharat Bhai Patel")
		