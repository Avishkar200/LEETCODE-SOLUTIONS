class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a=[]
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                a.append(nums1[i])
        h=set(a)
        return sorted(h)