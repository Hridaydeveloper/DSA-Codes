nums = [20,1,5,0,20,9]
for i in range(len(nums)):
    minimum = i
    for j in range(i + 1, len(nums)):
        if nums[j] < nums[minimum]:
            nums[j], nums[minimum] = nums[minimum], nums[j]
print(nums)
