class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()

        closest = int(nums[0] + nums[1] + nums[2])
        base = 0
        while base < len(nums) - 2:
            i = base + 1
            j = len(nums) - 1

            while i < j:
                curr = nums[base] + nums[i] + nums[j]

                if curr == target:
                    return curr
                
                if abs(curr - target) < abs(closest - target):
                    closest = curr

                if curr < target:
                    i += 1
                else:
                    j -= 1
            base += 1
        return closest
    
        
