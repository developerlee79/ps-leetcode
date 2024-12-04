class Solution(object):
    def makeSmallestPalindrome(self, s):
        n = len(s)
        half = n >> 1
        arr = []
        for i in range(half):
            target = s[i]
            if ord(s[i]) > ord(s[n - i - 1]):
                target = s[n - i - 1]
            arr.append(target)
        palindrome = "".join(arr)
        if n & 1 == 0:
            return palindrome + palindrome[::-1]
        else:
            return palindrome + s[half] + palindrome[::-1]
