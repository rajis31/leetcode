class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        # Solution 1
        # missing = []
        # for i in range(1, len(nums)+1):
        #     if i not in nums:
        #         missing.append(i)
        # return missing

        # Solution 2
        # missing = [i for i in range(1, len(nums)+1) if i not in nums]
        # return missing

        # Solution 3
        # setA = set(nums)
        # setB = set(range(1, len(nums)+1))
        # return setB - setA
