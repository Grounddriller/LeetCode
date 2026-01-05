class Solution:
    def longestPalindrome(self, s: str) -> str:
        def check(i, j):
            x = i
            y = j - 1

            while x < y:
                if s[x] != s[y]:
                    return False

                x += 1
                y -= 1

            return True

        for length in range(len(s), 0, -1):
            for start in range(len(s) - length + 1):
                if check(start, start + length):
                    return s[start : start + length]

        return ""