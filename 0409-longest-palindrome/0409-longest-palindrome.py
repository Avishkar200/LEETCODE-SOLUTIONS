from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        m=0
        p=0
        h=Counter(s)
        a=list(h.values())
        for i in range(len(a)):
            if a[i]%2==0:
                p+=a[i]
            else:
                p+=a[i]-1
                m=1
        return p+m
            



        