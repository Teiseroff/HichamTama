import numpy as np

f = open('Cards/1.txt')
lines = f.readlines()

print(lines)

M = np.zeros((3,3))

for i in range(0,len(lines)) :
    l = lines[i].replace("\n","")
    print(l)
    for j in range(0,len(l)) :
        c = l[j]
        if(c=="1") :
            M[i][j] = 1
    
print(M)


