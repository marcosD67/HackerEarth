#Result: 6/100, WA
#Naive solution
n, m = [int(x) for x in input().split()]
graph = []
 
for i in range(n):
  row = list(input())
  # graph.append(row)
  print(*row, sep = '')