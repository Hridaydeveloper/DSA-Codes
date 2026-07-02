#Remove Duplicates from sorted array
nums = [0,0,1,1,1,2,2,3,3,4]
start = 0
for i in range(len(nums)):
    if nums[i] != nums[start]:
        start += 1 
        nums[start] = nums[i]
print(nums)