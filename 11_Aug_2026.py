# GFG POTD - 2026-08-11
# Largest Odd Squares with Limited 1s
# Approach: 2D Prefix Sum + Binary Search

class Solution:
    def largestSquare(self, mat: list[list[int]], queries: list[list[int]], k: int) -> list[int]:
        # code here
        def prefix_sum(matrix):
            n = len(matrix)
            m = len(matrix[0])
            prefix = [[0]*(m+1) for _ in range(n+1)]
            for row in range(n):
                for col in range(m):
                    prefix[row+1][col+1] = (matrix[row][col] +
                                        prefix[row][col+1] +
                                        prefix[row+1][col] -
                                        prefix[row][col])
                                        
            return prefix
            
        def get_ones(pref, top, left, bottom, right):
            ones = (pref[bottom+1][right+1] -
                    pref[top][right+1] -
                    pref[bottom+1][left] + 
                    pref[top][left])
                    
            return ones
            
        ans = []
        n = len(mat)
        m = len(mat[0])
        pref = prefix_sum(mat)
        for i,j in queries:
            up = i
            left = j
            down = n-1-i
            right = m-1-j
            max_radius = min(up,left,down,right)
            
            low = 0
            high = max_radius
            
            
            while low <= high:
                mid = (low+high)//2
                
                top = i-mid
                bottom = i+mid
                left = j-mid
                right = j+mid
                
                number_of_ones = get_ones(pref,top,left,bottom,right)
                
                if number_of_ones <= k:
                    low = mid + 1
                    
                else:
                    high = mid - 1
                    
                
            ans.append(2*high+1)
            
        return ans
                    
        
        
