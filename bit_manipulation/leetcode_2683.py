class Solution(object):
    def doesValidArrayExist(self, derived):
        xr_sum = 0
        for i in derived:
            xr_sum ^= i
        return xr_sum == 0
