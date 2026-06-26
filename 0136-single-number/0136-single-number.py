from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n=0
        for i in nums:
            n^=i   #XOR ALL THE VALUES
        return n