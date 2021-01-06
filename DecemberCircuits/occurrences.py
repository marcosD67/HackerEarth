#Result: 100/100
#Solved: 0:37:25
from collections import defaultdict
for tc in range(int(input())):
  n = int(input())
  arr = [int(x) for x in input().split()]
 
  d = defaultdict(list)
 
  for i, x in enumerate(arr):
    d[x].append(i+1)
  ans = 0
 
  for k, v in d.items():
    ans += abs(v[-1] - v[0])
  print(ans) 