class Solution:
    def maxDepth(self, s: str) -> int:
        max_par=0
        count=0
        for i in s:
            if i=="(":
                count+=1
            if count>max_par:
                max_par=count
            if i==")":
                count-=1
        return max_par
        