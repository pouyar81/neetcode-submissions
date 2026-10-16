class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # nums = [3,4,5,6]
        # target = 9

        seen = {} # index: value

        for i, n in enumerate(nums):
            diff = target - n
            if diff in seen:
                return [seen[diff], i]
            seen[n] = i







    
        