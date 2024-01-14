import math

# Symbols
class SYM:
    # Create
    def __init__(self, s=None, n=None):
        self.txt = s or " "
        self.at = n or 0
        self.n = 0
        self.has = {}
        self.mode = None
        self.most = 0

    # Update
    def add(self, x):
        if x != "?":
            self.n += 1
            self.has[x] = 1 + (self.has.get(x, 0))
            if self.has[x] > self.most:
                self.most, self.mode = self.has[x], x

    # Query
    def mid(self):
        return self.mode

    def div(self, e=0):
        for v in self.has.values():
            e -= v / self.n * math.log(v / self.n, 2)
        return e

    def small(self):
        return 0

# Example usage:
# sym_instance = SYM("example")
# sym_instance.add("value")
# print(sym_instance.mid())
# print(sym_instance.div())
# print(sym_instance.small())

