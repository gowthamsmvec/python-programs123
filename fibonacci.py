a = int(input("How many terms: "))
i,j = 0,1
count = 0
if a<= 0:
   print("Please enter a positive integer")
elif a== 1:
   print("Fibonacci sequence upto",a,":")
   print(i)
else:
   print("Fibonacci sequence:")
   while count < a:
       print(i)
       k = i + j
       i = j
       j = k
       count += 1
