class Solution:
    def firstUniqChar(self, s: str) -> int:
        store = defaultdict(int)

        for c in s:
            store[c] += 1

        for i, c in enumerate(s):
            if store[c] == 1:
                return i

        return -1