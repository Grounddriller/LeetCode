class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        maxLength = 0
        charSet = set()
        x = 0
        
        for y in range(n):
            if s[y] not in charSet:
                charSet.add(s[y])
                maxLength = max(maxLength, y - x + 1)
            else:
                while s[y] in charSet:
                    charSet.remove(s[x])
                    x += 1
                charSet.add(s[y])
        
        return maxLength
            