class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        is_seen = set()

        for i in nums:
            if i in is_seen:
                return True
            
            is_seen.add(i)

        return False