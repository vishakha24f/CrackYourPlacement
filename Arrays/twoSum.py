class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = {}
        
        for i, num in enumerate(nums):
            difference = target - num
            
            if difference in num_to_index:
                return [num_to_index[difference], i]
            
            num_to_index[num] = i
        return []
        