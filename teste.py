import zeros
import numpy as np

x = np.arange(0, 3, 0.01);
A = 27*x**3 + 27/2*x**4 + 9*x**5/4 + (x**6)/8;
B = 3+x;
y = B*20**2 - 9.81*A;

graph = zeros.graphically(x,y)