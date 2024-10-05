writer = open('updatedfile.txt','w')
reader = open('repeatedfile.txt','r')
emptyset = set()
for i in reader:
    if i not in emptyset:
        emptyset.add(i)
        writer.write(i)
writer.close()
reader.close()