#Result: 8/100 TLE
#on the right track, but ran the subset sum function too much
def subsetSum(arr, n, total):
    subset = [[False for j in range(total + 1)] for i in range(3)] 
    for i in range(n + 1): 
        for j in range(total + 1): 
            # A subset with sum 0 is always possible  
            if (j == 0): 
                subset[i % 2][j] = True
   
            # If there exists no element no sum  
            # is possible  
            elif (i == 0): 
                subset[i % 2][j] = False
            elif (arr[i - 1] <= j): 
                subset[i % 2][j] = subset[(i + 1) % 2][j - arr[i - 1]] or subset[(i + 1)  
                                                                               % 2][j] 
            else: 
                subset[i % 2][j] = subset[(i + 1) % 2][j] 
                  
    return subset[n % 2][total]
for tc in range(int(input())):
  n = int(input())
  arr = [int(x) for x in input().split()]
  ans = []
  for x in arr:
    power = 2
    found = False
    while power < 4:
      target = x**power
      total = subsetSum(arr, n, target)
      if total:
        found = True
        break
      power+=1
    if found:
      ans.append(1)
    else:
      ans.append(0)
  print(*ans)