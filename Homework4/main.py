class Counter:
    def __init__(self, i = 0, max_number = 0):
        self.I = i
        self.Max_Number = max_number
    def __str__(self):
        return f"{self.I}"
    def __iter__(self):
        self.I = 0
        return self
    def __next__(self):
        self.I += 1
        if(self.I > self.Max_Number):
            raise StopIteration
        return self.I