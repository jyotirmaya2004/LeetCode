class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        negatives = 0 
        ab_sum = 0 
        lowest_nbr = float('inf')
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                abs_matrix = abs(matrix[i][j])
                if abs_matrix < lowest_nbr:
                    lowest_nbr = abs_matrix
                if matrix[i][j] < 0:
                    negatives += 1
                ab_sum += abs_matrix
        if negatives % 2 == 0:
            return ab_sum
        else:
            return ab_sum - 2*lowest_nbr
 
