class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left, right) -> str:
            tmp_pal = ""

            while left >= 0 and right < len(s) and s[left] == s[right]:                
                tmp_pal = s[left:right+1]
                
                if left == 0 and right == len(s) - 1:
                    break
                
                left -= 1
                right += 1
            
            return tmp_pal

        result = s[0]
        c_pal = ""
        
        for i, c in enumerate(s):            
            odd = expand(i, i)
            even = expand(i, i + 1)

            c_pal = max(odd, even, key=len)

            if len(c_pal) > len(result):
                result = c_pal

        return result



            