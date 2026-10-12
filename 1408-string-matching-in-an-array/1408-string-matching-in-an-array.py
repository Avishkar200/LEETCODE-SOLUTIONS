class Solution:
    def stringMatching(self, words: list[str]) -> list[str]:
        l=[]
        words.sort(key=len)
        for i in words:
            for j in words:
                if i in j and i!=j:
                    l.append(i)
                    break
        return l


        