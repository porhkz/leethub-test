class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = s[0]
        
        for i, c in enumerate(s):
            left = i
            right = i
            c_pal = ""

            if len(s) % 2 == 0 and i != len(s) - 1:
                right = i + 1

            while s[left] == s[right]:
                c_pal = s[left:right+1]

                if left != 0:
                    left -= 1
                
                if right != len(s) - 1:
                    right += 1

            if len(c_pal) > len(result):
                result = c_pal

        return result



            