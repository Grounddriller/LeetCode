def is_anagram(str1, str2):
    if len(str1) != len(str2):
        return False

    count = {}

    for ch in str1:
        count[ch] = count.get(ch, 0) + 1

    for ch in str2:
        if ch not in count:
            return False
        count[ch] -= 1
        if count[ch] < 0:
            return False

    return True
