count = 0
def isSafe(x, y, grid, visited):
        if 0 <= x < n and 0 <= y < m:
            if not visited[x][y] and grid[x][y] == '.':
                return True
        return False
def dfs(x, y, grid, visited):
    global count
    visited[x][y] = True
    for row, col in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        if isSafe(x+row, y+col, grid, visited):
            count+=1
            dfs(x+row, y+col, grid, visited)
    
for tc in range(int(input())):
    n, m = [int(x) for x in input().split()]

    areas = []
    grid = []

    for i in range(n):
        row = [x for x in input()]
        grid.append(row)
    visited = [[False for i in range(m)] for i in range(n)]
   
    ans = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '#': continue
            if not visited[i][j]:
                count = 1
                ans += 1
                dfs(i, j, grid, visited)
                areas.append(count)
                
    print(ans)
    print(*areas)