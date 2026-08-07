class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        leftSum=[0]
        rightSum=[]
        Sum=0
        i=0
        while i<len(nums)-1:
            Sum+=nums[i]
            leftSum.append(Sum)
            i+=1
        for i in range(len(nums)-1):
            r=0
            r+=sum(nums[i+1:len(nums)])
            rightSum.append(r)
        rightSum.append(0)
        answer=[abs(x-y) for x,y in zip(leftSum,rightSum)]
        return answer
        

        






        