def partition(nums,low,high):
    pivot = high
    i = low
    start = low
    
    while i < len(nums):
        if nums[i] < nums[pivot]:
            nums[start], nums[i] = nums[i], nums[start]
            start += 1
        i += 1
    nums[start], nums[pivot] = nums[pivot], nums[start]
    
    return start
    
def quick_sort(nums, low, high):
    if low < high:
        pivot_idx = partition(nums, low, high)
        
        #left quick_sort
        quick_sort(nums, low, pivot_idx - 1)
        
        #right quick_sort
        quick_sort(nums, pivot_idx + 1, high)
    
nums = [10, 20, 3, 5, 7, 8,8,7,6]
quick_sort(nums, 0, len(nums)- 1)
print(nums)
