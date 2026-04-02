def flood_fill(grid, sr, sc, target):
    original = grid[sr][sc]

    if original == target:
        return grid

    def dfs(r, c):
        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
            return
        if grid[r][c] != original:
            return

        grid[r][c] = target

        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    dfs(sr, sc)
    return grid
