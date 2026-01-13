class Solution:
    def isValid(self, s: str) -> bool:
        ans = []

        for i in range(len(s)):
            if ans:
                last = ans[-1]
                if self.is_pair(last, s[i]):
                    ans.pop()
                    continue
            ans.append(s[i])
            
        return not ans

    def is_pair(self, last, current):
        if last == "(" and current == ")" or last == "{" and current == "}" or last == "[" and current == "]":
            return True
        return False
