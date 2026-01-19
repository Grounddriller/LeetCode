class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        
        x = dividend
        y = divisor

        if x == y:
            return 1
        
        if x == -2**31 and y == -1:
            return (2**31) -1
        
        if y == 1:
            return x

        sign = -1 if (x < 0) ^ (y < 0) else 1

        w, z = abs(x), abs(y)
        ans = 0

        while w >= z:
            p = 0
            while w >= (z << p):
                p +=1

            p -= 1
            w -= (z << p)
            ans += (1 << p)

        return min(max(sign * ans, -2**31), 2**31 -1)