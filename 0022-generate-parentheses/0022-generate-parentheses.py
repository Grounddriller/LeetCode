class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def combine(openPar, closePar, s):
            if openPar == closePar and openPar + closePar == n * 2:
                ans.append(s)
                return

            if openPar < n:
                combine(openPar + 1, closePar, s + "(")
            
            if closePar < openPar:
                combine(openPar, closePar + 1, s + ")")

        combine(0, 0, "")

        return ans