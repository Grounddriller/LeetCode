class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        word_freq = {}
        for word in words:
            word_freq[word] = 1 + word_freq.get(word, 0)

        word_len = len(words[0])
        window_len = len(words) * word_len
        ans = []
        
        for i in range(len(s) - window_len + 1):
            substr_freq = {}
            j = i

            while j < i + window_len:
                current_word = s[j : j + word_len]

                if current_word not in word_freq:
                    break
                substr_freq[current_word] = substr_freq.get(current_word, 0) + 1

                if substr_freq[current_word] > word_freq[current_word]:
                    break
                j += word_len

            if j == i + window_len:
                ans.append(i)
        
        return ans

