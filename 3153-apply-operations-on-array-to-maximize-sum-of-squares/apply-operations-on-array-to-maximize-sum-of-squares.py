class Solution(object):
    def maxSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        mod=10**9+7
        bits=[0]*30
        for num in nums:
            for b in range(30):
                if num &(1<<b):
                    bits[b]+=1
        ans=0
        for _ in range(k):
            num=0

            for b in range(30):
                if bits[b]>0:
                    num |=(1<<b)
                    bits[b]-=1
            ans=(ans+num*num)%mod
        return ans 

        