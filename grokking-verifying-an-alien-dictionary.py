def verify_alien_dictionary(words, order):
    rank = {char: i for i, char in enumerate(order)}

    for i in range(len(words) - 1):
        word1 = words[i]
        word2 = words[i + 1]

        for j in range(min(len(word1), len(word2))):
            if word1[j] != word2[j]:
                if rank[word1[j]] > rank[word2[j]]:
                    return False
                break
        else:
            if len(word1) > len(word2):
                return False

    return True
