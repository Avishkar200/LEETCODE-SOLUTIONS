class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        for i in range(len(numbers)):
            if target-numbers[i] in numbers[i+1:]:
                return [i+1,numbers.index(target-numbers[i],i+1)+1]"""
        left=0
        right=len(numbers)-1
        while left<right:
            total =numbers[left]+numbers[right]
            if total==target:
                return[left+1,right+1]
            elif total<target:
                left+=1
            else:
                right-=1
            

            