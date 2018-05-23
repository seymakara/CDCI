# We define the Perfect Number is a positive integer that is equal to the sum of all its positive divisors except itself.

# Now, given an integer n, write a function that returns true when it is a perfect number and false when it is not.
# Example:
# Input: 28
# Output: True
# Explanation: 28 = 1 + 2 + 4 + 7 + 14

class Solution(object):
    def checkPerfectNumber(self, num):
        if num <= 1: return False
        
        sum = 1
        
        root = int(math.sqrt(num))
        
        for i in range(2, root + 1):
            if num % i== 0:
                sum += i
                if i != (num // i):
                    sum += num // i
        return sum == num 
        