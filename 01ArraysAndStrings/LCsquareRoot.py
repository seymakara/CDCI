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