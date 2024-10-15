import collections


class FirstUnique(object):

    def __init__(self, nums):
        self.counter = collections.Counter(nums)
        self.queue = []
        for num in nums:
            if self.counter.get(num) == 1:
                self.queue.append(num)

    def showFirstUnique(self):
        return self.queue[0] if len(self.queue) > 0 else -1

    def add(self, value):
        self.counter.update({value, 1})

        if self.counter.get(value) == 1:
            self.queue.append(value)
        elif value in self.queue:
            self.queue.remove(value)
