#Result: 100/100
#Solved: 0:59:07
mod = 10**9+7
def fact(n):
  if n == 0:return 0
  ans = 1
  for i in range(2, n+1):
    ans *= i
    ans %= mod
  return ans
x, n = [int(x) for x in input().split()]
if n > 5: print(1)
else: print(pow(x, fact(n), 10))