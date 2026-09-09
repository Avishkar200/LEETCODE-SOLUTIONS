class Solution:
    def countCommas(self, n: int) -> int:
        t = 0

        if n >= 1000:
            t += n - 999

        if n >= 1000000:
            t += n - 999999

        if n >= 1000000000:
            t += n - 999999999

        if n >= 1000000000000:
            t += (n - 999999999999)
        if n >= 1000000000000000:
            t += n - 999999999999999

        return t
