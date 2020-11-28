#Result: 100/100
n = int(input())
if not n:
  print(0)
  print(0)
if n == 1:
    print(-1)
    print(-1)
elif n == 2:
    print(2)
    print(2, 1)
    print(2)
    print(2, 1)
elif n == 3:
    print(4)
    print(3, 1, 2)
    print(4)
    print(2, 3, 1)
elif n == 5:
    print('''6
2 1 5 3 4
12
5 3 4 2 1''')
elif n == 7:
    print('''8
2 1 4 3 7 5 6
24
7 6 4 5 3 2 1''')
else:
    if n % 2 == 0:
        #min below
        arr = [0 for i in range(n)]
        arr[0] = 2
        arr[1] = 1
        arr[2] = 4
        arr[3] = 3
        minTotal = 0
        start = 6
        for i in range(4, n-1, 2):
            arr[i] = start
            arr[i+1] = start-1
            start+=2
        for i in range(1, n+1):
            minTotal += abs(arr[i-1]-i)
        print(minTotal)
        print(*arr)
        #max below
        arr = [i for i in range(n, 0, -1)]
        maxTotal = 0
        for i in range(1, n+1):
            maxTotal += abs(arr[i-1]-i)
        print(maxTotal)
        print(*arr)
    else:
        arr = [0 for i in range(n)]
        arr[0] = 2
        arr[1] = 1
        arr[2] = 4
        arr[3] = 3
        minTotal = 0
        start = 6
        j = 4
        while j < n:
            if j < n-1:
                arr[j] = start
                arr[j+1] = start-1
            else:
                arr[j] = start
            start += 2
            if start == n-1:
                j += 4
            else:
                j += 2
        start = n-2
        for i in range(n-1, 0, -1):
            if not arr[i]: 
                arr[i] = start
                start+=2
        for i in range(1, n+1):
            minTotal += abs(arr[i-1]-i)
        print(minTotal)
        print(*arr)
        #max below
        maxTotal = 0
        arr = [i for i in range(n, 0, -1)]
        arr[n//2], arr[n//2-1] = arr[n//2-1], arr[n//2]
        for i in range(1, n+1):
            maxTotal += abs(arr[i-1]-i)
        print(maxTotal)
        print(*arr)