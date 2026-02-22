class Solution(object):
    def binaryGap(self, n):
        """
        :type n: int
        :rtype: int
        """
        max_distance=0
        prev_index=-1
        index=0
        while n:
            if n & 1:
                if prev_index!=-1:
                    max_distance=max(max_distance,(index-prev_index))
                prev_index=index
            n>>=1
            index+=1
        return max_distance
        