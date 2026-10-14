class Solution(object):
    def maxSumOfSquares(self, num, sum):
        """
        :type num: int
        :type sum: int
        :rtype: str
        """
        if sum <1 or sum> 9*num:
            return ""
        result=""
        for i in range(num):
            digit=min(9,sum)
            result+=str(digit)
            sum-=digit
        return result        