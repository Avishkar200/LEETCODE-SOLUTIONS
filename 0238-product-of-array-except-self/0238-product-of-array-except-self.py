import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        a=[]
        s=math.prod(nums)
        c=nums.count(0)
        if c==0:
            for i in range(len(nums)):
                a.append(int(s/nums[i]))
        elif c==1:
            r=math.prod([x for x in nums if x!=0])
            for j in range(len(nums)):

                if nums[j]==0:
                    
                    a.append(r)
                else:
                    a.append(0)
        else:
            for k in range(len(nums)):
                a.append(0)
        return a
        


        