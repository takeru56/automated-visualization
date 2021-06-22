import matplotlib.pyplot as plt
import os

MAKE_RESULT_PATH = lambda f: os.path.join(os.path.dirname(__file__), '../result/' + f + '.png')

def test():
    left = [1, 2, 3]  # グラフの横軸（X軸）
    height = [3, 5, 0]  # 値（Y軸）
    plt.bar(left, height)
    yyyymm = 202109
    plt.savefig(MAKE_RESULT_PATH('bid' + str(yyyymm)[4:6]))


if __name__ == '__main__':
    test()
