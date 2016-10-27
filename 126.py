import collections, string
class Solution(object):
    def findLadders(self, beginWord, endWord, wordlist):
        """
        :type beginWord: str
        :type endWord: str
        :type wordlist: Set[str]
        :rtype: List[List[int]]
        """
        def construct_paths(source, dest, tree):
            if source == dest:
                return [[source]]
            return [[source] + path for succ in tree[source]  # path can be [] - for failed trials.
                    for path in construct_paths(succ, dest, tree)]

        def add_path(tree, word, neigh, is_forw):
            if is_forw:
                tree[word] += neigh,
            else:
                tree[neigh] += word,

        def bfs_level(cur, other, tree, is_forw, wordlist):
            if not cur:
                return False
            if len(cur) > len(other):
                return bfs_level(other, cur, tree, not is_forw, wordlist)
            for word in (cur | other):
                wordlist.discard(word)
            next, done = set(), False
            while cur:
                word = cur.pop()
                for neigh in [word[:idx] + c + word[idx+1:]
                              for c in string.ascii_lowercase
                              for idx in range(len(word))]:
                    if neigh in other:
                        done = True
                        add_path(tree, word, neigh, is_forw)
                    if not done and neigh in wordlist:
                        next.add(neigh)
                        add_path(tree, word, neigh, is_forw)
            return done or bfs_level(next, other, tree, is_forw, wordlist)

        tree, paths = collections.defaultdict(list), []
        is_found = bfs_level(set([beginWord]), set([endWord]), tree, True, wordlist)
        return construct_paths(beginWord, endWord, tree)
s=Solution()
print s.findLadders("hit", "dog", {"hog", "hig", "hip"})
