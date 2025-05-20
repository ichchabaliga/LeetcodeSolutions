# Last updated: 19/05/2025, 20:17:55
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
    
    def longest_common_prefix(self):
        prefix = []
        node = self.root
        
        # Traverse while node has exactly one child and is not end of a word
        while node and not node.is_end_of_word and len(node.children) == 1:
            char = next(iter(node.children))  # Get the single child character
            prefix.append(char)
            node = node.children[char]
        
        return "".join(prefix)
    
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
    
        trie = Trie()
        for word in strs:
            trie.insert(word)
        
        return trie.longest_common_prefix()