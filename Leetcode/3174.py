class Solution(object):
    def clearDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        stack = []
        for i in s:
            if not stack or not i.isnumeric():
                stack.append(i)
            else:
                if stack: stack.pop()

        return ''.join(stack)