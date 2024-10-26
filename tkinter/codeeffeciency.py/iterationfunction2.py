def function(n):
    iteration = 0 
    print("The user selected ",n)
    iteration +=1
    print("The number of iterations are",iteration,"/n")
function(10)
function(20)

def function2(n):
    iteration = 0
    for i in range(1,n+1):
        iteration += 1
    print("when user puts",n,"The amount of iterations =",iteration)
function2(10)
function2(20)

def function3(n):
    iteration = 0
    for i in range(1,n*n):  
        for j in range(1,iteration):
            print("*",end="")
            iteration += 1
            print("when user puts",n,"The amount of iterations =",iteration)
function3(10)
function3(20)