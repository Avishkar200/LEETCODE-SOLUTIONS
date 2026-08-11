"""class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        st=nums[0]
        max_len=1
        k=[st]
        m=[k]
        for i in range(1,len(nums)):
            if nums[i-1]==nums[i]-1:
                k.append(nums[i])    
            else:
                st=nums[i]
                m.append(k)
                k=[st]
        m.sort(reverse=True,key=len)
        j=sum(m[0])
        while j in nums:
            j+=1
        return j"""
                
class Solution:

    def missingInteger(self, nums: list[int]) -> int:
        prefix_sum = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                prefix_sum += nums[i]
            else:
                break
        num_set = set(nums)

        while prefix_sum in num_set:
            prefix_sum += 1

        return prefix_sum 

                
        
            


        