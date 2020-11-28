#Result: 0/100 TLE
mod = int(1e9+21)
from math import factorial as f

def binomial(n, k):
  n %= mod
  k %= mod
  nf, kf = f(n)%mod, f(k)%mod
  return nf // (kf * (f((n-k)%mod)))

def I(n):
    if not n % 4:
        return 1
    if n % 4 == 1: return 0
    if n % 4 == 2: return -1
    if n % 4 == 3: return 0
def solve(n, k):
    ans = 0

    for s in range(n+1):
        for r in range(s, n+1):
            for t in range(s+1):
                ans += (binomial(n, r) * binomial(r,s) * binomial(s,t) * t * pow((3*(k**2)), t/2) * I(t))/(s+1)
                
                ans %= mod
    return ans
for tc in range(int(input())):
    l, r = [int(x) for x in input().split()]
    if r > l:
        print(0)
        continue
    print(solve(l, r))