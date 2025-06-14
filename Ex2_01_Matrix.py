# Time Complexity: O(m * n), where m is the number of rows and n is the number of columns
# Space Complexity: O(m * n) for the result matrix and queue in the worst case
# Did this code successfully run on Leetcode: Yes
# Any problem you faced while coding this: No

from typing import List
from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])
        
        # Initialize result matrix with -1 (unvisited)
        res = [[-1] * cols for _ in range(rows)]
        q = deque()

        # Step 1: Enqueue all 0s and set their distance to 0
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    res[r][c] = 0
                    q.append((r, c))

        # 4-directional movement (up, down, left, right)
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        # Step 2: Multi-source BFS
        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and res[nr][nc] == -1:
                    res[nr][nc] = res[r][c] + 1
                    q.append((nr, nc))

        return res


        # ---------------------------------------------------------------------
        # DP-based approach
        # Time Complexity: O(m * n), where m = number of rows, n = number of columns
        #   - We visit each cell twice (forward and backward pass)
        # Space Complexity: O(m * n) for the distance matrix
        
        # rows = len(mat)
        # cols = len(mat[0])
        
        # # Initialize distance matrix with infinity
        # dist = [[float('inf')] * cols for _ in range(rows)]
        
        # # First pass: top-left to bottom-right
        # for r in range(rows):
        #     for c in range(cols):
        #         if mat[r][c] == 0:
        #             dist[r][c] = 0  # Distance to 0 is 0 itself
        #         else:
        #             if r > 0:
        #                 dist[r][c] = min(dist[r][c], dist[r-1][c] + 1)
        #             if c > 0:
        #                 dist[r][c] = min(dist[r][c], dist[r][c-1] + 1)

        # # Second pass: bottom-right to top-left
        # for r in range(rows - 1, -1, -1):
        #     for c in range(cols - 1, -1, -1):
        #         if r < rows - 1:
        #             dist[r][c] = min(dist[r][c], dist[r+1][c] + 1)
        #         if c < cols - 1:
        #             dist[r][c] = min(dist[r][c], dist[r][c+1] + 1)

        # return dist