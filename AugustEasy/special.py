#Result: 100/100
#Solved: 0:57:58
import itertools
from math import gcd
n = int(input())
 
digits = len(str(n))
 
nums = []
for j in range(1, digits+1):
    for i in itertools.product(['4', '7'], repeat=j):
        val = int(''.join(i))
        if val <= n:
            nums.append(val)
ans = 0
m = len(nums)
for i in range(m):
    for j in range(i+1, m):
        if gcd(nums[i], nums[j]) == 1:
            ans+=1
print(ans)