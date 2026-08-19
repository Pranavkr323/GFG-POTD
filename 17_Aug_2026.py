# GFG POTD - 2026-08-17
# Snake and Ladder Problem
# Approach: BFS

from collections import deque
class Solution:
    def minThrows(self, n, lad, sn):
        # code here
        visited = {1}
        sn_lad = {}
        k = len(lad)
        m = len(sn)
        
        for i in range(0, k, 2):
            sn_lad[lad[i]] = lad[i+1]
            
        for i in range(0, m, 2):
            sn_lad[sn[i]] = sn[i+1]
            
        queue = deque([(1,0)])
        
        while queue:
            cell, throws = queue.popleft()
            
            for dice in range(1,7):
                next_cell = cell + dice
                
                if next_cell > n * n:
                    continue
                
                if next_cell in sn_lad:
                    next_cell = sn_lad[next_cell]
                    
                if next_cell == n * n:
                    return throws + 1
                    
                if next_cell not in visited:
                    visited.add(next_cell)
                    
                    queue.append((next_cell, throws + 1))
        return -1
