file1 = open('codingal.txt','r')
file2 = open('codingalempty.txt','w')
for i in file1.readlines():
    if not (i.startswith("codingal")):
        print(i)
        file2.write(i)
file1.close()
file2.close()