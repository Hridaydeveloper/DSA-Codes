#Two sum
#index: 0  1  2  3
nums = [2, 1, 5, 3]
target = 4
hashMap = {}
for i in range(len(nums)):
    diff = target - nums[i]
    if diff in hashMap:
        print([hashMap[diff], i])
    hashMap[nums[i]] = i
    
    