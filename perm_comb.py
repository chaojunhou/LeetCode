def perm(items,n=None):
    if n is None:
        n=len(items)
    for i in range(len(items)):
        v=items[i:i+1]
        if n==1:
            yield v
        else:
            rest=items[:i]+items[i+1:]
            for p in perm(rest,n-1):
                yield v+p

def comb(items,n=None):
    if n is None:
        n=len(items)
    for i in range(len(items)):
        v=items[i:i+1]
        if n==1:
            yield v
        else:
            rest=items[i+1:]
            for c in comb(rest,n-1):
                yield v+c
if __name__=='__main__':
    Perm=perm('abc')
    for b in Perm:
        print b
        break
    print '_'*20
    for b in Perm:
        print b
    Comb=comb('abcd')
    print '-'*20
    for c in Comb:
        print c
