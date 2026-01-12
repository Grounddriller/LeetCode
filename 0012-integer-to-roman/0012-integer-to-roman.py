 # input = 3749
            # 3000 -> M = 1000 -> 3000/1000 = 3 -> 3000 = MMM
            # 3749 - 3000 = 749
            # 700 -> ? -> D = 500, C = 100 -> 700/500 = 1, 200 remain
            # -> 200/100 = 2 -> DCC = 700
            # etc......

class Solution:
    def intToRoman(self, num: int) -> str:
        value_symbols = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'),
            (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), 
            (5, 'V'), (4, 'IV'), (1, 'I')
        ]

        Roman = []

        for value, symbol in value_symbols:
            if num == 0:
                break
            count = num // value
            Roman.append(symbol * count)
            num -= count * value
        return ''.join(Roman)