def largest_integer(num):
    digits = list(str(num))
    
    even_digits = []
    odd_digits = []
    
    for ch in digits:
        digit = int(ch)
        if digit % 2 == 0:
            even_digits.append(digit)
        else:
            odd_digits.append(digit)
            
    even_digits.sort(reverse=True)
    odd_digits.sort(reverse=True)
    
    even_index = 0
    odd_index = 0
    result = []
    
    for ch in digits:
        digit = int(ch)
        
        if digit % 2 == 0:
            result.append(str(even_digits[even_index]))
            even_index += 1
        else:
            result.append(str(odd_digits[odd_index]))
            odd_index += 1
            
    return int("".join(result))
