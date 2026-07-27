class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        store = defaultdict(int)

        if len(s) != len(t):
            return False

        for i in s:
            store[i] += 1

        for k in t:
            if store[k] == 0:
                return False

            store[k] -= 1

        return True
            
        