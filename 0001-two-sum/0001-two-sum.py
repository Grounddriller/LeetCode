class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):  
            for j in range(i+1, len(nums)):
                if nums[j] == target - nums[i]:
                    return[i,j]
        return[]

#len(nums) -> Number of elements in list
#range(len(num)) -> produces index values for each element in the list

# (Inner loop) So, each value in nums is given a index value i that can be called with nums[i]
# to get the associated integer from the array.

# (Outer loop) Functions the same as the inner loop with the key difference being indice values for j
# start at i+1. This is because we may not use the same element twice.

# (if statement) The equation finds the complement. target - int @ nums[i] == int @ nums[j]
# Also, this could've worked too: Int @ nums[i] + int @ nums[j] = target 

# (Return statement) So if the condition given in the if statement is true, then return solution as a pair of
# integers, with these integers being the index values i and j.

# Brute force approuch that goes there every possible pair in the list until it finds the answer.
# Slow approuch which uses O(n^2) meaning it takes us n^2 operations to get to our solution, with n being the number
# of elements in our array.

# (Edge Cases) Duplicate numbers, and negative numbers