file = open('codingal.txt','r')
print("/n The characters/n")
print(file.read(99999))
file.close()

file = open('codingal.txt','a')
file.write("Hello my name is penguin and i am 1 years old")
file.close()