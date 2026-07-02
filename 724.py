#Find the Pivot Index (Prefix Sum)
nums = [3, 1, 7, 2, 1, 6, 6, 1]
left_sum = 0
total_sum = sum(nums)
for i in range(len(nums)):
    right_sum = total_sum - left_sum - nums[i]
    if left_sum == right_sum:
        print(i)
    left_sum += nums[i]
print("-1")