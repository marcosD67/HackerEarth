#Result: 100/100
#Solved: 135:18:27
#Digit Dynamic Programming Solution (python3 version, submitted after C++ version)
def count(pos, cnt, tight, num, k, dp):
  if pos == len(num):
    if cnt == len(num): return 1
    return 0
  
  if dp[pos][cnt][tight] != -1:
    return dp[pos][cnt][tight]
 
  ans = 0
 
  limit = 9 if tight else num[pos]
 
  for dig in range(limit + 1):
    currCount = cnt
 
    if dig % k == 0: 
      currCount+=1
      currTight = tight
 
      if dig < num[pos]:
        currTight = 1
      
      ans += count(pos+1, currCount, currTight, num, k, dp)
  
  dp[pos][cnt][tight] = ans
  return dp[pos][cnt][tight]
 
 
def solve(n, k):
  dp = [[[-1, -1] for x in range(18)]  
                    for y in range(18)] 
 
  num = []
 
  while n:
    num.append(n%10)
    n //= 10
  num.reverse()
 
  return count(0,0,0,num,k,dp)
for tc in range(int(input())):
  l, r, k = [int(x) for x in input().split()]
 
  ans = solve(r, k) - solve(l-1, k)
  print(ans)