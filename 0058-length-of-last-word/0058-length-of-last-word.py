class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        d=s.strip()
        count=0
        i=-1
        g=d.count(" ")
        if g==0:
            return len(d)
        else:
            while d[i]!=" ":
                count+=1
                i-=1
        return count




        