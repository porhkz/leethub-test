class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = matrix[0][0]
        right = len(matrix) * len(matrix[0]) - 1

        while left <= right:
            mid = (left + right) // 2
            row, col = mid // len(matrix[0]), mid % len(matrix[0])

            mid_val = matrix[row][col]

            if target == mid_val:
                return True
            elif target < mid_val:
                right = mid - 1
            else: 
                left = mid + 1

        return False
