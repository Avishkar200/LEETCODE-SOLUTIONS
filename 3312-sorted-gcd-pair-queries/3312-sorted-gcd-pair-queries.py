import math
from itertools import accumulate
from bisect import bisect_right
from collections import Counter
from typing import List

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        max_num = max(nums)
        
        counts = Counter(nums)
        
        count_divisor = [0] * (max_num + 1)
        for i in range(1, max_num + 1):
            for j in range(i, max_num + 1, i):
                count_divisor[i] += counts[j]
                
        count_gcd_pair = [0] * (max_num + 1)
        
        for gcd in range(max_num, 0, -1):
            v = count_divisor[gcd]
            total_pairs = v * (v - 1) // 2
            
            for larger_gcd in range(2 * gcd, max_num + 1, gcd):
                total_pairs -= count_gcd_pair[larger_gcd]
                
            count_gcd_pair[gcd] = total_pairs
       
        prefix_sums = list(accumulate(count_gcd_pair))
        
 
        ans = []
        for q in queries:
            idx = bisect_right(prefix_sums, q)
            ans.append(idx)
            
        return ans