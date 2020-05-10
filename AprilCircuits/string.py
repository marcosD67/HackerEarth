#Result: 100/100
#Solved: 13:14:53
#Uncomment to see what my code is doing
for tc in range(int(input())):
    n = int(input())
    arr = list(input())
    split, changes = 0, 0
    minimum = float('inf')
    for i in range(n+1):
      # print(arr[:split], arr[split:])
      # print(arr[split])
      if split == 0:
        for j, x in enumerate(arr[:split]):
            if x != "A":changes+=1
        for j, x in enumerate(arr[split:]):
            if x != "B":changes+=1
      else:
        if arr[split-1] == 'A': changes = max(0, changes-1)
        else:changes+=1
      # print(changes)
      minimum = min(changes, minimum)
      # print("MIN:", minimum)
      split+=1
    print(minimum)