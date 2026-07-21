from collections import Counter
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
    
        a = Counter(nums)
        k = []

        max_freq = max(a.values())
        t = [i for i, j in a.items() if j == max_freq]

        for i in t:
            run_condition_l = True
            run_condition_r = True
            f = 0
            h = 0
            
            for l in range(len(nums)):
                if run_condition_l and nums[l] == i:
                    f = l
                    run_condition_l = False  # Lock it down
                    break

            for r in range(len(nums) - 1, -1, -1):
                if run_condition_r and nums[r] == i:
                    h = r
                    run_condition_r = False 
                    break
                    
            m = h - f + 1
            k.append(m)
        return min(k)



        