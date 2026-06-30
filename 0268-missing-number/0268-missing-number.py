class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s= sum(nums)
        tot_sum=sum(range(0,max(nums)+1))
        if len(nums)==max(nums)+1:
            return max(nums)+1
        return tot_sum-s
        