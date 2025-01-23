class Solution:
    def optimalPlacement(self, w: int, h: int, n: int) -> int:
        """
        Approach:
        - Use combinations to place buildings in all possible configurations of `n` buildings in a grid.
        - For each configuration, calculate the maximum distance from any cell to the nearest building using BFS.
        - Return the minimum of these maximum distances across all configurations.
        Time Complexity:
        - Generating combinations: O((w*h choose n)) ≈ O((w*h)^n / n!)
        - BFS for each configuration: O(w * h)
        - Overall: O((w*h)^n / n! * w * h)
        Space Complexity:
        - BFS queue: O(w * h)
      
        Any problem you faced while coding this: Iterating over combinations for large grids can be computationally expensive.
        """

        def bfs(buildings):
            """
            Perform BFS to calculate the maximum distance from any cell to the nearest building.
            """
            visited = [[False] * h for _ in range(w)]
            queue = deque()

            # Initialize the queue with the positions of the buildings
            for x, y in buildings:
                queue.append((x, y, 0))
                visited[x][y] = True

            max_dist = 0

            while queue:
                x, y, dist = queue.popleft()
                max_dist = max(max_dist, dist)

                # Explore all 4 possible movements
                for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < w and 0 <= ny < h and not visited[nx][ny]:
                        visited[nx][ny] = True
                        queue.append((nx, ny, dist + 1))

            return max_dist

        # Generate all possible combinations of n buildings
        cells = [(i, j) for i in range(w) for j in range(h)]
        min_distance = float('inf')

        for buildings in combinations(cells, n):
            # Calculate the maximum distance for this configuration
            max_dist = bfs(buildings)
            min_distance = min(min_distance, max_dist)

        return min_distance
