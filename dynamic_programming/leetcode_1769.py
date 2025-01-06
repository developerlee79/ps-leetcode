class Solution(object):
    def minOperations(self, boxes):
        n = len(boxes)
        operations = [0] * n

        left = 0
        right = 0
        left_count = 0
        right_count = 0

        for i in range(1, n):
            if boxes[i] == '1':
                right += i
                right_count += 1

        operations[0] = right

        for i in range(1, n):
            if boxes[i - 1] == '1':
                left_count += 1
            left += left_count
            right -= right_count
            if boxes[i] == '1':
                right_count -= 1
            operations[i] = left + right

        return operations
