class Solution(object):
    def tupleSameProduct(self, nums):
        n = len(nums)
        prod_freq = {}
        for i in range(n):
            for j in range(i + 1, n):
                prod = nums[i] * nums[j]
                if prod not in prod_freq:
                    prod_freq[prod] = 0
                prod_freq[prod] += 1
        count = 0
        for freq in prod_freq.values():
            if freq > 1:
                count += freq * (freq - 1)
        return count << 2
