class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        valid = ""
        for i in range (len(s)):
            char = s[i]
            if char == "(":
                valid = valid + char
                stack.append(len(valid) - 1)
            elif char == ")":
                if stack and valid[stack.pop()] == "(":
                    valid = valid + char
            else:
                valid = valid + char
    
        while stack:
            idx = stack.pop()
            valid = valid[:idx] + valid[idx+1:]

        return valid
    
s = "lee(t(c)o)de)"
print(Solution().minRemoveToMakeValid(s))