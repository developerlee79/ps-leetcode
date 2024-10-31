class Solution(object):
    def decode(self, encoded):
        n = len(encoded) + 1

        x = 1

        for i in range(2, n + 1):
            x ^= i

        for i in range(1, n, 2):
            x ^= encoded[i]

        perm = [x]

        for i in range(n - 1):
            perm.append(perm[i] ^ encoded[i])

        return perm
