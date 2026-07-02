#Contain Duplicate 
nums = [1,1,1,3,3,4,3,2,4,2]
hashmap = {}
for i in range(len(nums)):
    if nums[i] in hashmap:
        print("true")
        break
    hashmap[nums[i]] = 1
else:
    print("false")
    