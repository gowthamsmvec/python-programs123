myStr =  input('Enter the string : ')
i = int(input('Enter the index of character to be removed : '))
resStr = ""
for index in range(len(myStr)):
	if index != i:
		resStr = resStr + myStr[index]
print ("Entered string : " + myStr)
print ("String formed by removing i'th character : " + resStr)
