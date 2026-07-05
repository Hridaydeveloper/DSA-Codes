class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0

        for bit in range(32):
            count = 0

            for num in nums:
                if (num >> bit) & 1:
                    count += 1

            if count % 3 != 0:
                res = res | (1 << bit)

        # Handle negative numbers
        if res >= 2 ** 31:
            res -= 2 ** 32

        return res
