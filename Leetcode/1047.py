class Solution(object):
    def removeDuplicates(self, s:str):
        stack = []

        for ch in s:
            if not stack or stack[-1] != ch:
                stack.append(ch)
            elif stack[-1] == ch:
                stack.pop()

        return ''.join(stack)


str = "azxxzy"

print(Solution().removeDuplicates(str))