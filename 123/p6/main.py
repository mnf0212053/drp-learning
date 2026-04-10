import numpy as np
import matplotlib.pyplot as pyplot

# 1. Modul Numpy = Modul fungsi matematik
# 2. Modul Matplotlib = Modul grafik

def f(x):
    return pow(x, 2)

if __name__ == '__main__':
    x = np.linspace(-4, 4, num=300)
    y = f(x)

    pyplot.plot(x, y)
    pyplot.show()
