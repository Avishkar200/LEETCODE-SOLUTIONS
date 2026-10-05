class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        total_score = 0
        depth = 0
        
        for i, char in enumerate(s):
            if char == '(':
                depth += 1
            else:
                depth -= 1
                # Check if it's a "()" pair
                if s[i - 1] == '(':
                    total_score +=2**depth 
                    
        return total_score
        