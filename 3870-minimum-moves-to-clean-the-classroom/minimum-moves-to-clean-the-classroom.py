from collections import deque

class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m = len(classroom)
        if m == 0:
            return -1

        n = len(classroom[0])

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        litter = {}
        start_x = start_y = -1

        for i in range(m):
            for j in range(n):
                if classroom[i][j] == 'L':
                    litter[(i, j)] = len(litter)

                if classroom[i][j] == 'S':
                    start_x = i
                    start_y = j

        total_litter = len(litter)

        if total_litter == 0:
            return 0

        full_mask = (1 << total_litter) - 1

        q = deque()
        q.append((start_x, start_y, energy, 0, 0))

        visited = set()
        visited.add((start_x, start_y, energy, 0))

        while q:
            x, y, e, mask, moves = q.popleft()

            if mask == full_mask:
                return moves

            if e == 0:
                continue

            for dx, dy in directions:
                new_x = x + dx
                new_y = y + dy

                if not (0 <= new_x < m and 0 <= new_y < n):
                    continue

                if classroom[new_x][new_y] == 'X':
                    continue

                new_energy = e - 1
                new_mask = mask

                if classroom[new_x][new_y] == 'R':
                    new_energy = energy

                if classroom[new_x][new_y] == 'L':
                    idx = litter[(new_x, new_y)]
                    new_mask |= (1 << idx)

                state = (
                    new_x,
                    new_y,
                    new_energy,
                    new_mask
                )

                if state not in visited:
                    visited.add(state)

                    q.append((
                        new_x,
                        new_y,
                        new_energy,
                        new_mask,
                        moves + 1
                    ))

        return -1