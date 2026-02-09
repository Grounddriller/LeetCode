class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def dfs(counter, path):
            if len(path) == len(nums):
                ans.append(path)
                return

            for x in counter:
                if counter[x]:
                    counter[x] -= 1
                    dfs(counter, path+[x])
                    counter[x] += 1
        dfs(Counter(nums), [])
        return ans