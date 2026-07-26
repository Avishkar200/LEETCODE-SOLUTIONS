class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        s=str(x)
        Sum=0
        for i in s:
            Sum+=int(i)
        if x%Sum==0:
            return Sum
        else:
            return -1
        