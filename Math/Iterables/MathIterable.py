class MathIterable:
    def __init__(self, initial_values: list | None = None):
        self.values = initial_values or []

    def __iter__(self):
        return self

    def __next__(self):
        self.values = self.values + [self.calc_next(self.values)]
        value = self.values[-1]
        if value is None:
            raise StopIteration
        return value

    def calc_next(self, values: list):
        raise NotImplementedError("Subclasses must implement calc_next")
