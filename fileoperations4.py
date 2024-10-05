with open('codingal.txt','r') as fp:
    data1 = fp.read()
with open('doc.txt','r') as fp:
    data2 =fp.read()
data1 += data2
data1 += "eeeeee"
print('merging time')
with open('merged.txt','w') as fp:
    fp.write(data1)
fp.close()