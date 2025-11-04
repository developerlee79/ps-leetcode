from typing import List


class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        answer = [0] * (n - k + 1)
        freq = {}
        for i in range(k - 1):
            if nums[i] not in freq:
                freq[nums[i]] = 0
            freq[nums[i]] += 1

        for i in range(k - 1, n):
            if nums[i] not in freq:
                freq[nums[i]] = 0
            freq[nums[i]] += 1
            answer[i - k + 1] = self.sum_of_top_freq(freq, x)
            freq[nums[i - k + 1]] -= 1

        return answer

    @staticmethod
    def sum_of_top_freq(freq, x: int) -> int:
        queue = []
        for i, num in freq.items():
            queue.append((num, i))
        queue.sort()
        sum_freq = 0
        for _ in range(x):
            if not queue:
                break
            num, i = queue.pop()
            sum_freq += num * i
        return sum_freq
