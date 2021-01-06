#Reslt: 100/100
#Solved: 8:18:36
for tc in range(int(input())):
  n, zero, one = [int(x) for x in input().split()]
 
  arr = [int(x) for x in input().split()]
  ans = 0
 
  first, second = [], []
  for i in range(n):
    if not i or i % 2 == 0:
      first.append(1)
      second.append(0)
    else:
      first.append(0)
      second.append(1)
  
  for i in range(n):
    if arr[i] == first[i]: continue
    if arr[i]:
      ans += one
    else:
      ans += zero
  secondAns = 0 
  for i in range(n):
    if arr[i] == second[i]: continue
    if arr[i]:
      secondAns += one
    else:
      secondAns += zero
  print(min(ans, secondAns))