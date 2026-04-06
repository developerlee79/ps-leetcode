from typing import List


class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        max_distance = 0
        obs_set = set[(int, int)]()
        
        for row in obstacles:
            x, y = row
            obs_set.add((x, y))

        direction = 0
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        def turn_direction(command):
            nonlocal direction
            if command == -1:
                if direction < 3:
                    direction += 1
                else:
                    direction = 0
            else:
                if direction > 0:
                    direction -= 1
                else:
                    direction = 3

        x = 0
        y = 0
        for command in commands:
            if command < 0:
                turn_direction(command)
                continue
            for _ in range(command):
                if (x + directions[direction][0], y + directions[direction][1]) in obs_set:
                    break
                x += directions[direction][0]
                y += directions[direction][1]
            max_distance = max(max_distance, (abs(x) ** 2 + abs(y) ** 2))

        return max_distance
