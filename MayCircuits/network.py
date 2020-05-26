#Result: 15/100
#Solved: 98:30:02
from math import gcd

mod = 10**9+7
check = 212072634227239451
n, m = [int(x) for x in input().split()]
grid = [[i for i in range(m+1)] for i in range(n+1)]
for i in range(n):
  row = [int(x) for x in input().split()]
  grid[i+1] = row
  # print(grid[i+1])
dp = [1 for i in range(m)]
for i in range(n-1):
  for j in range(1, m):
    # print(grid[i][j], end = ' ')
    dp[j] += dp[j-1]
    dp[j] %= mod
  # print()
# print(dp)
print(dp[m-1] % mod)