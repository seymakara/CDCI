#Compute and return the square root of x, where x is guaranteed to be a non-negative integer.
#Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

class Solution(object):
    def mySqrt(self, x):
        start = 0
        end = x
        while start + 1 < end:
            mid = start + (end - start)/2
            if mid * mid == x:
                return mid
            elif mid * mid > x:
                end = mid
            else:
                start = mid
        if end * end == x:
            return int(end)
        else:
            return int(start)