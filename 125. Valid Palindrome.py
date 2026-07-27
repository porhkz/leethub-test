class Solution:
    def isPalindrome(self, s: str) -> bool:        
        list_s = [c for c in s if c.isalnum()]
        list_s = [c.lower() for c in list_s]
        s = "".join(list_s)
        right = len(s)-1

        if len(s) == 0 or len(s) == 1:
            return True

        for i in range(len(s)):
            if i == right:
                return True
            
            if s[i] != s[right]:
                return False
            
            right = right - 1

        return True
            
