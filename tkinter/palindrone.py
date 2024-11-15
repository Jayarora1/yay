firstDigit = input("Please enter a digit: ")
secondDigit = input("Please enter a digit: ")
thirdDigit = input("Please enter a digit: ")

original = firstDigit + secondDigit + thirdDigit
reversed = thirdDigit + secondDigit + firstDigit

if original == reversed:
    print("this is a palindrone")
else:
    print("this is not a palindrone")
