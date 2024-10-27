class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        max_depth = 0
        for para in s:
            if para == "(":
                stack.append(para)
                max_depth = max(max_depth, len(stack))
            elif para == ")":
                stack.pop()
        
        return max_depth