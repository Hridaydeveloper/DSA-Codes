nums = [3,5,1,6,2,4]
for i in range(len(nums)):
    for j in range(len(nums)-i-1):
        if nums[j] > nums[j + 1]:
            nums[j+1], nums[j] = nums[j], nums[j+1]
print(nums)
