class Solution(object)
    def reverseWords(self, s):
        words = s.split()
        i, j = 0, len(words) - 1
        while i < j:
            words[i], words[j] = words[j], words[i]
            i += 1
            j -= 1
        return " ".join(words)