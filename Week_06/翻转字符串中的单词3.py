class Solution(object):
    def reverseWords(self, s):
        def reverse(word):
            letters = list(word)
            i, j = 0, len(letters) - 1
            while i < j:
                letters[i], letters[j] = letters[j], letters[i]
                i += 1
                j -= 1
            return "".join(letters)
        words = s.split()
        for i in range(len(words)):
            words[i] = reverse(words[i])
        return " ".join(words)