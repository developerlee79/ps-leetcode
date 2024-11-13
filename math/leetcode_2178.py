class Solution(object):
    def maximumEvenSplit(self, finalSum):
        if finalSum % 2 != 0:
            return []

        split_evens = []
        even_sum = 0
        k = 2

        while even_sum + k <= finalSum:
            split_evens.append(k)
            even_sum += k
            k += 2

        split_evens[-1] += (finalSum - even_sum)

        return split_evens
