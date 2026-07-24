class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a=[]
        for i in range(len(nums1)):
            r=True
            j=nums2.index(nums1[i])
            l=j
            while l<len(nums2)-1:
                if nums2[l+1]>nums1[i] and r==True:
                    a.append(nums2[l+1])
                    r=False
                else:
                    l+=1
            if len(a)<i+1:
                a.append(-1)
        return a

