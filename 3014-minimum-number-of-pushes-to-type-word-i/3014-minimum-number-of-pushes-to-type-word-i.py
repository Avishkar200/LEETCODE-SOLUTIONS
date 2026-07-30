from collections import Counter
class Solution:
    def minimumPushes(self, word: str) -> int:
        h=Counter(word)
        l=(sorted(h.values(),reverse=True))
        s=0
        for i  in range(len(l)):
            if i<=7:
                s=s+l[i]*1
            elif 8<=i<16:
                s+=l[i]*2
            elif 16<=i<24:
                s+=l[i]*3
            else:
                s+=l[i]*4
        return s

        