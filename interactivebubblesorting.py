myList = []
swapped = True
num = int(input("How many elements do you want to sort: "))

for i in range(num):
    val = int(input("Enter a list element: "))
    myList.append(val)

while swapped:
    swapped = False
    for i in range(len(myList) - 1):
        if myList[i] > myList[i + 1]:
            swapped = True
            myList[i], myList[i + 1] = myList[i + 1], myList[i]

print("\nSorted:")
print(myList)
