class Solution:
    def reverseBits(self, n: int) -> int:
        m = (n >> 16) | (n << 16)
        m = ((m & 0xff00ff00) >> 8) | ((m & 0x00ff00ff) << 8)
        m = ((m & 0xf0f0f0f0) >> 4) | ((m & 0x0f0f0f0f) << 4)
        m = ((m & 0xcccccccc) >> 2) | ((m & 0x33333333) << 2)
        m = ((m & 0xaaaaaaaa) >> 1) | ((m & 0x55555555) << 1)
        return m & 0xffffffff
