class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers = {}

        for i, number in enumerate(nums):
            check_num = target - number;

            if check_num in numbers:
                result = [numbers[check_num], i]
                result.sort()
                return result
            
            numbers[number] = i

            #test for DOM