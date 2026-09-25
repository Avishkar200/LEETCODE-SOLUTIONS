class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            s=str(nums[i])
            Sum=0
            for j in s:
                Sum+=int(j)
            if Sum==i:
                return i
        return -1
        