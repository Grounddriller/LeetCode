class Solution:
    def romanToInt(self, s: str) -> int:
        romanVar = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        number = 0
        for i in range(len(s)-1):
            if romanVar[s[i]] < romanVar[s[(i+1)]]:
                number -= romanVar[s[i]]
            else:
                number += romanVar[s[i]]
        return number+romanVar[s[-1]] 
