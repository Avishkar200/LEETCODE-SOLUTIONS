class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        a=[]
        for i in range(len(nums)):
            count=0
            j=0
            while j<len(nums):
                if nums[j]<nums[i]:
                    count+=1
                j+=1
            a.append(count)
        return a





        