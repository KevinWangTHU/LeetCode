class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        def generate(cur):
            return [cur[:i] + chr(97+j) + cur[i+1:] for i in range(len(cur)) for j in range(26)]

        def bfs(begin, wordList):
            front = set()
            front.add(begin)
            length = 1
            while front:
                newFront = set()
                length += 1
                for word in front:
                    gene = generate(word)
                    for w in gene:
                        if w == endWord:
                            return length
                        if w in wordList:
                            newFront.add(w)
                            wordList.remove(w)
                front = newFront
            return 0

        def bfs2(beginWord, endWord, wordList):
            if beginWord == endWord:
                return 1
            front = set()
            front.add(beginWord)
            end = set()
            end.add(endWord)
            length = 1
            while front and end:
                newFront = set()
                length += 1
                for word in front:
                    gene = generate(word)
                    for w in gene:
                        if w in end:
                            return length
                        if w in wordList:
                            newFront.add(w)
                            wordList.remove(w)
                front = newFront
                newEnd = set()
                length += 1
                for word in end:
                    gene = generate(word)
                    for w in gene:
                        if w in front:
                            return length
                        if w in wordList:
                            newEnd.add(w)
                            wordList.remove(w)
                end = newEnd
            return 0

        return bfs2(beginWord, endWord, wordList)

s=Solution()
print s.ladderLength("hit","dog",{"hot","dig"})
