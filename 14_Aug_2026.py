# GFG POTD - 2026-08-14
# Problem - Subset Sum on Generated Sequence
# Approach: Greedy on Superincreasing Sequence

class Solution:
    def isPossible(self, arr, s, x):
        seq = [s]
        total = s
    
        for num in arr:
            val = total + num
    
            if val > x:
                break
    
            seq.append(val)
            total += val
    
        remaining = x
    
        for num in reversed(seq):
            if num <= remaining:
                remaining -= num
    
            if remaining == 0:
                return True
    
        return False
