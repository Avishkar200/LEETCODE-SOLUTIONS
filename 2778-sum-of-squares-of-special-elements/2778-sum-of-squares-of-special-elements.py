class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        Sum=0
        for i in range(0,len(nums)):
            if len(nums)%(i+1)==0:
                Sum+=nums[i]**2
        return Sum