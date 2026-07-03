class Solution:
    def fib(self, n: int) -> int:
        a=0
        b=1
        if n==0:
            return 0
        else:
            for i in range(n-1):
                fib=a+b
                a=b
                b=fib
        return b
        