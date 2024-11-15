numberSmallest = int(input("please enter a number"))
numberLargest = int(input("please enter a number"))
while numberSmallest:
    numberStore = numberSmallest
    numberSmallest = numberLargest % numberSmallest
    numberLargest = numberStore
print(numberLargest)