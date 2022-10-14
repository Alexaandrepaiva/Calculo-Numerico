import numpy as np
import matplotlib.pyplot as plt


def f(x):
    if x < 0.5:
        return 2
    else:
        return 1


def int_trpz(f, a, b, Io, k, s, z):
    if k == 1:
        I = (f(s, z, a) + f(s, z, b)) * (b - a) / 2.0
    else:
        n = 2 ** (k - 2)
        h = (b - a) / n
        x = a + h 
        sum = 0.0
        for i in range(n):
            sum = sum + f(s, z, x)
            x = x + h
        I = (Io + h * sum) 
    return I


def c(s, z):
    def h(s, z, x):
        return (f(x) * z) / ((z ** 2 + (s - x) ** 2) ** 1.5)

    return int_trpz(h, 0, 1, 0, 20, s, z)


s = np.arange(0, 2, 0.001)

plt.style.use('fivethirtyeight')

fig = plt.figure()
fig.subplots_adjust(hspace=0.5, top=0.95)

plt1 = fig.add_subplot(311)
plt2 = fig.add_subplot(312)
plt3 = fig.add_subplot(313)

plt1.plot(s, c(s, 1 / 4), color='b')
plt2.plot(s, c(s, 1 / 2), color='b')
plt3.plot(s, c(s, 1), color='b')

plt1.title.set_text("z=1/4")
plt2.title.set_text("z=1/2")
plt3.title.set_text("z=1")

plt.show()