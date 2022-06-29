a=int(input("Enter the starting value= "))
b=int(input("Enter the ending value= "))
for i in range(a,b+1):
    if i>1:
        for j in range(2,i):
            if (i%j)==0:
                break
        else:
            print(i)
