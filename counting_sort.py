nums = [4, 2, 2, 8, 3, 3, 1]

max_ele = max(nums)
count = [0] * (max_ele + 1)

for num in nums:
    count[num] += 1

i = 0

for num in range(max_ele + 1):
    for j in range(count[num]):
        nums[i] = num
        i += 1

print(nums)
