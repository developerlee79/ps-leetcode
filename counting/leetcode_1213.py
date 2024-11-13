class Solution(object):
    def arraysIntersection(self, arr1, arr2, arr3):
        intersections = []
        counter = {}

        self.count_frequency(arr1, counter)
        self.count_frequency(arr2, counter)

        for num in arr3:
            if num in counter and counter[num] == 2:
                intersections.append(num)

        return intersections

    @staticmethod
    def count_frequency(nums, counter):
        for num in nums:
            if num not in counter:
                counter[num] = 0
            counter[num] = counter[num] + 1
