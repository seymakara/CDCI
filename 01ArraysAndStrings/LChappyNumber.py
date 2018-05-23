# Write an algorithm to determine if a number is "happy".
# A happy number is a number defined by the following process: Starting with any positive integer, 
# replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), 
# or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

# Input: 19
# Output: true
# Explanation: 
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1

class Solution(object):
    def isHappy(self, n):
        nums = set() # A set is an unordered collection with no duplicate elements. 
        while n != 1:
            n = sum([int(i) ** 2 for i in str(n)]) # sayinin (sayinin karakterlerini dolasabilmek icin onu string e cevir) rakamlarinin karesini alip bir listeye koy. Karelerin toplamini al.
            if n in nums: #Eger kendini tekrar etmeye basladiysa, 1 e ulasamayacak demektir
                return False
            else:
                nums.add(n)
        else: 
            return True