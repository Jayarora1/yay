def function3(n):
    iteration = 0
    for i in range(0,n):  
        for j in range(0,n):
            print("*",end=" ")
            iteration += 1
        print("")
    print("/nwhen user puts",n,"The amount of iterations =",iteration)
function3(5)
function3(10)