class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket_list = [[] for _ in range(len(nums) + 1)]
        frequency_count = defaultdict(int)
        result = []

        for num in nums:
            frequency_count[num] += 1

        for num, freq in frequency_count.items():
            bucket_list[freq].append(num)

        for freq in range(len(bucket_list) -1, 0, -1):
            for n in bucket_list[freq]:
                result.append(n)

            if len(result) == k:
                return result

        return result