class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        actual = (len(nums) * (len(nums)+1))/2
        total  = sum(nums)
        return actual - total
