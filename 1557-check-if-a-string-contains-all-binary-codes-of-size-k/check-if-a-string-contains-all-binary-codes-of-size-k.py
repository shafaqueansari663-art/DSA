class Solution(object):
    def hasAllCodes(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        n=len(s)
        if n-k+1<(1<<k):
            return False 
        seen=set()
        current=0
        for i in range(n):
            current=((current<<1)&((1<<k)-1))|int(s[i])
            if i >=k-1:
                seen.add(current)
        return len(seen)==(1<<k)
        