class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        # n ^ 0 = n
        for i in range(len(nums)):
            result = nums[i] ^ result
        return result

        
