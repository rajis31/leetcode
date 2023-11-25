class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counts = {}

        for num in nums:
            if not counts.get(num):
                counts[num] = 1

            elif counts.get(num):
                del counts[num]   
        return list(counts.keys())[0]
