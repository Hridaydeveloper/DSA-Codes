#Find the sub array from the given sum.
#122. Best Time to Buy and Sell Stock II
# 217,14,242,560,48,53
# 217: Done
# 14: Done
# 242: Done
# 560: Done
# 48: Done
# 53: Done
# s = "y#fo##f"
# t = "y#f#o##f"
# count = 0
# count1 = 0
# i = len(s) - 1
# j = len(t) - 1
# while i >= 0:
#     if s[i] == "#":
#         count += 1
#     i -= 1
# while j >= 0:
#     if t[j] == "#":
#         count1 -= 1
#     j -= 1
# if s[i] != t[j]:
#     print(False)
# else:
#     print(True)
        
# nums = [-1]
# cur_sum = 0
# max_sum = nums[0]
# for i in range(len(nums)):
#     cur_sum = cur_sum + nums[i]
#     if cur_sum > max_sum:
#         max_sum = cur_sum
#     elif cur_sum < 0:
#         cur_sum = 0
        
# print(max_sum)

# nums = [2, 1, 2, 1]
# Output: 4
# hashMap = {} 
# res = []
# for i in range(len(nums)):
#     freq = nums[i] 
#     hashMap[freq] = hashMap.get(freq, 0) + 1
# for key in hashMap:
#     if hashMap[key] == 1:
#         res.append(key)
# print(max(res)) if res else print(-1) 

# nums = [1]
# max_sum = 0
# prefix_sum = 0
# for i in range(len(nums)):
#     prefix_sum += nums[i]
#     if prefix_sum > max_sum:
#         max_sum = prefix_sum
#     if prefix_sum < 0:
#         prefix_sum = 0
# print(max_sum) 

# nums1 = [1,3]
# nums2 = [2]
# res = nums1 + nums2
# res.sort()
# n = len(res)
# if n % 2 != 0:
#     ans = (n-1)//2
#     print(res[ans])
# else:
#     ans = n//2
#     result = (res[ans] + res[ans-1])/2
#     print(result)

# nums = [3,3] 
# target = 6
# hashMap = {}
# for i in range(len(nums)):
#     diff = target - nums[i]
#     if diff in hashMap:
#         print([hashMap[diff], i])
#     hashMap[nums[i]] = i 

# nums = [1]
# target = 1
# n = len(nums)
# i = 0
# j = n - 1
# while i <= j:
#     if nums[i] != target:
#         i += 1
#     if nums[j] != target:
#         j -= 1
#     if i <= j and nums[i] == target and nums[j] == target:
#         print([i, j])
#         break
# else:
#     print([-1, -1])

# nums = [15,-2,2,-8,1,7]
# length = 0
# max_length = 0
# prefix_sum = 0
# for i in range(len(nums)):
#     prefix_sum += nums[i]
#     if prefix_sum == 0:
#         length += 1
#         if length > max_length:
#             max_length = length 
# print(max_length)

nums = [3, 6]
hashMap = {}
for i in range(len(nums)):
    product = nums[i] * 2
    result = nums[i]/2
    print(result)
    if product in hashMap or result in hashMap:
        print(True)
    hashMap[nums[i]] = i
else:
    print(False)
    
    
    
