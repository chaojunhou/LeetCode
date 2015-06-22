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

            middle=len(num)/2
            left=merge_sort(num[:middle])
            right=merge_sort(num[middle:])
        
            merged=[]
            while left and right:
                merged.append(left.pop(0) if str(left[0])+str(right[0]) >= str(right[0])+str(left[0]) else right.pop(0))
            while left:
                merged.append(left.pop(0))
            while right:
                merged.append(right.pop(0))
            return merged
           
        num=merge_sort(num)
        st=''.join(str(element) for element in num)
        if st[0]=='0':
            return '0'
        return st
    def largestNumber_3(self,num):
        
        def quickSort(num, low, high):
            def partition(num, low, high):
                x = num[high]
                i = low -1
                for j in range(low, high):
                    if str(num[j]) + str(x) > str(x) + str(num[j]):
                        i += 1
                        num[i], num[j] = num[j], num[i]
                num[i+1], num[high] = num[high], num[i+1]
                return i+1                
            if low < high:
                q = partition(num, low, high)
                quickSort(num, low, q-1)
                quickSort(num, q+1, high)
        quickSort(num, 0, len(num)-1)
        st=''.join(str(element) for element in num)
        if st[0]=='0':
            return '0'
        return st            
        


if __name__=='__main__':
    sol=Solution()
    num=[3, 30, 34, 5, 9]
    print sol.largestNumber_2(num)
    print sol.largestNumber_1(num)
    print sol.largestNumber_3(num)
