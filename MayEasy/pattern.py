#Result: 100/100
#Solved: 0:14:58

r, c, x, y = [int(x) for x in input().split()]
grid = [[0 for i in range(c)] for i in range(r)]

for i in range(r):
  for j in range(c):
    curr = max(abs((x-i)), abs((y-j)))
    print(curr, end= ' ')
  print()