
def list_length(list):
    counter=0
    for i in list:
        counter=counter+1   
    return counter

 
li = [ 1, 4, 5, 7, 8 ]
  

print ("List : ",li)
 
print ("Length of list using naive method is : ",list_length(li))
