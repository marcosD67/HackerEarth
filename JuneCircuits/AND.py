#Result: 100/100
#Solved: 147:06:02
def solve(n):
  if n > 0:
    return n + solve(n//2)
  else: return n
limit = int(1e5)
ans = [0] + [0] + [0] + []
curr, counter = 1, 4
for i in range(3, limit+1):
    if counter < 1:
      counter = 4
      curr+=1
    ans.append(solve(curr))
    counter-=1
 
 
for tc in range(int(input())):
  n = int(input())
  print(ans[n])