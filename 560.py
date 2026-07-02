nums = [1, 2, 3]
k = 5
hashMap = {0: 1}
count = 0
prefix_sum = 0
for i in range(len(nums)):
    prefix_sum = prefix_sum + nums[i]
    diff = prefix_sum - k
    if diff in hashMap:
        count += hashMap[diff]
    hashMap[prefix_sum] = hashMap.get(prefix_sum, 0) + 1
print(count)
    
    