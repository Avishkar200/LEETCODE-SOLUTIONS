class Solution:
    def checkIfExist(self, arr: list[int]) -> bool:
        seen=set()
        for i in arr:
            if 2*i in seen or (i%2==0 and i//2 in seen):
                return True
            seen.add(i)
        return False
        """
        if list(set(arr))==[0]:
            return True
        for i in range(len(arr)):
            if (arr[i]/2) in arr and arr[i]>0:
                return True
        return False
        """