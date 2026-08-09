class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        result = defaultdict(int)
        result_list = []

        for i, word in enumerate(words):
            tmp_dict = defaultdict(int)
            
            for c in word:
                tmp_dict[c] += 1

            if i == 0:
                for key, value in tmp_dict.items():
                    result[key] = value

                continue
                
            for key, value in list(result.items()):
                if not tmp_dict[key]:
                    result.pop(key)
                elif tmp_dict[key] < value:
                        result[key] = tmp_dict[key]

        for key, value in result.items():
            result_list.extend([key] * value)

        return result_list

