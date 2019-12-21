n = int(input("Please Enter the Number Of Applications Currently Opened On the System : "))
k = int(input("Please Enter the Number Of Times User Presses Tab Key Holding the ALT Key : "))
list1 = []
n = int(input("Enter the Number Of Terms In The List : "))
for i in range(0, n):
    print("Enter number at location", i, ":")
    item = int(input())
    list1.append(item)
numberOfElements = int(len(list1))
positionOfKInList = list1.index(k)
numberAtKInList = list1[positionOfKInList]
list1.pop(positionOfKInList)
list1.insert(0, k)
print(list1)