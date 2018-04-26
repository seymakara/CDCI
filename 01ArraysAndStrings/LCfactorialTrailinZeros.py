#Given an integer n, return the number of trailing zeroes in n!

#Since 0 only company with 5*2, you only need to count the volume of 5 factor. (because 2 is always enough)

class Solution(object):
    def trailingZeroes(self, n):
        zeroCount = 0
        while n > 0:
            n = n // 5 
            zeroCount += n
        return zeroCount