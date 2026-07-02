#Contains Duplicate III
nums = [1,5,9,1,5,9]
indexDiff = 2
valueDiff = 3
for i in range(len(nums)):
    for j in range(len(nums)):
        if i != j and abs(i - j) <= indexDiff and abs(nums[i] - nums[j]) <= valueDiff:
            print("true")
    break
else:
    print("false")
            