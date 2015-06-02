def randomPick(k):
    import random
    n=random.randint(k,10*k)
    print n
    lst=[i+1 for i in range(k)]
    print lst
    for i in range(k+1,n):
        r=random.randint(1,i)
        if r<=k:
            lst[r-1]=i
    print lst
    print sorted(lst)
def GenKnuth(m,n):
    import random
    lst=[]
    for i in range(n):
        if random.randint(1,n-i)<=m:
            lst.append(i)
            m-=1
    print lst,len(lst)
GenKnuth(10,20)           
        
randomPick(20)
        
