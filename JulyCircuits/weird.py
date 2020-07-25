#Result: 25/100
#Solved: 25:50:06
#Brute force attempt. Tried a 2D DP approach but it wasn't correct and only got 20pts.
n, k, m = [int(x) for x in input().split()]
arr = [int(x) for x in input().split()]
visited = [False for i in range(n)]
total, index = 0, 1
seq = set()
while index <= k:
  greatest, el = 0, 0
  for i, x in enumerate(arr):
    if not visited[i]:
      if x*(index%m) > greatest:
        greatest = x*(index%m)
        el = i
  visited[el] = True
  total += greatest
  index+=1
print(total)