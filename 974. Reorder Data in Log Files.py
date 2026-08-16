class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digit_logs = []
        let_logs = []
        result = []

        for log in logs:
            if log.split(' ')[1].isdigit():
                digit_logs.append(log)
                continue
            
            let_logs.append(log)

        let_logs.sort(key= lambda log: (log.split(' ', 1)[1], log.split(' ', 1)[0]))


            
        for log in let_logs:
            result.append(log)

        for log in digit_logs:
            result.append(log)

        return result
            
             