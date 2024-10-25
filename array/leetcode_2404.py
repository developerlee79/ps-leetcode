class Solution(object):
    def mostFrequentEven(self, nums):
        nums.sort()

        frequency_map = {}

        most_frequency = 0
        most_frequency_num = -1

        for num in nums:
            if num % 2 == 0:
                frequency_map[num] = frequency_map.get(num, 0) + 1
                if most_frequency < frequency_map[num]:
                    most_frequency = max(most_frequency, frequency_map[num])
                    most_frequency_num = num

        return most_frequency_num
