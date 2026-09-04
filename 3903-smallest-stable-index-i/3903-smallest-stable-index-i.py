class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        s=[]
        n=len(nums)
        for i in range(n):
            l=max(nums[0:i+1])-min(nums[i:n])
            s.append(l)
        for j in range(len(s)):
            if s[j]<=k:
                return s.index(s[j])
        return -1
        