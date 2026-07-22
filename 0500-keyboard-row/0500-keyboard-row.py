class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        a=set("qwertyuiop")
        b=set("asdfghjkl")
        c=set("zxcvbnm")
        k=[]
        for i in words:
            s=set(i.lower())
            if s<=a or s<=b or s<=c:
                k.append(i)
        return k
                    
        