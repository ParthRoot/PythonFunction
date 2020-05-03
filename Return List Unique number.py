def fun(s):
	l = []
	for i in s:
		if i not in l:
			l.append(i)
	return l 
print(fun([1,2,3,4,3,4,5,2,5,2,53,2,4,5,2,4,2,1,4]))