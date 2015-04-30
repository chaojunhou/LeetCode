import random
class Solution:
    import random
    def largestNumber(self, num):
        length=len(num)
        for i in range(1,length):
            tmp=num[i]
            j=i-1
            while j>=0 and int(str(tmp)+str(num[j]))>int(str(num[j])+str(tmp)):
                              
                num[j+1]=num[j]
                j-=1
            num[j+1]=tmp
        st=''.join(str(element) for element in num)
        if st[0]=='0':
            return '0'
        return st
    def largestNumber_1(self,num):
        def quickSort(num):
            if len(num)<2:
                return num
            pivot=num[0]
            small=[elem for elem in num[1:] if int(str(elem)+str(pivot))>int(str(pivot)+str(elem))]
            medium=[pivot]
            large=[elem for elem in num[1:] if int(str(elem)+str(pivot))<=int(str(pivot)+str(elem))]
            return quickSort(small)+medium+quickSort(large)
        num=quickSort(num)
        st=''.join(str(element) for element in num)
        if st[0]=='0':
            return '0'
        return st
    def largestNumber_2(self,num):
        def merge_sort(num):
            if len(num)<2:
                return num
            def merge(left,right):
                merged=[]
                while left and right:
                    merged.append(left.pop(0) if int(str(left[0])+str(right[0]))>=int(str(right[0])+str(left[0])) else right.pop(0))
                while left:
                    merged.append(left.pop(0))
                while right:
                    merged.append(right.pop(0))
                return merged
            middle=len(num)/2
            left=merge_sort(num[:middle])
            right=merge_sort(num[middle:])
            return merge(left,right)
        num=merge_sort(num)
        st=''.join(str(element) for element in num)
        if st[0]=='0':
            return '0'
        return st
            
        


if __name__=='__main__':
    sol=Solution()
    num=[1]
    print sol.largestNumber_2(num)
