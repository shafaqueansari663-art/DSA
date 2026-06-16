class Solution(object):
    def processStr(self, s):
        """
        :type s: str
        :rtype: str
        """
        result=[]
        for ch in s:
            if ch.islower():
                result.append(ch)
            elif ch=="%":
                result.reverse()
            elif ch=="*":
                if result:
                    result.pop()
            elif ch=="#":
                result.extend(result)       
        return "".join(result)