class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [0 for i in range(len(nums))]
        suffix = [0 for i in range(len(nums))]
        result = [0 for i in range(len(nums))]

        prefix_count = 1
        suffix_count = 1

        for i in range(len(nums)):
            prefix[i] = prefix_count
            suffix[len(nums) - 1 - i] = suffix_count

            prefix_count = prefix_count * nums[i]
            suffix_count = suffix_count * nums[len(nums) - 1 - i]


        for i in range(len(nums)):
            result[i] = prefix[i] * suffix[i]

        return result


