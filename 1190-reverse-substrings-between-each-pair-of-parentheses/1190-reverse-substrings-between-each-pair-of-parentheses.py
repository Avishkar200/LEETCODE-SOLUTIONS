class Solution:
    def reverseParentheses(self, s: str) -> str:
        a=[""]
        for i in s:
            if i=="(":
                a.append("")
            elif i==")":
                rev=a.pop()[::-1]
                a[-1]+=rev
            else:
                a[-1]+=i
        return a[0]
        