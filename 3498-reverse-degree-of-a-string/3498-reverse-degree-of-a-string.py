class Solution:
    def reverseDegree(self, s: str) -> int:
        rev_degree=0
        for i in range(len(s)):
            d=(27-(ord(s[i])-96))*(i+1)
            rev_degree+=d
        return rev_degree


        