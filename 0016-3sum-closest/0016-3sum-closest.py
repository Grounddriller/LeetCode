class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = nums[0] + nums[1] + nums[2]
        n = len(nums)

        for i in range(n-2):
            j = i+1
            k = len(nums) - 1

            while j < k:
                total = nums[i] + nums[j] + nums[k]

                if abs(target - total) < abs(target - ans):
                    ans = total
                
                if total == target:
                    return target
                
                elif total < target:
                    j += 1
                
                else:
                    k -= 1
            
        return ans
