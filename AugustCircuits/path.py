#Result: 100/100
#Solved: 99:45:55
#DFS and Backtrack to find all paths from source to destination
from collections import defaultdict
 
keep = defaultdict(int)
 
n, m = [int(x) for x in input().split()]
a, b = [int(x) for x in input().split()]
visited = [False for i in range(n+1)]
adj = [[] for i in range(n+1)]
ans, paths = 0, 0
for i in range(m):
  u, v = [int(x) for x in input().split()]
  adj[u].append(v)
  adj[v].append(u)
 
def check(path): #populate map 
  for (x, y) in path:
    keep[(x, y)] += 1
def dfs(source, destination, path, parent):
  visited[source] = True
  path.append((source, parent)) #keep track of current path
  global paths #global variable counter
  if source == destination: #if path is complete
    check(path)
    paths+=1
  else:
    for other in adj[source]:
      if not visited[other]:
        dfs(other, destination, path, source)
  path.pop() #backtracking
  visited[source] = False #backtracking
 
dfs(a, b, [], 0)
 
for k, v in keep.items(): #map keeps count in how many paths each edge appears in
  if k[1] == 0: continue #ignore starting node 
  if v == paths:
    ans+=1
print(ans)