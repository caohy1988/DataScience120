def getBiggestRegion(grid, n, m):
    count_max = 0
    count_temp = 0
    for i in range(n):
        for j in range(m):
            count_temp = 0
            stack = []
            if grid[i][j] == 1:
                count_temp += 1
                grid[i][j] = 0
                stack.append((i,j))
            while len(stack) > 0:
                (i, j) = stack.pop()
                if  i < (n-1) and  i > 0 and j < (m-1) and j > 0:
                    if grid[i+1][j] == 1:
                        stack.append((i+1, j))
                        count_temp += 1
                        grid[i+1][j] = 0
                    if grid[i][j+1] == 1:
                        stack.append((i, j+1))
                        count_temp += 1
                        grid[i][j+1] = 0
                    if grid[i-1][j] == 1:
                        stack.append((i-1, j))
                        count_temp += 1
                        grid[i-1][j+1] = 0
                    if grid[i][j-1] == 1:
                        stack.append((i, j-1))
                        count_temp += 1
                        grid[i][j-1] = 0

                elif i == (n-1):
                    if j == 0:
                        if grid[i][j+1] == 1:
                            stack.append((i, j+1))
                            count_temp += 1
                            grid[i][j+1] = 0
                        if grid[i-1][j] == 1:
                            stack.append((i-1, j))
                            count_temp += 1
                            grid[i-1][j] = 0

                    elif j < m - 1:
                        if grid[i][j+1] == 1:
                            stack.append((i, j+1))
                            count_temp += 1
                            grid[i][j+1] = 0
                        if grid[i-1][j] == 1:
                            stack.append((i-1, j))
                            count_temp += 1
                            grid[i-1][j] = 0
                        if grid[i][j-1] == 1:
                            stack.append((i, j-1))
                            count_temp += 1
                            grid[i][j-1] = 0
                    else:
                        if grid[i][j-1] == 1:
                            stack.append((i, j-1))
                            count_temp += 1
                            grid[i][j-1] = 0
                        if grid[i-1][j] == 1:
                            stack.append((i-1, j))
                            count_temp += 1
                            grid[i-1][j] = 0




                elif j == (m-1):
                    if i == 0:
                        if grid[i+1][j] == 1:
                            count_temp += 1
                            stack.append((i+1, j))
                            grid[i+1][j] = 0
                        if grid[i][j-1] == 1:
                            count_temp += 1
                            stack.append((i, j-1))
                            grid[i][j-1] = 0
                    elif i < n - 1:
                        if grid[i+1][j] == 1:
                            count_temp += 1
                            stack.append((i+1, j))
                            grid[i+1][j] = 0
                        if grid[i][j-1] == 1:
                            count_temp += 1
                            stack.append((i, j-1))
                            grid[i][j-1] = 0
                        if grid[i-1][j] == 1:
                            count_temp += 1
                            stack.append((i-1, j))
                            grid[i-1][j] = 0
                    else:
                        if grid[i][j-1] == 1:
                            stack.append((i, j-1))
                            count_temp += 1
                            grid[i][j-1] = 0
                        if grid[i-1][j] == 1:
                            stack.append((i-1, j))
                            count_temp += 1
                            grid[i-1][j] = 0
                elif j == 0:
                    if i == 0:
                        if grid[i+1][j] == 1:
                            count_temp += 1
                            stack.append((i+1, j))
                            grid[i+1][j] = 0
                        if grid[i][j+1] == 1:
                            count_temp += 1
                            stack.append((i, j+1))
                            grid[i][j+1] = 0
                    elif i < n - 1:
                        if grid[i+1][j] == 1:
                            count_temp += 1
                            stack.append((i+1, j))
                            grid[i+1][j] = 0
                        if grid[i][j+1] == 1:
                            count_temp += 1
                            stack.append((i, j+1))
                            grid[i][j+1] = 0
                        if grid[i-1][j] == 1:
                            count_temp += 1
                            stack.append((i-1, j))
                            grid[i-1][j] = 0
                    else:
                        if grid[i][j-1] == 1:
                            stack.append((i, j-1))
                            count_temp += 1
                            grid[i][j-1] = 0
                        if grid[i-1][j] == 1:
                            stack.append((i-1, j))
                            count_temp += 1
                            grid[i-1][j] = 0
                elif i == 0:
                    if j == 0:
                        if grid[i+1][j] == 1:
                            count_temp += 1
                            stack.append((i+1, j))
                            grid[i+1][j] = 0
                        if grid[i][j+1] == 1:
                            count_temp += 1
                            stack.append((i, j+1))
                            grid[i][j+1] = 0
                    elif j < m - 1:
                        if grid[i+1][j] == 1:
                            count_temp += 1
                            stack.append((i+1, j))
                            grid[i+1][j] = 0
                        if grid[i][j+1] == 1:
                            count_temp += 1
                            stack.append((i, j+1))
                            grid[i][j+1] = 0
                        if grid[i][j-1] == 1:
                            count_temp += 1
                            stack.append((i, j-1))
                            grid[i][j-1] = 0
                    else:
                        if grid[i][j-1] == 1:
                            stack.append((i, j+1))
                            count_temp += 1
                            grid[i][j-1] = 0
                        if grid[i+1][j] == 1:
                            stack.append((i+1, j))
                            count_temp += 1
                            grid[i+1][j] = 0


            if count_temp > count_max:
                count_max = count_temp
    return count_max





n = int(input().strip())
m = int(input().strip())
grid = []
for grid_i in range(n):
    grid_t = list(map(int, input().strip().split(' ')))
    grid.append(grid_t)
print(getBiggestRegion(grid, n, m))
