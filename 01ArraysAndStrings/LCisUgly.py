# Write a program to check whether a given number is an ugly number.

# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.

# Example 1:

# Input: 6
# Output: true
# Explanation: 6 = 2 × 3

# Input: 14
# Output: false 
# Explanation: 14 is not ugly since it includes another prime factor 7.

class Solution(object):
    def isUgly(self, num):
        if num == 0:
            return False
        if num == 1:
            return True
        if num % 2 == 0:
            return self.isUgly(num/2)
        if num % 3 == 0:
            return self.isUgly(num/3)
        if num % 5 == 0:
            return self.isUgly(num/5)
        return False