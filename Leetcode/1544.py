
class Solution(object):
    def makeGood(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for ch in s:
            if stack and stack[-1].lower() == ch.lower() and ((stack[-1].isupper() and ch.islower()) or (stack[-1].islower() and ch.isupper())):
                stack.pop()
            else:
                stack.append(ch)
        
        return ''.join(stack)

