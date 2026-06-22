class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        b = text.count('b')
        a_count = text.count('a')
        l = text.count('l') // 2
        o = text.count('o') // 2
        n = text.count('n')

        return (min(b, a_count, l, o, n))