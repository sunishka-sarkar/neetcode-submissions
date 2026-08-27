class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        islands=0
        visited=set()
        def dfs(r,c):
            if(r<0 or c<0 or c>=cols or r>=rows or grid[r][c]=="0" or (r,c) in visited):
                return
            visited.add((r,c))
            #explore 4 dir
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1" and (r,c) not in visited:
                    islands+=1
                    dfs(r,c)
        return islands
        