#Result: 9/100
#Solved: 1:27:51
for tc in range(int(input())):
  n = int(input())
  arr = [int(x) for x in input().split()]
  for i, x in enumerate(arr):
    if x == 0: print("1", end = ' ')
    else:
      subset = []
      for j in range(n):
        if j == i: continue
        subset.append(arr[j])
      
      m = len(subset)
      found = False
      for i in range(m):
        if found:break
        total_so_far = subset[i]
        if total_so_far == x:
          found = True
          break
        for j in range(i+1, m):
          
          total_so_far += subset[j]
          if total_so_far == x: 
            found = True
            break
          else:
            if total_so_far > x:
              total_so_far -= subset[j]
      print("1" if found else "0", end = ' ')
  print()