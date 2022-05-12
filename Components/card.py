

import numpy as np

class Card() :

    def __init__(self,id) :

        self.id = id

        matrixFile = open('Cards/'+str(self.id)+'.txt')
        lines = matrixFile.readlines()
        M = np.zeros((5,5))
        for i in range(0,len(lines)) :
            l = lines[i].replace("\n","")
            for j in range(0,len(l)) :
                c = l[j]
                if(c=="1") :
                    M[i][j] = 1

        self.matrix = M
        

    def getId(self) :
        return self.id

    def getMatrix(self) :
        return self.matrix

    

