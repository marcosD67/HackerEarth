import sys
arr = []
n = 0
for tc in range(int(input())):
    line = [int(x) for x in input().split()]

    query = line[0]

    if query == 1:
        a, b = line[1:]
        arr.append((a, b))
        n+=1
    else:
        x = int(line[1])
        if query == 2:
            x-=1
            if 0 <= x < n:
              del arr[x]
        else:
            ans = pow(2, 100) * -1
            c = arr.copy()
            c= set(c)
            for (a, b) in c:
                ans = max(a*x + b, ans)
            print(ans)