# Given a positive integer num, write a function which returns True if num is a perfect square else False.

# Note: Do not use any built-in library function such as sqrt.

# Example 1:

# Input: 16
# Returns: True
# Example 2:

# Input: 14
# Returns: False

class Solution(object):
    def isPerfectSquare(self, num):
        l = 0
        r = num
        
        while l <= r:
            mid = (l+r) / 2

            if mid * mid == num:
                return True
            
            elif mid * mid < num:
                l = mid + 1
            else:
                r = mid -1       
        return False
    
    num 16
    l 0 4
    r 16 7 6 5
    mid 8 3