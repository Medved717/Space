from collections import defaultdict

d = defaultdict(int)
text = "aabbcc"

for ch in text:
    d[ch]

result = d['a'] + d['b'] + d['c']
print(result)