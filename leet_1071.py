# Leet Code Problem 1071: https://leetcode.com/problems/greatest-common-divisor-of-strings/

def gcd(str1, str2):
    initial = str1 if len(str1) < len(str2) else str2
    gcd = ""
    for i in reversed(range(len(initial))):
        gcd_tmp = initial[0:i+1]
        c1 = int(len(str1)/len(gcd_tmp))
        c2 = int(len(str2)/len(gcd_tmp))
        if str1 == (gcd_tmp*c1) and str2 == gcd_tmp*c2:
            gcd = gcd_tmp
            break 
    return gcd

print(gcd("LEET", "ABAB"))

