class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        
        # We only need to iterate over 1/4 of the manifold 
        # to touch every cyclic orbit exactly once.
        for r in range((n + 1) // 2):
            for c in range(n // 2):
                # 1. Store the initial state (The "Current" potential)
                tmp = matrix[r][c]
                
                # 2. Perform the Cyclic Transition (In-Place)
                # We move values backward along the orbit to fill the 'holes'
                # Bottom-left to Top-left
                matrix[r][c] = matrix[n - 1 - c][r]
                
                # Bottom-right to Bottom-left
                matrix[n - 1 - c][r] = matrix[n - 1 - r][n - 1 - c]
                
                # Top-right to Bottom-right
                matrix[n - 1 - r][n - 1 - c] = matrix[c][n - 1 - r]
                
                # Top-left (tmp) to Top-right
                matrix[c][n - 1 - r] = tmp        