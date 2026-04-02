from trie_node import *

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word):
        node = self.root

        for char in word:
            index = ord(char) - ord('a')

            if node.children[index] is None:
                node.children[index] = TrieNode()

            node = node.children[index]

        node.is_end = True

    def search_word(self, word):
        def dfs(index, node):
            if index == len(word):
                return node.is_end

            char = word[index]

            if char == ".":
                for child in node.children:
                    if child and dfs(index + 1, child):
                        return True
                return False
            else:
                idx = ord(char) - ord('a')
                if node.children[idx] is None:
                    return False
                return dfs(index + 1, node.children[idx])

        return dfs(0, self.root)

    def get_words(self):
        result = []

        def dfs(node, path):
            if node.is_end:
                result.append(path)

            for i in range(26):
                if node.children[i]:
                    dfs(node.children[i], path + chr(i + ord('a')))

        dfs(self.root, "")
        return result
