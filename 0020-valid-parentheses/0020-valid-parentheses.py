class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        mapping={
            "]":"[",
            ")":"(",
            "}":"{"
        }
        for i in s:
            if i in mapping.values():
                stack.append(i)
            elif not stack or stack.pop()!=mapping[i]:
                return False
        return len(stack)==0

