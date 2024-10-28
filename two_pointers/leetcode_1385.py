class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        count = 0

        for num1 in arr1:
            is_distance_value = True
            for num2 in arr2:
                if abs(num1 - num2) <= d:
                    is_distance_value = False
                    break
            if is_distance_value:
                count += 1

        return count

