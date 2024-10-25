class Solution(object):
    def digArtifacts(self, n, artifacts, dig):
        dig_grid = [[False for _ in range(n)] for _ in range(n)]

        for location in dig:
            x, y = location
            dig_grid[x][y] = True

        found_artifacts = 0

        for artifact in artifacts:
            startX = artifact[0]
            startY = artifact[1]
            endX = artifact[2]
            endY = artifact[3]
            if self.is_extracted(dig_grid, startX, startY, endX, endY):
                found_artifacts += 1

        return found_artifacts

    @staticmethod
    def is_extracted(dig_grid, startX, startY, endX, endY):
        for i in range(startX, endX + 1):
            for j in range(startY, endY + 1):
                if not dig_grid[i][j]:
                    return False
        return True
