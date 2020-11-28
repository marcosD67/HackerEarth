#Result: 20/100
n = int(input())
from collections import defaultdict 
graph = [set() for i in range(n+1)]
 
for tc in range(n):
  x, y = [int(s) for s in input().split()]
  graph[tc+1].add(abs(x+y))
q = defaultdict(int)
for tc in range(int(input())):
  line = list(input().split())
  if line[0] == '+':
    i, x, y = line[1:]
    i, x, y = int(i), int(x), int(y)
    graph[i].add(abs(x+y))
  else:
    l, r, k = line[1:]
    l, r, k = int(l), int(r), int(k)
    if tuple((l,r,k)) in q:
      print(q[tuple((l,r,k))])
      continue
    powers = []
    for j in range(l, r+1):
      for x in graph[j]:
        powers.append((x-k)**2)
    ans = float('-inf')
    m = len(powers)
    for j in range(m):
      for k in range(j+1, m):
        ans = max(ans, abs(powers[j] - powers[k]))
    q[tuple((l,r,k))] = ans
    print(ans)