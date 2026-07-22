class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        a=set("qwertyuiop")
        b=set("asdfghjkl")
        c=set("zxcvbnm")
        k=[]
        for i in words:
            s=set(i.lower())
            if s.issubset(a) or s.issubset(b) or s.issubset(c):
                k.append(i)
        return k
                    
        