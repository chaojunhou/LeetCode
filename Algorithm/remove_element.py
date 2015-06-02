import random
class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        if not A :
            return 0
        slow=0
        for fast in range(len(A)):
            if A[fast]==elem:
                continue
            else:
                A[slow]=A[fast]
                slow+=1
        print A
        return slow
    def removeElement1(self, A, elem):
        count = 0
        lst = []
        for val in A:
            if val != elem:
                count += 1
                lst.append(val)
        A = lst
        print A
        return count
                

if __name__ == '__main__':
    sol = Solution()
    A = [random.randint(1,10) for i in range(12)]
    element = random.randint(1,10)
    print A, element
    #print sol.removeElement(A,element)
    
    print sol.removeElement1(A,element)
