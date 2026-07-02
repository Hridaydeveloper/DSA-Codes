nums = [-2,1,-3,4,-1,2,1,-5,6]
max_sub = nums[0]
curr_sum = 0
for i in range(len(nums)):
    curr_sum += nums[i]
    if curr_sum > max_sub:
        max_sub = curr_sum
    if curr_sum < 0:
        curr_sum = 0
print(max_sub)
        
    