class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        p = x
        q = 0
        
        while p >= 1:
            q *= 10
            q += p%10
            p /= 10
        return q == x