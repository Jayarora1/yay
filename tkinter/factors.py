def Factor(number):
    for i in range(1,number + 1):
        if number % i == 0:
            print(i)
number = int(input("Please enter a number"))
Factor(number)        