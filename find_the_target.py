def find(A):
    target=A[0]:
        for i in range(1,len(A)):
            if A[i]<target:
                target=A[i]
import random
A=[random.randint(1,100) for i in range(10)]
find(A)
