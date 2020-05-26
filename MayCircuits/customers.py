#Result: 51.69/100
#Solved: 1:31:55
n, k = [int(x) for x in input().split()]
arrivals = [int(x) for x in input().split()]
time = [int(x) for x in input().split()]
satisfaction = [int(x) for x in input().split()]
 
if k >= n:
  print(*arrivals)
else:
  ans = []
  chefs = []
  for i in range(k):
    ans.append(arrivals[i])
    chefs.append(arrivals[i] + time[i])
 
  
  for i in range(k, n):
    minEl = min(chefs)
    if arrivals[i] < minEl:
      ans.append(minEl)
      pos = chefs.index(minEl)
      chefs[pos] = (arrivals[i] + abs(arrivals[i] - minEl) + time[i])
    else:
      ans.append(arrivals[i])
      pos = chefs.index(minEl)
      chefs[pos] = (arrivals[i] + time[i])
  print(*ans)