#Result: 100/100
n, q = [int(x) for x in input().split()]
arr = [int(x) for x in input().split()]
 
sums = [0 for i in range(n)]
for i, x in enumerate(arr):
    num = x
    total = 0
    while num:
        total += num%10
        num//=10
    sums[i] = total
 
for i in range(q):
  index = int(input())
  index -= 1
  ans = -1
  for j in range(index+1, n):
    if sums[j] < sums[index] and arr[index] < arr[j]:
      ans = j+1
      break
  print(ans)