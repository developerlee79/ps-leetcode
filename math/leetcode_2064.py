class Solution(object):
    def minimizedMaximum(self, n, quantities):
        low = 1
        high = max(quantities)

        while low < high:
            mid = int((low + high) / 2)
            count = 0
            for q in quantities:
                count += -(-q // mid)
            if count <= n:
                high = mid
            else:
                low = mid + 1

        return low
