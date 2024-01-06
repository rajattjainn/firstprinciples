# LeetCode Problem #392: https://leetcode.com/problems/is-subsequence/?envType=study-plan-v2&envId=leetcode-75
def isSubsequence(sub, string):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """

    def parse_string(char, index, str):
        for i in range(index, len(str)):
            if char == str[i]:
                index = i + 1
                return index
        return False
    
    index = 0
    for c in sub:
        char_exists = parse_string(c, index, string)
        if char_exists == False:
            return False
        else: 
            index = char_exists
    return True


sub = "acb"
string = "ahbgdc"
print (isSubsequence(sub, string))