class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        square_sum=0
        a=[]
        for i in range(len(nums)):
            for j in range(len(nums)):
                sub_arr=nums[i:j+1]
                distinct_arr=len(set(sub_arr))
                square_sum+=distinct_arr**2
        return square_sum
       
