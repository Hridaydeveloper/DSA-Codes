class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:

        nums.sort()
        res = []

        if len(nums) < 3:
            return res

        base = 0

        while base < len(nums) - 2:
            if base > 0 and nums[base] == nums[base - 1]:
                base += 1
                continue
            i = base + 1
            j = len(nums) - 1

            while i < j:
                curr = nums[base] + nums[i] + nums[j]

                if curr == 0:
                    res.append([nums[base], nums[i], nums[j]])
                    i += 1
                    j -= 1

                    while i < j and nums[i] == nums[i - 1]:
                        i += 1
                    while i < j and nums[j] == nums[j + 1]:
                        j -= 1

                elif curr < 0:
                    i += 1

                else:
                    j -= 1

            base += 1

        return res
