class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        p = x
        q = 0
        
        while p >= 10:
            q *= 10
            q += p%10
            p /= 10
        return q == x/10 and p == x%10 # q checks for the front, p checks for the back.