a=int(input("Enter the Year="))
if(a%400==0):
   print(a," is a leap year")
elif(a%100==0):
    print(a,"is a non leap year")
elif(a%4==0):
    print(a,"is a leap year")
else:
    print(a,"is a non leap year")
   
