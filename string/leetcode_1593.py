class Solution(object):
    def maxUniqueSplit(self, s):
        return self.find_max_unique(s, len(s), 0, set([]))

    def find_max_unique(self, s, n, i, num_set):
        if i >= n:
            return len(num_set)

        max_count = 1

        for j in range(i, n):
            target = s[i:j + 1]
            if target not in num_set:
                num_set.add(target)
                max_count = max(max_count, self.find_max_unique(s, n, j + 1, num_set))
                num_set.remove(target)

        return max_count
