# GFG POTD - 2026-08-19
# Triplets with Sum in Range
# Approach: Sorting

class Solution:
   
    def countTriplets(self, arr: list[int], l: int, r: int) -> int:
        arr.sort()
        n = len(arr)

        def count(x):
            ans = 0

            for i in range(n - 2):
                left = i + 1
                right = n - 1

                while left < right:
                    total = arr[i] + arr[left] + arr[right]

                    if total <= x:
                        ans += right - left
                        left += 1
                    else:
                        right -= 1

            return ans

        return count(r) - count(l - 1)
