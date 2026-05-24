class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col_len = len(matrix[0])
        for r in range(row):
            if target >= matrix[r][0] and target <= matrix[r][col_len - 1]:
                start = 0
                end = col_len - 1
                while start <= end:
                    mid = (start + end) // 2
                    if target == matrix[r][mid]:
                        return True
                    elif target < matrix[r][mid]:
                        end = mid - 1
                    else:
                        start = mid + 1
            else:
                continue
        return False