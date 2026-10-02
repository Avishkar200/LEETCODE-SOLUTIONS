class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        rem_weight=0
        stones.sort()
        while len(stones)>1:
            if stones[-1]==stones[-2]:
                stones.pop()
                stones.pop()
            else:
                rem_weight=stones[-1]-stones[-2]
                stones.pop()
                stones.pop()
                stones.append(rem_weight)
                stones.sort()
            if len(stones)==0:
                return 0
        return stones[0]
        