class Solution:
    def isPalindrome(self, s: str) -> bool:
        right = len(s)-1

        if len(s) == 0 or len(s) == 1:
            return True
        
        for i in range(s):
            if s[i] != s[right]:
                return False
            
            right = len(s) - 1

        return False
            
