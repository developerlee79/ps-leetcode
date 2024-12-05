class Solution(object):
    def canChange(self, start, target):
        n = len(start)
        left_count = 0
        right_count = 0

        for i in range(n):
            left = start[i]
            right = target[i]
            if left == 'R':
                if left_count > 0:
                    return False
                right_count += 1
            if right == 'L':
                if right_count > 0:
                    return False
                left_count += 1
            if right == 'R':
                if right_count == 0:
                    return False
                right_count -= 1
            if left == 'L':
                if left_count == 0:
                    return False
                left_count -= 1

        return left_count == right_count == 0
