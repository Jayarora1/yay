with open('codingal.txt','w') as file:
    file.write("Hello my name is Penguin i am 1 years old")
file.close()

with open('codingal.txt','r') as file:
    data = file.readlines()
    for line in data:
        word = line.split()
        print(word)
file.close()