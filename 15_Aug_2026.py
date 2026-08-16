# GFG POTD - 2026-08-12
# Numbers Without d as Digit
# Approach: Digit DP

class Solution:

    def countWithout(self, n: int, d: int) -> int:
        # code here
        digits = list(map(int, str(n)))
        mem = {}
            
        def solve(pos, tight, started):
            if pos == len(digits):
                return 1
                
            if ( pos, tight, started ) in mem:
                return mem[(pos, tight, started)]
                
            limit = digits[pos] if tight else 9
            
            ans = 0
            
            for digit in range(limit + 1):
                if digit == d and (started or (digit != 0)) :
                    continue
                
                new_tight = tight and ( digit == digits[pos] )
                new_started = started or (digit != 0)
                
                ans += solve(pos + 1, new_tight, new_started)
                
            mem[(pos, tight, started)] = ans
            return ans
                
        return solve(0, True, False) - 1
        
