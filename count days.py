class Solution:
    #day =sunday,monday,..
    #n=0,1,2,3,4,...
    def findAnswer(self, d, n):
       days = {0: "sunday", 1: "monday", 2: "tuesday", 3: "wednesday", 4: "thursday", 5: "friday", 6: "saturday"}  #this is refernce not used in code
       print(((d-n)%7))

sol=Solution()
sol.findAnswer(2,18)

#calculation
'''
example: if we give d=2,n=18 means
        formula=(d-n)%7
    solution:
        
        (d - n) % 7 = (2 - 18) % 7
             = (-16) % 7

    a = b*q + r  , q=quotient , r=remainder
    
        -16 / 7 = -2.285...
         floor = -3
         q = -3
        
        r = -16 - 7 * (-3)
          = -16 + 21
          = 5
