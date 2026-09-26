class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        d={}
        for key,value in knowledge:
            d[key]=value
        result=[]
        key=""
        j=False
        for i in s:
            if i=="(":
                j=True
                key=""
            elif i==")":
                if key in d:
                    result.append(d[key])
                else:
                    result.append("?")
                j=False
            elif j:
                key+=i
            else:
                result.append(i)
        return "".join(result)
        