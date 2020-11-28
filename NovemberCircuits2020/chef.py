#result: 55.461/100
#CPU scheduling approximation problem

from heapq import heappush, heappop

class Order:
    def __init__(self, index, arrival, prep, anger):
        self.index = index
        self.arrival = arrival
        self.prep = prep
        self.anger = anger
        
    def __lt__(self, other):
        cost1Self = self.prep * self.anger
        cost1other = (max(self.arrival + self.prep, other.arrival) - other.arrival) * other.anger + other.prep * other.anger
        cost1 = cost1Self + cost1other

        cost2other = other.prep * other.anger
        cost2self = (max(other.arrival + other.prep, self.arrival) - self.arrival) * self.anger + self.prep * self.anger
        cost2 = cost2self + cost2other
        return cost1 < cost2

n, k = [int(x) for x in input().split()]
arrivals = [int(x) for x in input().split()]
time = [int(x) for x in input().split()]
anger = [int(x) for x in input().split()]

orders = []

for index, (a,b,c) in enumerate(zip(arrivals, time, anger), 1):
    orders.append(Order(index,a,b,c))
contracts = [int(x) for x in input().split()]

orders = sorted(orders)
def solve(orders, contracts, n, k):
    ans = [0 for i in range(n)]
    chefs = []
    for chef in range(k):
        heappush(chefs, (0, contracts[chef], chef+1))

    for order in orders:
        T, contractTime, chef = heappop(chefs)

        while contractTime <= 0:
            T, contractTime, chef = heappop(chefs)

        T = max(T, order.arrival)
        ans[order.index-1] = (T, chef)
        heappush(chefs, (T + order.prep+1, contractTime-order.prep, chef))
    return ans

res = solve(orders, contracts, n, k)
for x in res:
    print(*x)