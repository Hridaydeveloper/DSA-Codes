# 1480. Running Sum of 1d Array
nums = [3,1,2,10,1]
stack = []
prefix_sum = 0
for i in range(len(nums)):
    prefix_sum = prefix_sum + nums[i]
    stack.append(prefix_sum)
print(stack)
        
    
    