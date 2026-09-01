class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])
        start_r, start_c = -1, -1
        litter_pos = {}

        # 1. Parse grid to find 'S' and assign bit indices to all 'L'
        for r in range(m):
            for c in range(n):
                if classroom[r][c] == "S":
                    start_r, start_c = r, c
                elif classroom[r][c] == "L":
                    litter_pos[(r, c)] = len(litter_pos)

        num_litters = len(litter_pos)
        target_mask = (1 << num_litters) - 1

        # If there are no litter items, 0 steps needed
        if num_litters == 0:
            return 0

        # 2. BFS Setup
        # visited[r][c][mask] stores the maximum remaining energy seen for state (r, c, mask)
        visited = {}

        # Queue elements: (r, c, mask, current_energy, steps)
        queue = deque([(start_r, start_c, 0, energy, 0)])
        visited[(start_r, start_c, 0)] = energy

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while queue:
            r, c, mask, e, steps = queue.popleft()

            # If current remaining energy is strictly less than a recorded visit, prune
            if e < visited.get((r, c, mask), -1):
                continue

            # Try moving in 4 directions
            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                # Check boundary conditions and obstacles
                if 0 <= nr < m and 0 <= nc < n and classroom[nr][nc] != "X":
                    new_e = e - 1

                    # Out of energy check
                    if new_e < 0:
                        continue

                    new_mask = mask
                    cell = classroom[nr][nc]

                    # If landing on a Reset cell, restore energy
                    if cell == "R":
                        new_e = energy

                    # If landing on an uncollected Litter cell, update mask
                    if cell == "L" and (nr, nc) in litter_pos:
                        litter_idx = litter_pos[(nr, nc)]
                        new_mask |= 1 << litter_idx

                    # Check if all litters are collected
                    if new_mask == target_mask:
                        return steps + 1

                    # State optimization: record only if we reached (nr, nc, new_mask) with MORE remaining energy
                    if new_e > visited.get((nr, nc, new_mask), -1):
                        visited[(nr, nc, new_mask)] = new_e
                        queue.append((nr, nc, new_mask, new_e, steps + 1))

        return -1
        
        
        