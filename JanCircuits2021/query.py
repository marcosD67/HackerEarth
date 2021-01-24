#Result: 100/100
#Solved: 34:30:21
from collections import defaultdict
for tc in range(int(input())):
  n, q = [int(x) for x in input().split()]
 
  arr = [int(x) for x in input().split()]
 
  d = defaultdict(int)
 
  for x in arr:
    d[x] += 1
  rank = len(d) + 1
  # print("initial d:", d)
  for i in range(q):
    l, r = [int(x) for x in input().split()]
    l -= 1
    
    d[arr[l]] -= 1
    if not d[arr[l]]: 
      del d[arr[l]]
      rank -= 1
    if r not in d:
      rank += 1
    arr[l] = r
    d[r] += 1
 
    print(rank)

