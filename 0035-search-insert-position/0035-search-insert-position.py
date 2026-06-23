class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            h=0
            if nums[i]>=target:
                h=i
                break
            elif target>nums[len(nums)-1]:
                return len(nums)
        return h
        