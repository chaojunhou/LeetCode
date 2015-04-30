strmap1=''
stmap='http://www.pythonchallenge.com/pc/def/map.html'
for x in stmap:
	if x.islower():
		number=ord(x)+2
		if(number>122):
			number=number-122+96
		strmap1+=chr(number)
	else:
		strmap1+=x

print strmap1
