class Solution(object):
    def minMaxDifference(self, num):
        num_str = str(num)

        max_target = ''
        min_target = ''

        max_number = ''
        min_number = ''

        for digit in num_str:
            if max_target == '' and digit != '9':
                max_target = digit
            if min_target == '':
                min_target = digit

            if max_target == digit and min_target == digit:
                max_number += '9'
                min_number += '0'
            elif max_target == digit:
                max_number += '9'
                min_number += digit
            elif min_target == digit:
                max_number += digit
                min_number += '0'
            else:
                max_number += digit
                min_number += digit

        return int(max_number) - int(min_number)
