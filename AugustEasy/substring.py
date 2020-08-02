#Result: 15/100
#Solved: 1:13:24
from collections import defaultdict
 
d = defaultdict(int)
s = list(input())
n = len(s)
max_freq = 0
ans = ""
for i in range(n):
    substr = ''
    for j in range(i, n):
        substr += s[j]
        d[substr] += 1
        if max_freq < d[substr]:
            max_freq = d[substr]
            ans = substr
        elif max_freq == d[substr]:
            if len(ans) < len(substr):
                ans = substr
print(ans)