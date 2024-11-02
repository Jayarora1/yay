def fact(n):
    p = "doesnt work for negetive numbers"
    if n==1 or n==0:
        return 1
    elif n<0:
        return p
    else:
      return n*fact(n-1)
print(fact(5))
