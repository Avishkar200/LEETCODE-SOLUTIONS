class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        l=len(nums)
        max_num=max(nums)
        min_num=min(nums)
        max_index=max(nums.index(max_num),nums.index(min_num))
        min_index=min(nums.index(max_num),nums.index(min_num))
        if l==0:
            return 0
        elif l==1:
            return 1
        else:
            m=(min_index+1)+l-max_index
            o=l-min_index
        return min(m,o,(max_index+1))



         
        