class StockSpanner:
    def __init__(self):
        self.stack: list[tuple[int, int]] = []

    def next(self, price: int) -> int:
        span = 1
        while self.stack and self.stack[-1][1] <= price:
            span += self.stack[-1][0]
            self.stack.pop()
        self.stack.append((span, price))
        return span
