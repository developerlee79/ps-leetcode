class Solution(object):

    def findDifferentBinaryString(self, nums):
        n = len(nums)
        return ''.join('1' if nums[i][i] == '0' else '0' for i in range(n))

    @staticmethod
    def to_binary_string(n, length):
        binary_string = bin(n)[2:]
        return '0' * (length - len(binary_string)) + binary_string
