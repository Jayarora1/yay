number = int(input("Please enter a number: "))
digits = len(str(number))
temp = number
resultnumber = 0
while temp > 0:
    digit = temp % 10
    resultnumber += digit**digits
    temp//=10
if number == resultnumber:
    print("it is an armstrong number")
else:
    print("it is not an armstrong number")