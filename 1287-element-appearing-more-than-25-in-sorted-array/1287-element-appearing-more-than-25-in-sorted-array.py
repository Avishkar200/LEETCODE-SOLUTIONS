class Solution:
    def findSpecialInteger(self, arr: list[int]) -> int:
        s=list(set(arr))
        for i in s:
            if arr.count(i)>len(arr)/4:
                return i
        
        