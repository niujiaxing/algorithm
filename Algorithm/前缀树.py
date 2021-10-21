class Trie:

    def __init__(self):
        self.children = [None for _ in range(26)]
        self.isend = False

    def insert(self, word: str) -> None:
        root = self.children
        for i in range(len(word)):
            ch = ord(word[i])-ord('a')
            if not root[ch]:
                root[ch] = Trie()
                root = root[ch]
                if i == len(word)-1:root.isend = True

    def search(self, word: str) -> bool:
        root = self.children
        for i in range(len(word)):
            ch = ord(word[i]) - ord('a')
            if not root[ch]:
                return False
            root = root[ch]
        return True if root.isend == True else False




    def startsWith(self, prefix: str) -> bool:
        root = self.children
        for i in range(len(prefix)):
            ch = ord(prefix[i]) - ord('a')
            if not root[ch]:
                return False
            root = root[ch]
        return True

root = Trie()
