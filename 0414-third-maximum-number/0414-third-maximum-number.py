class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        s=sorted(set(nums))
        try:
            return s[-3]
        except IndexError:
            return max(nums)