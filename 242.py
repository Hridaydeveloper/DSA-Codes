s = "anagram"
t = "nagarama"
res = {}
ress = {}
if len(s) != len(t):
    print("false")
    exit()
for i in range(len(s)):
    n = s[i]
    res[n] = res.get(n, 0) + 1
for i in range(len(t)):
    n = t[i]
    ress[n] = ress.get(n, 0) + 1
if res == ress:
    print("true")
else:
    print("false")