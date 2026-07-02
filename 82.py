#Remove duplicates from sorted array
nums = [1,1,1,2,2,3]
start = 1
for i in range(2, len(nums)):
    if nums[i] != nums[start - 1]:
        start += 1
        nums[start] = nums[i]
print(start + 1)   