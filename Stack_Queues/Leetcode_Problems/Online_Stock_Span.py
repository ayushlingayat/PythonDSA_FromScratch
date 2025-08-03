class StockSpanner:

    def __init__(self):
        self.st = []  # Stack of pairs (price, span)

    def next(self, price: int) -> int:
        span = 1
        while self.st and self.st[-1][0] <= price:
            span += self.st[-1][1]
            self.st.pop()
        self.st.append((price, span))
        return span
