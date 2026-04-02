def extra_character_index(str1, str2):
    xor_result = 0

    # XOR all characters from both strings
    for ch in str1:
        xor_result ^= ord(ch)
    for ch in str2:
        xor_result ^= ord(ch)

    # This is the extra character
    extra_char = chr(xor_result)

    # Determine the longer string
    longer = str1 if len(str1) > len(str2) else str2

    # Return first occurrence index
    for i, ch in enumerate(longer):
        if ch == extra_char:
            return i

    return -1
