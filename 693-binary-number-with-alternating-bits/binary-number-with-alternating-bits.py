class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        prev= n&1
        n>>=1
        while n:
            cur=n&1
            if cur==prev:
                return False
            prev=cur
            n>>=1
        return True


