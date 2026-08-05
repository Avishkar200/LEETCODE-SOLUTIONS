class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        smaller_map = {}
        
        for i, num in enumerate(sorted_nums):
            if num not in smaller_map:
                smaller_map[num] = i
                
        return [smaller_map[num] for num in nums]