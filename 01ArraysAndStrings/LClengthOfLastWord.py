#Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.
#If the last word does not exist, return 0.

class Solution(object):
    def lengthOfLastWord(self, s):
        arr = s.rstrip(' ').split(' ')
        return len(arr[-1])
        