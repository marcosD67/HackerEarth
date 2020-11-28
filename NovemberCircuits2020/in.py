#result: 100/100
n = int(input())
arr = [int(x) for x in input().split()]
 
ptr = 0
ans = 0
left= 0 
it = 0
while ptr < n:
  # print(arr[ptr])
  if ptr + arr[ptr] >= n:
    left = n-ptr-1
    break
  ptr += arr[ptr]+1
  it += 1
# print(left)
# print(it)
try:
  ans = (arr[ptr] - left) + ((n-1)-it)
except:
  ans = (n-it)
print(ans)