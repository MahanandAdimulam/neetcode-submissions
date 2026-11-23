class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flatened_matrix = []
        for row in matrix:
            flatened_matrix.extend(row)
        start = 0
        end = len(flatened_matrix)-1
        while start <= end:
            mid = (start + end) // 2
            if flatened_matrix[mid] > target:
                end = mid - 1
            elif flatened_matrix[mid] < target:
                start = mid + 1
            elif flatened_matrix[mid] == target:
                return True
        return False