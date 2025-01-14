class Solution(object):
    def findThePrefixCommonArray(self, A, B):
        n = len(A)
        prefix_common_arr = []

        a_set = 0
        b_set = 0
        common_count = 0

        for i in range(n):
            a_set ^= 1 << A[i]
            b_set ^= 1 << B[i]
            if A[i] == B[i]:
                common_count += 1
            else:
                if a_set & (1 << B[i]) != 0:
                    common_count += 1
                if b_set & (1 << A[i]) != 0:
                    common_count += 1
            prefix_common_arr.append(common_count)

        return prefix_common_arr
