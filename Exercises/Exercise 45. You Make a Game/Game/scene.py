import time as t


class timer(object):

    def begin(self):
        self.start_time = t.time()
        return self.start_time

    def end(self):
        self.finish_time = t.time()
        return self.finish_time

    def result(start, end):
        total = int(end - start)
        minutes = 0

        while True:
            if total <= 0:
                break

            elif total <= 59:
                break

            total -= 60
            minutes += 1
    
        return f"{minutes}m {abs(total)}s"