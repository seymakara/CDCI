# You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.

# Given n, find the total number of full staircase rows that can be formed.

# n is a non-negative integer and fits within the range of a 32-bit signed integer.

# Example 1:

# n = 5

# The coins can form the following rows:
# ¤
# ¤ ¤
# ¤ ¤

# Because the 3rd row is incomplete, we return 2.
# Example 2:

# n = 8

# The coins can form the following rows:
# ¤
# ¤ ¤
# ¤ ¤ ¤
# ¤ ¤

# Because the 4th row is incomplete, we return 3.


class Solution(object):
    def arrangeCoins(self, n):
        row = 0
        
        while n >= 0: # Sifirlandiktan sonra bir kere daha devam edicektir ki coin sayisi negatife dusunce durur. Fkara row sayisi ilerlemis oldugunda 1 cikarmamis gerekir. n 0 dan kucuk oldugunda da coin yetmemis demektir ama row sayisi yine de bir arttigi icin row dan bir cikarmamiz gerekir.
            row += 1
            n -= row
            
        return row - 1 