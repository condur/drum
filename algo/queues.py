from collections import deque


def numIslands(grid):
    """
    Given a 2d grid map of '1's (land) and '0's (water),
    count the number of islands. An island is surrounded by water
    and is formed by connecting adjacent lands horizontally or vertically.

    You may assume all four edges of the grid are all surrounded by water.

    :type grid: List[List[str]]
    :rtype: int
    """
    directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

    def get_children(grid, i, j):
        for dx, dy in directions:
            x, y = i + dx, j + dy
            if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == "1":
                yield (x, y)

    def bfs(grid, i, j):
        q = deque()
        q.append((i, j))
        while q:
            x, y = q.popleft()
            grid[x][y] = "0"
            for child in get_children(grid, x, y):
                q.append(child)

    counter = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "1":
                bfs(grid, i, j)
                counter += 1

    return counter
