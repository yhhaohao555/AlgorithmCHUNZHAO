class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordset = set(wordList)
        if endWord not in wordset:
            return 0
        beginset = set([beginWord])
        endset = set([endWord])
        visited = set([beginWord, endWord])
        step = 1

        while beginset:
            if len(beginset) > len(endset):
                beginset, endset = endset, beginset
            next_set = set()
            for word in beginset:
                letters = list(word)
                for i in range(len(letters)):
                    ch = letters[i]
                    for k in range(26):
                        letters[i] = chr(ord('a') + k)
                        new_word = ''.join(letters)
                        if new_word in wordset:
                            if new_word in endset:
                                return step + 1
                            if new_word not in visited:
                                next_set.add(new_word)
                                visited.add(new_word)
                    letters[i] = ch
            step += 1
            beginset = next_set
        return 0