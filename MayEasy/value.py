#Result: 100/100
#Solved: 1:47:29
#After some digging, the answer turned out to be the sum of the 2 biggest
#terms of the Fibonacci sequence smaller than n
n = int(input())
fib = [0] + [1] + []
index = 2
curr, prev = 0, 0
while True: #Dynamic Programming approach
    if fib[index-1] + fib[index-2] > n:
        curr = fib[index-1]
        prev = fib[index-2]
        break
    fib.append(fib[index-1] + fib[index-2])
    index+=1
print(curr+prev)