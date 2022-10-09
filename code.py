from random import randrange
from .v import v_weights

#T = input("input [t1,t2,t3,t4,t5,t6,t7,t8]")


T = [3 ,6 ,4 ,4 , 5, 5, 1, 1]

v_flag = []

A = []
threshold = 4


for i in range(100):
    A.append([randrange(1,4),
            randrange(1,7),
            randrange(1,5),
            randrange(1,5),
            randrange(1,6),
            randrange(1,6),
            randrange(1,6),
            randrange(1,6)])


counter  = 0
for i in range(len(A)):
        count = 0
        for j in range(len(A[i])):
                if A[i][j] == T[j]:
                        count += 1

        if count >= threshold:
                v_flag.append(1)

        else:
                v_flag.append(0)

