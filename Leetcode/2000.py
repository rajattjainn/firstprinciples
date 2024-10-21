class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        if ch not in word:
            return word
        idx = word.index(ch)
        s1 = (lambda s:s[::-1])(word[:idx+1])
        s2 = word[idx+1:]
        return s1 + s2