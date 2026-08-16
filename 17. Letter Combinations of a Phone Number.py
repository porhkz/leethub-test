class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []

        phone = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz",
        }
            
        def backtrack(index, path) -> str:
            if len(path) == len(digits):
                result.append(path)
                return
                                
            digit = digits[index]
            letters = phone[digit]

            for letter in letters:
                backtrack(index + 1, path + letter)

        backtrack(0, "")

        return result



        

        