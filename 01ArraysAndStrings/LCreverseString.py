class Solution(object): 
    def reverseString(self, s):
        l = len(s)
        if l < 2:
            return s
        return self.reverseString(s[l//2:]) + self.reverseString(s[:l//2])
    
    
#                 func('abcd') 
#                     V
#         func('cd')  +  func('ab')
#             V            V
# func('d') + func('c')  func('b') + func('a')
#    v          v           v           v
#    d          c           b           a