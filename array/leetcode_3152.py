class Solution(object):
    def isArraySpecial(self, nums, queries):
        n = len(nums)

        if n == 1:
            return [True] * len(queries)

        not_special_index = []

        last_even = nums[0] % 2

        if last_even == nums[1] % 2:
            not_special_index.append(0)

        for i in range(1, n - 1):
            is_even = nums[i] % 2
            next_even = nums[i + 1] % 2
            if last_even != next_even or last_even == is_even:
                not_special_index.append(i)
            last_even = is_even

        if last_even == nums[-1] % 2:
            not_special_index.append(n - 1)

        not_special_index.sort()

        is_specials = []

        for query in queries:
            start, end = query
            if start == end:
                is_specials.append(True)
            elif end - start == 1:
                is_specials.append(nums[start] % 2 != nums[end] % 2)
            else:
                is_specials.append(self.is_special(not_special_index, start + 1, end - 1))

        return is_specials

    @staticmethod
    def is_special(arr, start, end):
        low = 0
        high = len(arr) - 1

        while low <= high:
            mid = (low + high) / 2

            if start <= arr[mid] <= end:
                return False
            elif start > arr[mid]:
                low = mid + 1
            else:
                high = mid - 1

        return True
