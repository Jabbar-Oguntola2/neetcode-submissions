class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i, val in enumerate(nums):
            needed = target - val
            if needed in dic:
                return [dic[needed], i]
            dic[val] = i
        
