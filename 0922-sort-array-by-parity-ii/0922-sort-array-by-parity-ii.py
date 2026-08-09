class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        j=[]
        l=0
        k=1
        index=0
        while index<len(nums):
            if nums[index]%2==0:
                j.insert(l,nums[index])
                l+=2
            else:
                j.insert(k,nums[index])
                k+=2
            index+=1
        return j
                
        