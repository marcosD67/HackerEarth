#Result: 100/100
#Solved: 38:29:28
#Binary Search problem!
import sys
n, m = [int(x) for x in input().split()]
arr = [int(x) for x in input().split()]
planes = [int(x) for x in input().split()]
planes.sort()
if max(planes) < max(arr):print(-1)
elif max(arr) < max(planes):print(1)
else:
    planesTaken = []
    time, index = 0, 0
    found = False
    curr = 0
    while index != n:
        low = 0
        high = m-1
        found = False #assume impossible
        while low <= high:
            mid = (low+high)//2
            if planes[mid] >= arr[index] and mid not in planesTaken:
                planesTaken.append(mid)
                found = True
                break
            else: 
                low = mid + 1
        if arr[index] <= planes[curr] < planes[mid] and curr not in planesTaken:
            planesTaken.pop(-1)
            planesTaken.append(curr)
            curr+=1
            found = True
        if found:
            index+=1
            if index == n-1:
                time+=1
        else: 
            time+=1
            if index != n:
                time+=1 #still need more trips
            planesTaken.clear()
    print(time)