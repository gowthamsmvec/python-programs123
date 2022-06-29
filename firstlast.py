NumList = []
 

Number = int(input("How many elements in list :- "))
     
for i in range(1, Number + 1):
    value = int(input("Please enter the Value of %d Element :- " %i))
    NumList.append(value)
 

print("\nList before swapping of elements :-\n",NumList)

temp=NumList[0]
NumList[0]=NumList[Number-1]
NumList[Number-1]=temp
   
print("List after swapping of elements :-\n",NumList) 
