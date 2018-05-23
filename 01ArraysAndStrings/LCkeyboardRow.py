# Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.
# Example 1:
# Input: ["Hello", "Alaska", "Dad", "Peace"]
# Output: ["Alaska", "Dad"]


class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        a=set('qwertyuiop')
        b=set('asdfghjkl')
        c=set('zxcvbnm')
        res=[]
        for word in words:
            t=set(word.lower())
            if a&t==t:
                res.append(word)
            elif b&t==t:
                res.append(word)
            elif c&t==t:
                res.append(word)
        return res