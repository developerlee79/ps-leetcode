class Solution(object):
    def lexicalOrder(self, n):
        nums = []
        self.find_next(n, 0, nums)
        return nums[1:]

    def find_next(self, n, i, nums):
        if i > n:
            return

        nums.append(i)

        for add in range(10):
            if i == 0 == add:
                continue
            self.find_next(n, i * 10 + add, nums)
