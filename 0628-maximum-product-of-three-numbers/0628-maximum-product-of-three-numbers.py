class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        pro=1
        s=1
        nums.sort()
        for i in range(len(nums)-1,len(nums)-4,-1):
            pro=pro*nums[i]
        for i in range(2):
            s=s*nums[i]
        return max(s*nums[-1],pro)


        