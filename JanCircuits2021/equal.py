#Result: 100/100
#Solved: 155:02:46

#Count inversions (if they're both the same parity, then YES)
# However, if they have a character in common (occurence > 1) then it's always YES
# If none of the rules above apply, then NO
def mergeSort(arr, n): 
    temp_arr = [0]*n 
    return _mergeSort(arr, temp_arr, 0, n-1) 
  
  
def _mergeSort(arr, temp_arr, left, right): 
 
    inv_count = 0
  
    if left < right: 
  
        mid = (left + right)//2
  
        inv_count += _mergeSort(arr, temp_arr,  
                                    left, mid) 
        inv_count += _mergeSort(arr, temp_arr,  
                                  mid + 1, right) 
        inv_count += merge(arr, temp_arr, left, mid, right) 
    return inv_count 
  
def merge(arr, temp_arr, left, mid, right): 
    i = left     # Starting index of left subarray 
    j = mid + 1 # Starting index of right subarray 
    k = left     # Starting index of to be sorted subarray 
    inv_count = 0
  
    while i <= mid and j <= right: 
        if arr[i] <= arr[j]: 
            temp_arr[k] = arr[i] 
            k += 1
            i += 1
        else: 
            temp_arr[k] = arr[j] 
            inv_count += (mid-i + 1) 
            k += 1
            j += 1
  
    while i <= mid: 
        temp_arr[k] = arr[i] 
        k += 1
        i += 1
  
    while j <= right: 
        temp_arr[k] = arr[j] 
        k += 1
        j += 1
  
    for loop_var in range(left, right + 1): 
        arr[loop_var] = temp_arr[loop_var] 
          
    return inv_count 
 
from collections import Counter
for tc in range(int(input())):
  n = int(input())
  s1 = list(input())
  s2 = list(input())
  ans1 = mergeSort(s1, n)
  ans2 = mergeSort(s2, n)
  if ''.join(s1) != ''.join(s2):
    print("NO")
    continue
  else:
    if n < 3:
      print("NO")
      continue
    c = Counter(s1)
    d = Counter(s2)
    able = False
    for k, v in c.items():
      if k in d.keys():
        if v == d[k] and v > 1:
          able = True
          break
    if able:
      print("YES")
    elif ((ans1 ^ ans2) & 1) == 0:
      print("YES")
    else:
      print("NO")