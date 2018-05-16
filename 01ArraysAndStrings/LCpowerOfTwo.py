# Given an integer, write a function to determine if it is a power of two.

class Solution(object):
    def isPowerOfTwo(self, n):
        if n == 0:
            return False
        
        while n % 2 == 0:
            n /= 2
            
        if n == 1:
            return True
        return False