nums = [9,30,1,5,2,4,1]
for i in range(len(nums)):
    minimum = nums[i]
    for j in range(i + 1, len(nums)):
        if nums[j] < minimum:
            minimum, nums[j] = nums[j], minimum
    nums[i], minimum = minimum, nums[i]
print(nums)
