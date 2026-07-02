# matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
# n = len(matrix)
# m = len(matrix[0])
# res = []
# first_col = 0
# end_col = m - 1
# first_row = 0
# end_row = n - 1

# while len(res) <n*m:
#     #first_row, first_col --> end_col
#     for i in range(first_col, end_col + 1):
#         res.append(matrix[first_row][i])
#     first_row += 1
#     if len(res) == n*m:
#         break
    
#     #end_col, first_row --> end_row
#     for i in range(first_row, end_row + 1):
#         res.append(matrix[i][end_col])
#     end_col -= 1
#     if len(res) == n*m:
#         break
    
#     #end_row, end_col --> first_col
#     for i in range(end_col, first_col - 1, -1):
#         res.append(matrix[end_row][i])
#     end_row -= 1
#     if len(res) == n*m:
#         break
    
#     #first_col, end_row --> first_row
#     for i in range(end_row, first_row -1, -1):
#         res.append(matrix[i][first_col])
#     first_col += 1
# print(res)

# nums = [2, 7, 1, 6, 3]
# # Output: 3
# total_sum = sum(nums)
# left_sum = 0
# for i in range(len(nums)):
#     right_sum = total_sum - left_sum - nums[i]
#     if left_sum == right_sum:
#         print(i)
#     left_sum += nums[i]
    

# set1 = {100, 12.2, 'hii', 'hello', 'hello'}
# set2 = set1.copy()
# print(len(set1))
# set1.add(100)
# set2.discard(100)
# set1.clear()
# print(set1)
# print(set2)

# set1 = {5, 1, 8, 7}
# set2 = {2, 1, 5, 6, 9}
# # union
# print(set1|set2)
# print(set2.union(set1))
# # intersection
# print(set1 & set2)
# print(set1.intersection(set2)) 
# # difference
# print(set2 - set1)
# print(set1.difference(set2)) 
# # symmetric difference
# print(set2^set1)
# print(set1.symmetric_difference(set2))

# dict1 = {1: "Hriday", 2: "Debapriya", 3: "Tuya", 4: "Tiya", 5: "Gopal"}
# for i in dict1:
#     print(f"{i}.",dict1[i])
# for i in dict1.items():
#     print()
# print(list(dict1.items()))

# list1 = [2, 1, 3, 3, 1, 4, 4]
# res = {}
# for i in list1:
#     if i in res:
#         res[i] += 1
#     else:
#         res[i] = 1
# for i in res:
#     print(i, res[i])

nums = [2, 1, 4, 8, 5]
# target = 13
# hashMap = {}
# for i in range(len(nums)):
#     diff = target - nums[i]
#     if diff in hashMap:
#         print([hashMap[diff], i])
#     else:
#         hashMap[nums[i]] = i

# min_price = nums[0]
# profit = 0
# for i in range(1, len(nums)):
#     diff = nums[i] - min_price
#     if diff > profit:
#         profit = diff
#     elif nums[i] < min_price:
#         min_price = nums[i]
# print(profit)

# If the array is sorted
# nums = [1, 3, 4, 5, 8]
# target = 11
# i = 0
# j = len(nums) - 1
# while i<j:
#     sum = nums[i] + nums[j]
#     if sum > target:
#         j -= 1
#     elif sum < target:
#         i += 1
#     elif sum == target:
#         print(i, j)
#         break
# else:
#     print("Not Found.")

# arr = [4,0,4,3,3]
# k = 5
# # 2.80000
# window_sum = sum(arr[:k])
# max_avg = window_sum

# for i in range(k, len(arr)):
#     window_sum = window_sum - arr[i - k] + arr[i]
#     if window_sum > max_avg:
#         max_avg = window_sum
    
# print(max_avg/k)

# s = "abcedf"
# hashMap = {}
# start = 0
# longest = 0
    
# for i in range(len(s)):
#     if s[i] in hashMap and hashMap[s[i]] >= start:
#         start = hashMap[s[i]] + 1
        
#     curr_length = i - start + 1
#     if curr_length > longest:
#         longest = curr_length
    
#     hashMap[s[i]] = i
    
# print(longest)
         
# nums = [2, 1, 2, 4, 7]
# target = 11
# hashMap = {}
# for i in range(len(nums)):
#     diff = target - nums[i]
#     if diff in hashMap:
#         print([hashMap[diff], i])
#     hashMap[nums[i]] = i

# nums = [2,1,-1]
# total = sum(nums)
# left_sum = 0
# for i in range(len(nums)):
#     right_sum = total - left_sum - nums[i]
#     if left_sum == right_sum:
#         print(i)    
#     left_sum += nums[i]
# else:
#     print("-1")

# prices = [7,5, 1]
# min_price = prices[0]
# profit = 0
# for i in range(1, len(prices)):
#     diff = prices[i] - min_price
#     if diff > profit:
#         profit = diff
#     elif prices[i] < min_price:
#         min_price = prices[i]
# print(profit)
    
# s = "y#fo##f"
# t = "y#f#o##f"
# # output: ad 
# stack = []
# stack1 = []
# for i in range(len(s)):
#     if s[i] == "#":
#         if len(stack) > 0:
#             stack.pop()
#     else:
#         stack.append(s[i])
        
# for i in range(len(t)):
#     if t[i] == "#":
#         if len(stack1) > 0:
#             stack1.pop()
#     else:
#         stack1.append(t[i])
        
# print(''.join(stack))
# print(''.join(stack1))        

# nums = [1,2,3,5,7,4,10]
# for i in range(len(nums)):
#     if nums[i] % 2 != 0:
#         nums[i] = nums[i] * -1
# nums.sort()
# for i in range(len(nums)):
#     if nums[i] % 2 != 0:
#         nums[i] = nums[i] * -(1)
# print(nums)

# nums = [6,6,6,6]
# n = len(nums)//2
# hashMap = {}
# count = 0
# for i in range(len(nums)):
#     if nums[i] not in hashMap:
#         if count < n:
#             count += 1
#             hashMap[nums[i]] = i
# print(count)

# nums = "leetcode"
# hashMap = {}
# for i in range(len(nums)):
#     n = nums[i]
#     hashMap[n] = hashMap.get(n, 0) + 1
# print(hashMap)
# for i, n in enumerate(nums):
#     if hashMap[n] == 1:
#         print(i)
#         break
# else:
#     print(-1)

temp = [10, 2, 1, 3, 4]
res = []
count = 0
start = temp[0]
for i in range(1, len(temp)):
    if start < temp[i]:
        count += 1
        res.append(count)
        start += 1
        count = 0
    elif start > temp[i]:
        count += 1
        start += 1
print(res)