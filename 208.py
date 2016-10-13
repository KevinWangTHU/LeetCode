class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = {}


class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        cur = self.root
        for c in word:
            if c in cur.d:
                cur = cur.d[c]
            else:
                cur.d[c] = TrieNode()
                cur = cur.d[c]
        cur.d[0] = None

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        cur = self.root
        for c in word:
            if c in cur.d:
                cur = cur.d[c]
            else:
                return False
        return True if 0 in cur.d else False


    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        cur = self.root
        for c in prefix:
            if c in cur.d:
                cur = cur.d[c]
            else:
                return False
        return True if cur else False


# Your Trie object will be instantiated and called as such:
trie = Trie()
trie.insert("somestring")
trie.insert("key")
print trie.search("k")
print trie.startsWith("key")
