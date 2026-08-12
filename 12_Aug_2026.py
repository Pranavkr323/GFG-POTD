# GFG POTD - 2026-08-12
# Adventure in a Maze
# Approach: 2D DP + Recursion + Memoization

class Solution:
    def findWays(self, grid):
        # code here
        n = len(grid)
        MOD = 10**9 + 7
        mem = [[-1]*(n + 1) for _ in range (n + 1)]
        def dp(i,j):
            
            if i >= n or j >= n:
                return 0, 0
            
            if (i, j) == (n-1, n-1):
                return (1, grid[i][j])
                
            if mem[i][j] != -1:
                return mem[i][j]
            
            if grid[i][j] == 1:
                
                paths, adventure = dp(i, j + 1)
                
                if paths == 0:
                    return 0, 0
                    
                mem[i][j] = (paths, adventure + grid[i][j])
                return mem[i][j]
                    
            elif grid[i][j] == 2:
                
                
                paths, adventure = dp(i + 1, j)
                
                if paths == 0:
                    mem[i][j] = (0, 0)
                    return mem[i][j]
                mem[i][j] = (paths, adventure + grid[i][j])
                return mem[i][j]
            
            else:
                
                right_paths, right_adv = dp(i, j + 1)
                down_paths, down_adv = dp(i + 1, j)
                total_paths = right_paths + down_paths
                
                if total_paths == 0:
                    mem[i][j] = (0, 0)
                    return mem[i][j]
                    
                if right_paths == 0:
                    max_adv = down_adv
                
                elif down_paths == 0:
                    max_adv = right_adv
                
                else:    
                    max_adv = max(right_adv, down_adv)
                
                mem[i][j] = total_paths, max_adv + grid[i][j]
                return mem[i][j]
                
        paths, adventure = dp(0,0)
        return [paths % MOD, adventure]

