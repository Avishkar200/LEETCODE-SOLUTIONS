class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        j=1
        while True:
            if k*j in nums:
                j+=1
                continue
            else:
                return k*j
                