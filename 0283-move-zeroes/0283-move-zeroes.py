class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        count=0
        while 0 in nums:
            nums.remove(0)
            count+=1
        nums[:]=nums+[0]*count
        """
        Do not return anything, modify nums in-place instead.
        """
        