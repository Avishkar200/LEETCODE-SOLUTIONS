class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        a="Gold Medal"
        b="Silver Medal"
        c="Bronze Medal"
        l=[]
        s=sorted(score,reverse=True)
        for i in range(len(score)):
            h=s.index(score[i])
            j=h+1
            if j==1:
                l.append(a)
            if j==2:
                l.append(b)
            if j==3:
                l.append(c)
            if j!=1 and j!=2 and j!=3:
                l.append(str(j))
        return l


        