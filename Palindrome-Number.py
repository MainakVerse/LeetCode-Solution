# Just check if they ask the reverse of -121 as 121-. If this is true, convert to string

class Solution:
    def isPalindrome(self, x: int) -> bool:
        k = str(x)
        if k[::-1] == str(x):
            return True
        else:
            return False 
