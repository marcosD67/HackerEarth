#Result: 100/100
#Solved: 133:39:01
#Slightly modified Josephus problem
for tc in range(int(input())):
    n, k = [int(x) for x in input().split()]
    p = 1
    start = 2 * (k+1)
    while start > n: start -= n
    while p <= n:
        p *= 2
    ans = (2*n) - p + 1
    if start > 2:
        ans += (start-2)
    elif start == 1 and n > 1:
        ans-=1
    while ans > n:ans-=n
    print(ans)