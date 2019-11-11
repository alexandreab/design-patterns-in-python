class Fibonacci:
    def __iter__(self):
        self.last = 0
        self.penult = 1
        return self

    def __next__(self):
        x = self.last
        self.last += self.penult
        self.penult = x

        return self.last
