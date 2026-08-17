# GFG POTD - 2026-08-17
# Min Product Subset
# Approach: Sorting + Greedy

class Solution:
    def minProd(self, arr):
        # code here

        neg = 0
        arr.sort()
        
        for num in arr:
            if num < 0:
                neg += 1
            else:
                break
        
        if arr[0] >= 0:
            return arr[0]
            
        if arr[0] < 0:
            prod = 1
            if neg % 2 != 0:
                for num in arr:
                    if num != 0:
                        prod *= num
                        
            else:
                 for i in range(len(arr)):
                     if i != neg - 1 and arr[i] != 0:
                         prod *= arr[i]
                         
            return prod
                
                
        
