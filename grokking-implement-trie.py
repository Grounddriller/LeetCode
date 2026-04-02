from trie_node import *

class Trie():
    def __init__(self):
        self.root = TrieNode()

    # inserting string in trie
    def insert(self, string):
        node = self.root

        for char in string:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]

        node.is_end = True

    # searching for a string
    def search(self, string):
        node = self.root

        for char in string:
            if char not in node.children:
                return False
            node = node.children[char]

        return node.is_end

    # searching for a prefix
    def search_prefix(self, prefix):
        node = self.root

        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]

        return True
