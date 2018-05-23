# Write a function that takes a string as input and reverse only the vowels of a string.

# Example 1:
# Given s = "hello", return "holle".

# Example 2:
# Given s = "leetcode", return "leotcede".

# Note:
# The vowels does not include the letter "y".

class Solution(object):
    def reverseVowels(self, s):

        
        vowel_list = ["a","e","i","o","u","A","E","I","O","U"]
        vowels = {}
        
        for i in vowel_list:
            vowels[i] = vowels.get(i, 0) + 1
            
        s = list(s)
        
        p1, p2 = 0, len(s) - 1
        
        while p1 < p2:
            if s[p1] in vowels and s[p2] in vowels:
                temp = s[p1]
                s[p1] = s[p2] 
                s[p2] = temp
                p1 += 1
                p2 -= 1
            if s[p1] not in vowels:
                p1 += 1
            if s[p2] not in vowels:
                p2 -= 1
                
        return ''.join(s)