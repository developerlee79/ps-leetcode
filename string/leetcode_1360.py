import datetime


class Solution(object):
    def daysBetweenDates(self, date1, date2):
        date_format = '%Y-%m-%d'
        date_one = datetime.datetime.strptime(date1, date_format)
        date_two = datetime.datetime.strptime(date2, date_format)
        return abs((date_two - date_one).days)
