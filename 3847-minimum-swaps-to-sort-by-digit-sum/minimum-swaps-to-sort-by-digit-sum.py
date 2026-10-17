class Solution(object):
    def minSwaps(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def digit_sum(n):

            s=0
            while n :
                s+=n%10
                n//=10
            return s
        arr = sorted(nums, key=lambda x: (digit_sum(x), x))
        pos = {x: i for i, x in enumerate(nums)}
        swaps = 0

        for i in range(len(nums)):
            if nums[i] != arr[i]:
                j = pos[arr[i]]
                pos[nums[i]] = j
                nums[i], nums[j] = nums[j], nums[i]
                swaps += 1
        return swaps