# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

# Note: For the purpose of this problem, we define empty string as valid palindrome.

class Solution(object):
    def isPalindrome(self, s):
        l, r = 0, len(s)-1
        while l < r:
            if not s[l].isalnum():
                l+=1
                continue
            if not s[r].isalnum():
                r-=1
                continue
            if s[l].lower() != s[r].lower():
                return False
            l +=1; r -= 1
        return True