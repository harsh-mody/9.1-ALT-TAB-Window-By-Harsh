n = int(input("Please Enter the Number Of Applications Currently Opened On the System : "))
k = int(input("Please Enter the Number Of Times User Presses Tab Key Holding the ALT Key : "))
inputList = list(map(int, input('Please Enter The List To Be Entered Separated By Space : ').split()))
if len(inputList) == n:
    for i in range(0, len(inputList)):
        if inputList[i] % k <= 1:
            if inputList.__contains__(k):
                index = inputList.index(k)
                del inputList[index]
                inputList.insert(0, k)
    if k > len(inputList):
        k = k - len(inputList) - 1
        for i in range(0, len(inputList)):
            if inputList[i] % k <= 1:
                if inputList.__contains__(k):
                    index = inputList.index(k)
                    del inputList[index]
                    inputList.insert(0, k)
print(inputList)
