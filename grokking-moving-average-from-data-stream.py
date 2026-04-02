from collections import deque

class MovingAverage:

    def __init__(self, size):
        self.size = size
        self.queue = deque()
        self.current_sum = 0

    def next(self, val):
        self.queue.append(val)
        self.current_sum += val

        if len(self.queue) > self.size:
            self.current_sum -= self.queue.popleft()

        return self.current_sum / len(self.queue)
