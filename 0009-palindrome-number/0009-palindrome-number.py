class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev=0
        temp=x
        if x<0:
            return False
        else:
            while x>0:
                digit=x%10
                rev=rev*10+digit
                x=x//10
            if temp==rev:
                return  True
            else:
                return False 

        