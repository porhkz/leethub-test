class Solution:
    def convert(self, s: str, numRows: int) -> str:
        count, factor, hashmap, rslt = 0, 1, DefaultDict(str), ''

        if numRows == 1:
            return s 

        for i in range(len(s)):
            hashmap[count] = hashmap[count] + s[i]
            
            if count == numRows - 1:
                factor = -1
            elif count == 0:
                factor = 1

            count += factor

        for i in range(numRows):
            rslt += hashmap[i]

        return rslt