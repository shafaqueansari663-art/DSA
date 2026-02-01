class Solution(object):
    def minimumCost(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return []
        rest=nums[1:]
        rest.sort()
        return nums[0]+rest[0]+rest[1]