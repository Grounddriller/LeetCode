class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        n = len(s1)
        if n != len(s2):
            return False
        if s1 == s2:
            return True
        
        memo = {}
        
        def dfs(l, i, j):
            if (l, i, j) in memo:
                return memo[(l, i, j)]
            
            if s1[i:i+l] == s2[j:j+l]:
                memo[(l, i, j)] = True
                return True
            
            if sorted(s1[i:i+l]) != sorted(s2[j:j+l]):
                memo[(l, i, j)] = False
                return False
            
            for k in range(1, l):
                if dfs(k, i, j) and dfs(l-k, i+k, j+k):
                    memo[(l, i, j)] = True
                    return True

                if dfs(k, i, j+l-k) and dfs(l-k, i+k, j):
                    memo[(l, i, j)] = True
                    return True
            
            memo[(l, i, j)] = False
            return False
        
        return dfs(n, 0, 0)