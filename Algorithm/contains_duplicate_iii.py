import random
import collections
class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        dic = collections.OrderedDict()          
        for val in nums:
            key  = val / t if t else val

            if dic.get(key) or (dic.get(key-1) and (dic.get(key-1) - val<= t)) or  (dic.get(key+1) and (dic.get(key+1) - val <= t)):
                return True
            print dic
            if len(dic) == k:
                dic.popitem(False)
            dic[key] = val
            print dic
        return False
    def containsNearbyAlmostDuplicate1(self, nums, k, t):
        dic = collections.OrderedDict()          
        for val in nums:
            key  = val  if not t else val/t 
            for pre in ( dic.get(key-1), dic.get(key),dic.get(key+1)):
                print pre, val
                if pre and abs(pre - val) <= t:
                    return True
            if len(dic) == k:
                dic.popitem(False)
            dic[key] = val
        return False            
                
if __name__ == '__main__':
    sol = Solution()
    nums = [random.randint(1, 20) for i in range(10)]
    k = random.randint(1, 10)
    t = random.randint(1, 10)
    nums = [2,2]
    k = 3
    t = 0
    nums = [1,3,1]
    k = 1
    t = 1
    nums = [3,6,0,2]
    k = 2
    t = 2
    print nums, k, t
    print sol.containsNearbyAlmostDuplicate(nums, k, t)
    print sol.containsNearbyAlmostDuplicate1(nums, k, t)
