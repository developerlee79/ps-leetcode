class Solution(object):
    def shareCandies(self, candies, k):
        n = len(candies)
        flavors = {}

        for candy in candies:
            if candy not in flavors:
                flavors[candy] = 0
            flavors[candy] += 1

        i = 0

        while i < k:
            if flavors[candies[i]] == 1:
                del flavors[candies[i]]
            else:
                flavors[candies[i]] -= 1
            i += 1

        max_flavors = len(flavors)

        while i < n:
            if candies[i] in flavors:
                if flavors[candies[i]] == 1:
                    del flavors[candies[i]]
                else:
                    flavors[candies[i]] -= 1

            if candies[i - k] not in flavors:
                flavors[candies[i - k]] = 1
            else:
                flavors[candies[i - k]] += 1

            max_flavors = max(max_flavors, len(flavors))
            i += 1

        return max_flavors
