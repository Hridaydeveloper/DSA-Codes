# Leetcode : 14. Longest Common Prefix
s = ["flower","flow", "flight"]
if len(s) == 0:
    print("")
    
base = s[0]
for i in range(len(s)):
    for ch in s[1:]:
        if i == len(ch) or base[i] != ch[i]:
            print(base[0:i])
        if i == len(s):
            break
print(base)
 