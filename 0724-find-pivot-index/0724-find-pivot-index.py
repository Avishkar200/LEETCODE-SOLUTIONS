class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        t=sum(nums)
        l=0
        for i,j in enumerate(nums):
            if l==(t-l-j):
                return i
            l+=j
        return -1
        
          
        