# Time Complexity: O(m * n), where m is number of rows and n is number of columns
# Space Complexity: O(m * n) in worst case due to recursion stack (DFS depth)
# Did this code successfully run on Leetcode: Yes
# Any problem you faced while coding this: No

from typing import List
from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        rows = len(image)
        cols = len(image[0])
        original_col = image[sr][sc]

        # Base case: No need to fill if the color is already the same
        if original_col == color:
            return image

        def dfs(r, c):
            # Out of bounds or different color — stop
            if r < 0 or r >= rows or c < 0 or c >= cols or image[r][c] != original_col:
                return

            image[r][c] = color  # Fill current pixel

            # Recurse in all 4 directions
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        dfs(sr, sc)
        return image

        # ---------------------------------------------------------------------
        # BFS Version
        # Time Complexity: O(m * n)
        # Space Complexity: O(m * n) for the queue in the worst case
        #
        # q = deque()
        # q.append((sr, sc))
        # image[sr][sc] = color
        # directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        # while q:
        #     r, c = q.popleft()
        #     for dr, dc in directions:
        #         nr, nc = r + dr, c + dc
        #         if 0 <= nr < rows and 0 <= nc < cols and image[nr][nc] == original_col:
        #             image[nr][nc] = color
        #             q.append((nr, nc))

        # return image
