class Solution:
    def shortestToChar(self, s: str, c: str) -> list[int]:
        a = []
        l = []
        
        # 1. Find all indices where character matches c
        for i in range(len(s)):
            if s[i] == c:
                a.append(i)
        
        # 2. For each character, find the minimum absolute distance
        for i in range(len(s)):
            min_val = float('inf')  # Start with a very large number
            for j in a:
                d = abs(i - j)
                if d < min_val:     # Keep the smallest distance
                    min_val = d
            l.append(min_val)       # Add the minimum distance to the result list
            
        return l
