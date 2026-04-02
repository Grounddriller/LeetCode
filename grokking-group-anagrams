def group_anagrams(strs):
    from collections import defaultdict

    anagram_map = defaultdict(list)

    for word in strs:
        freq = [0] * 26
        for ch in word:
            freq[ord(ch) - ord('a')] += 1

        anagram_map[tuple(freq)].append(word)

    return list(anagram_map.values())
