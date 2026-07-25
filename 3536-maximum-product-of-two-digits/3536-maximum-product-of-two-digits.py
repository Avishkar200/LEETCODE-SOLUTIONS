class Solution:
    def maxProduct(self, n: int) -> int:
        a=[]
        s=str(n)
        for i in range(len(s)):
            a.append(int(s[i]))
        a.sort()
        return a[-1]*a[-2]

        