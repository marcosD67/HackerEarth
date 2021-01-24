#Result: 100/100
#Solved: 30:13:14
from collections import Counter
for tc in range(int(input())):
    n = int(input())
    s1 = list(input())
    s2 = list(input())
 
    c, d = Counter(s1), Counter(s2)
    able = True
    first, second = 1, 1
    for k, v in c.items():
        diff = abs(v - d[k])
        if diff > 1: able = False
        elif diff == 1:
          if v > d[k]:
            if not second: able = False
            second -= 1
          else:
            if not first: able = False
            first -= 1
    print("YES" if able else "NO")