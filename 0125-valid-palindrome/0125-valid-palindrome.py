class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        f="".join(char for char in s if char.isalnum())
        d=f[::-1]
        if f==d:
            return True 
        return False
        