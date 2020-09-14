myList = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

newList = myList[1:9]
#
# put your code here
#

for i in myList:
    if i in newList:
        del myList[i]

 
 
print("The list with unique elements only:")
print(myList)

