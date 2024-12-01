class Solution(object):
    def checkIfExist(self, arr):
        num_set = set()

        for num in arr:
            product = num << 1
            divide = num / 2.0
            if product in num_set or divide in num_set:
                return True
            num_set.add(num)

        return False
