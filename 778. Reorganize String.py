import heapq
from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = Counter(s)
        freq_list = []
        result = ""

        for key, value in freq.items():
            freq_list.append((value, key))

        heapq.heapify_max(freq_list)

        for i in range(len(s)):
            print(freq_list)

            count, char = heapq.heappop_max(freq_list)

            if len(result) != 0 and char == result[len(result) - 1]:
                if len(freq_list) == 1:
                    result = ""
                    break
                tmp_count, tmp_char, = heapq.heappop_max(freq_list)
                heapq.heappush_max(freq_list, (count, char))
                count = tmp_count
                char = tmp_char

            result += char
            print(result)

            count -= 1

            if count == 0:
                continue
            else:
                heapq.heappush_max(freq_list, (count, char))

        return result




        

