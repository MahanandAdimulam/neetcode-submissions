class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start = 0
        end = len(matrix)-1
        while start<=end:
            mid=int((start+end)/2)
            if target>=matrix[mid][0] and target <= matrix[mid][-1]:
                l=0
                r=len(matrix[mid])-1
                while l<=r:
                    mid2 = int((l+r)/2)
                    if target<matrix[mid][mid2]:
                        r=mid2-1
                    elif target>matrix[mid][mid2]:
                        l=mid2+1
                    elif target == matrix[mid][mid2]:
                        return True
                return False
            elif target < matrix[mid][0]:
                end = mid - 1
            elif target > matrix[mid][-1]:
                start = mid + 1
        return False