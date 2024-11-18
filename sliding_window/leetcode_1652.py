class Solution(object):
    def decrypt(self, code, k):
        if k < 0:
            return self.decrypt(code[::-1], -k)[::-1]

        n = len(code)
        decrypt_codes = [0] * n

        current_sum = sum(code[:k])

        for i, c in enumerate(code):
            current_sum += code[(i + k) % n] - c
            decrypt_codes[i] = current_sum

        return decrypt_codes
