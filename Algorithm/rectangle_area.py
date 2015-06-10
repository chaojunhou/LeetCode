class Solution:
    # @param {integer} A
    # @param {integer} B
    # @param {integer} C
    # @param {integer} D
    # @param {integer} E
    # @param {integer} F
    # @param {integer} G
    # @param {integer} H
    # @return {integer}
    def computeArea(self, A, B, C, D, E, F, G, H):
        if C < E or G < A or D < F or H < B:
            return (C-A)*(D-B) + (H-F)*(G-E)
        lst = []
        lst.append(A)
        lst.append(C)
        lst.append(E)
        lst.append(G)
        lst.sort()
        print lst
        w = lst[2]-lst[1]
        lst = []
        print lst
        lst.append(B)
        lst.append(D)
        lst.append(F)
        lst.append(H)
        lst.sort()
        h = lst[2] - lst[1]
        return (C-A)*(D-B) + (H-F)*(G-E) - w*h
    def computeArea1(self, A, B, C,D,E, F, G, H):
        res = (C-A)*(D-B) + (H-F)*(G-E)
        return  res   if C < E or G < A or D < F or H < B else res-(min(C,G)-max(A,E))*(min(D,H)-max(B,F))
        #return (C-A)*(D-B) + (H-F)*(G-E) if C < E or G < A or D < F or H < B else (C-A)*(D-B) + (H-F)*(G-E) - (min(C,G)-max(A,E))*(min(D,H)-max(B,F))


if __name__ == '__main__':
    sol = Solution()
    lst = []
    A = -3
    B = 0
    C = 3
    D = 4
    E = 0
    F = -1
    G = 9
    H = 2
    print sol.computeArea(A,B,C,D,E,F,G,H)
    print sol.computeArea1(A,B,C,D,E,F,G,H)
    
    
