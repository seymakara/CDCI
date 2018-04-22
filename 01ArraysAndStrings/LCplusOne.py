# turn digits into an integer
# add 1 to the integer
# turn the integer into a str
# loop trough the str and print the items as integers into a list

class Solution(object):
    def plusOne(self, digits):
        num = 0 
        for i in range(len(digits)):
            num += digits[i] * pow(10, (len(digits)-1-i))
        return [int(i) for i in str(num+1)]
