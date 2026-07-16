class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        s=[i[::-1] for i in image]
        for i in range(len(s)):
            for j in range(len(s[i])):
                if s[i][j]==1:
                    s[i][j]=0
                else:
                    s[i][j]=1
        return s
                

        