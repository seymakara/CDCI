class Solution(object):
    def addStrings(self, num1, num2):
        n1 = list(num1)
        n2 = list(num2)
        
        carry =0
        res = ""
        
        while len(n1)>0 or len(n2)>0:
            
            if len(n1) > 0:
                num1 = ord(n1.pop()) - ord('0') # turning them into an integer using their unicode code. ord(2) = 50 ord(0) = 48
                print "num1", num1
            else:
                num1 = 0
                
            if len(n2)>0:
                num2 = ord(n2.pop()) - ord('0')
            else:
                num2 = 0
            
            temp = num1 + num2 + carry
            res += (str(temp % 10))
            carry = temp // 10
            
        if carry:
            res += (str(carry))
        
        return tempRes[::-1] #reversing the string

        # res2 = ""    #OPTION 2
        # for i in res[::-1]: 
        #     res2 += i
        # return res2
        
        