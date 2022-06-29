NumList = []
 

Number = int(input("How many elements in list :- "))
     
for i in range(1, Number + 1):
    value = int(input("Please enter the Value of %d Element :- " %i))
    NumList.append(value)
 
print("\nList before swapping of elements :-\n",NumList)
 
position1 = int(input("Enter the position of element, which you want to swap :- "))
position2 = int(input("Enter the position of element, which you want to swap :- "))
 

def swapPositions(list, pos1, pos2): 
       
    list[pos1], list[pos2] = list[pos2], list[pos1] 
    return list
   
print("List after swapping of elements :-\n",swapPositions(NumList, position1-1, position2-1)) 
