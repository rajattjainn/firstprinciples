# Leet Code Problem 1768: https://leetcode.com/problems/merge-strings-alternately/?envType=study-plan-v2&envId=leetcode-75

def alternate(word1, word2):
    min_len = len(word1) if len(word1) < len(word2) else len(word2)
    
    combined_str = ""
    for i in range (min_len):
        combined_str = combined_str + word1[i] + word2[i]
    
    remaining_str = word1[min_len:] if len(word1) > len(word2) else word2[min_len:]
    combined_str = combined_str + remaining_str

    return combined_str
 
print (alternate("abc", "def"))

# def alternate(word1, word2):
#     len1 = len(word1)
#     len2 = len(word2)
    
#     if len1>len2:
#         big = word1
#         small = word2
#     else:
#         big = word2
#         small = word1
#     combined_str = ""
    
#     for i in range(len(small)):
#         combined_str = combined_str + word1[i] + word2[i]
#     combined_str = combined_str + big[len(small):]

#     return combined_str
