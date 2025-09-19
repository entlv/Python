
class Solution(object):
    def isPerfectSquare(self, num):
        x=sqrt(num) % 1  
        if x == 0:
            return True
        else:
            return False
