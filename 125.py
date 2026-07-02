#Valid Palindrome
s = "ma   .,LayAlam"
res = ""
cleaned = ''.join(ch.lower() for ch in s if ch.isalnum())
print(cleaned)
for i in range(len(cleaned)-1, -1, -1):
    res += cleaned[i]
if res == cleaned:
    print("true")
else:
    print("false")
    