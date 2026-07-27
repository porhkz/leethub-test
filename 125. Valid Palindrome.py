class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0 or len(s) == 1:
            return True
        
        list_s = [c for c in s if c.isalpha() and c.islower()]
        s = "".join(list_s)
        right = len(s)-1
        
        print(s)

        for i in range(len(s)):
            if s[i] != s[right]:
                return False
            
            right = len(s) - 1

        return False
            
