class EvenNumbers:
    def __init__(self, start=0, end = 1):
        self.start = start
        self.end = end

    def __iter__(self):
        self.i = self.start
        if self.i % 2 != 0:
            self.i += 1
        return self

    def __next__(self):
        if self.i >= self.end:
            raise StopIteration()
        current = self.i
        self.i += 2
        return current


en = EvenNumbers(10, 25)
for i in en:
    print(i)