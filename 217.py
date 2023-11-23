class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        # Solution 1 TC: O(N^2)
        # for i in range(0, len(nums)):
        #     val   = nums[i]
        #     count = 1
        #     for j in range(i+1, len(nums)):
        #         if val == nums[j]:
        #             count+=1

        #     if count >=2:
        #         return True
        # return False 

        # Solution 2
        count = {}

        for i in nums:
            if i not in count:
                count[i] = 1
            else:
                count[i] += 1
            
            if count[i] >= 2:
                return True
        
        return False
