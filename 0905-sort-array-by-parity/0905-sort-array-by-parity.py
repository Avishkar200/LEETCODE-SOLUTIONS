class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        j=[]
        for i in range(len(nums)):
            if nums[i]%2==0:
                j.append(nums[i])
        for k in range(len(nums)):
            if nums[k]%2!=0:
                j.append(nums[k])
        return j