class MulLayer:
    def __init__(self):
        self.x = None
        self.y = None

    def forward(self, x, y):
        self.x = x
        self.y = y
        out = x * y
        return out

    def backward(self, dout):
        # dout은 상류의 흐름을 말합니다.
        dx = dout * self.y
        dy = dout * self.x  # 서로의 순전파 때의 값을 바꿔 곱합니다.

        return dx, dy


class AddLayer:
    # 곱셈 계층처럼 이전의 순전파 값을 기억할 필요가 없습니다.
    def __init__(self):
        pass

    def forward(self, x, y):
        out = x + y
        return out

    def backward(self, dout):
        dx = dout * 1
        dy = dout * 1
        return dx, dy