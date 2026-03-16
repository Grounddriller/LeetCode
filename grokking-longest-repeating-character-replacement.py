def longest_repeating_character_replacement(s, k):
    left, max_count, longest, freq = 0, 0, 0, {}
    
    for right in range(len(s)):
        char = s[right]
        freq[char] = freq.get(char, 0) + 1
        
        max_count = max(max_count, freq[char])
        
        while (right - left + 1) - max_count > k:
            freq[s[left]] -= 1
            left += 1
            
        longest = max(longest, right - left + 1)
        
    return longest
