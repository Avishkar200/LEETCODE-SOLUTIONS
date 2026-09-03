
class Solution:
    def uniformArray(self, A):
        min_odd = min((x for x in A if x & 1), default=float('inf'))
        min_even = min((x for x in A if not x & 1), default=float('inf'))

        return min_odd < min_even or min_odd == float('inf')

