class Solution(object):
    def countFairPairs(self, nums, lower, upper):
        n = len(nums)

        nums.sort()

        count = 0

        i = 0
        j = n - 1

        while i < j:
            pair = nums[i] + nums[j]

            if pair < lower:
                i += 1
            elif pair > upper:
                j -= 1
            else:
                min_index = self.find_min_pair_index(nums, i, j, nums[i], lower)
                count += j - min_index
                if i != min_index:
                    count += 1
                i += 1

        return count

    @staticmethod
    def find_min_pair_index(nums, i, j, target, lower):
        start, end = i, j

        while start <= end:
            mid = int((start + end) / 2)
            if target + nums[mid] >= lower:
                end = mid - 1
            else:
                start = mid + 1

        return start
