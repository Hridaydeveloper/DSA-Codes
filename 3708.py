class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return nums
        else:
            longest = 2
            curr_length = 2
            for i in range(2, n):
                if nums[i] == nums[i - 1] + nums[i - 2]:
                    curr_length += 1
                    longest = max(curr_length, longest)
                else:
                    curr_length = 2
        return longest
        
