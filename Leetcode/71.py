class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        individual = path.split("/")
        stack = []
        for i in range(len(individual)):
            if individual[i] == "..":
                if stack: stack.pop()  
            elif individual[i] == "." or individual[i] == "/" or individual[i] == "" :
                continue
            else:
                stack.append(individual[i])

        final_path = ""
        for i in range(len(stack)):
            final_path = final_path + "/" + stack[i]
        
        return final_path if final_path else "/"

path = "/.../a/../b/c/../d/./"
print(Solution().simplifyPath(path))