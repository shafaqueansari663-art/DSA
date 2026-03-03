class Solution(object):
    def findKthBit(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        if n==1:
            return "0"
        length=(1<<n)-1
        middle=(1<<(n-1))
        #if middle
        if k==middle:
            return "1"
        #from left half
        if k < middle:
            return self.findKthBit(n-1,k)
        #right half
        mirror=length-k+1
        bit=self.findKthBit(n-1,mirror)
        #inverting bit 
        return "1" if bit =="0" else"0"

        