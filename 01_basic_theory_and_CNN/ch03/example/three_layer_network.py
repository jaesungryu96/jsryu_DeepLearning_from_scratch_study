import numpy as np
from sigmoid_function import sigmoid


def identity_function(x):
    return x


def init_network():
    network = {}  # 신경망에서 쓰일 매개변수들의 dictionary를 만들어줍니다. 가중치는 W1, W2, W3, 편향은 b1, b2, b3
    network['W1'] = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])  # W1 key에 np.array value 입력
    network['b1'] = np.array([0.1, 0.2, 0.3])
    network['W2'] = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
    network['b2'] = np.array([0.1, 0.2])
    network['W3'] = np.array([[0.1, 0.3], [0.2, 0.4]])
    network['b3'] = np.array([0.1, 0.2])

    return network


def forward(network, x):
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']

    a1 = np.dot(x, W1) + b1  # 행렬 곱을 계산합니다.
    z1 = sigmoid(a1)  # sigmoid 함수를 활성화 함수로 사용합니다.
    a2 = np.dot(z1, W2) + b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2, W3) + b3
    y = identity_function(a3)  # 출력층으로 항등 함수로 설계했습니다.

    return y


network = init_network()
x = np.array([1.0, 0.5])
y = forward(network, x)
print(y) # [0.31682708 0.69627909]