def count_pairs(nums, target):
    nums.sort()
    left = 0
    right = len(nums) - 1
    count = 0
    
    while left < right:
        current_sum = nums[left] + nums[right]
        
        if current_sum < target:
            count += (right - left)
            left += 1
        else:
            right -= 1
            
    return count
