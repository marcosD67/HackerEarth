#Result: 100/100
#Solved: 0:27:11
def sq(n):
    return n*n
def add(n):
    if n == 0:return 0
    if n%2 == 1:
        return sq((n+1)//2) + add(n//2)
    else:
        return sq(n//2) + add(n//2)
def divSum(l, r, m):
    return (add(r) - add(l-1)) % m
for tc in range(int(input())):
    n, m = [int(x) for x in input().split()]
    print(divSum(1, n, m))