#Result: 100/100
#Solved: 0:30:51
from collections import defaultdict
tc = int(input())
m = int(input())
virus = list(input())
d = defaultdict(int)

for ch in virus:
    if ch == 'C':
        d[ch]+=1
    elif ch == 'G':
        d[ch]+=1
prev_max = -1
ans = 0
for j in range(tc):
    interactions = 0
    n = int(input())
    vaccine = list(input())
    for el in vaccine:
        if el == 'C': 
            interactions += d['G']
        elif el == 'G':
            interactions += d['C']
    if j == 0:
        ans = j+1
        prev_max = interactions
    else:
        if interactions > prev_max:
            ans = j+1
            prev_max = interactions
        elif interactions == prev_max:
            ans = min(ans, j+1)
print(ans)