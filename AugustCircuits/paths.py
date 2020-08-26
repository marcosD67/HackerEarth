#Result: 6.68/100
#Solved: 147:20:07
k = int(input())
arr = [0,0,1,2,4,7,11,16,25,35,48,68,92,123,164,216,282,
 367,471,604,769,975,1225,1542,1924,2395,2968,3669,
 4514,5547,6781,8280,10071,12229,14796,17881,21537,
 25902,31066,37206,44443,53021,63098,74995,88946,
 105350,124533] #From OEIS
 
n = 0
for i, x in enumerate(arr):
  if x >= k:
    m = x
    n = i
    break
 
print(n, n*(n-1)//2)
for i in range(1, n+1):
  for j in range(i+1, n+1):
    print(i, j)
    if j == n: k-=1
 
    if not k: break
  if not k: break