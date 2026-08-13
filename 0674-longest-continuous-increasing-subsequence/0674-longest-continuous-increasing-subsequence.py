
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        count = 1
        max_len = 1
        
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                count += 1
            else:
                count = 1  
                
            if count > max_len:
                max_len = count
                
        return max_len
        