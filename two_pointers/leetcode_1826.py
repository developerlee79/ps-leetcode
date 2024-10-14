class Solution(object):
    def badSensor(self, sensor1, sensor2):
        n = len(sensor1)

        i = 0

        while i < n and sensor1[i] == sensor2[i]:
            i += 1

        if i >= n - 1 or (sensor1[i + 1:] == sensor2[i:-1] and sensor1[i:-1] == sensor2[i+1:]):
            return -1

        return 1 if sensor1[i + 1:] != sensor2[i:-1] else 2
