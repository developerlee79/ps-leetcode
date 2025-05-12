class Solution(object):
    def findEvenNumbers(self, digits):
        nums = []

        counter = [0] * 10
        for digit in digits:
            counter[digit] += 1

        for i in range(1, 10):
            if counter[i] == 0:
                continue
            counter[i] -= 1
            for j in range(10):
                if counter[j] == 0:
                    continue
                counter[j] -= 1
                for k in range(0, 10, 2):
                    if counter[k] == 0:
                        continue
                    counter[k] -= 1
                    nums.append(i * 100 + j * 10 + k)
                    counter[k] += 1
                counter[j] += 1
            counter[i] += 1

        return nums
