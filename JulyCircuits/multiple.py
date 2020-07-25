#Result: 100/100
#Solved: 39:12:25
#Solution based on prime factorization to find LCM, so making a prime sieve
#that was each index's smallest prime factor made the code fast enough.
MAX = 10**6+1
 
prime = [0 for i in range(MAX)]
max_map = dict()
 
 
def sieve():
  prime[0], prime[1] = 1, 1
 
  for i in range(2, MAX):
    if prime[i] == 0:
      for j in range(i*2, MAX, i):
        if prime[j] == 0:
          prime[j] = i
      prime[i] = i
 
def lcm(arr, n, m):
  seen = set()
  for i in range(n):
    temp = dict()
 
    num = arr[i]
    if num in seen: continue
    seen.add(num)
    while num > 1:
      factor = prime[num]
 
      if factor in temp.keys():
        temp[factor] +=1
      else:
        temp[factor] = 1
      
      num //= factor
    for j in temp:
      if j in max_map.keys():
        max_map[j] = max(max_map[j], temp[j])
      else:
        max_map[j] = temp[j]
    
  ans = 1
 
  for i in max_map:
    ans = (ans * pow(i, max_map[i], m))%m
  return ans
 
sieve()
for tc in range(int(input())):
  n, m, k = [int(x) for x in input().split()]
  arr = [int(x) for x in input().split()]
  ans = lcm(arr, n, m)
  print(pow(ans, k, m))
  max_map.clear()