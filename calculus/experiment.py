import matplotlib.pyplot as plt
import numpy as num  

import calculus.differentiate as differentiate
import calculus.integrate as integrate

# Exact Differentation Experiment
def g(x):
    return (x**2 * np.log(x))

a = 2

gprime = 2 + 4 * np.log(2)

hlist = np.linspace(0.005, 0.5, 100)

forward_error = np.abs([diff(g, a, h=h, mode=0) for h in hlist] - gprime)
backward_error = np.abs([diff(g, a, h=h, mode=2) for h in hlist] - gprime)
central_error = np.abs([diff(g, a, h=h, mode=1) for h in hlist] - gprime)
five_point_error = np.abs([diff(g, a, h=h, mode=3) for h in hlist] - gprime)

plt.figure()

plt.plot(hlist, forward_error, label="Forward Difference")
plt.plot(hlist, backward_error, label="Backward Difference")
plt.plot(hlist, central_error, label="Central Difference")
plt.plot(hlist, five_point_error, label="Five-Point Difference")

plt.title("Numerical Differentiation Errors vs Step Size")
plt.xlabel("Step Size (h)")
plt.ylabel("Absolute Error")

plt.legend()

# Reverse x-axis, step size decreases left to right
plt.xlim(0.5, 0.005)

plt.show()


plt.figure()

plt.plot(hlist, central_error, label="Central Difference")
plt.plot(hlist, five_point_error, label="Five-Point Difference")

plt.title("Central vs Five-Point Error")
plt.xlabel("Step Size (h)")
plt.ylabel("Absolute Error")

plt.legend()
plt.xlim(0.5, 0.005)

plt.show()


#Integration Experiment
c = 0.5
d = 1.5

gint = (27*np.log(27) - 26*np.log(8)-26) / 72


#nlist = integers from 10 to 100 in increments of 2 (Simpson needs even n)
nlist = list(range(10,101,2))

left_error = np.zeros(len(nlist), dtype=float)
right_error = np.zeros(len(nlist), dtype=float)
trapezoidal_error = np.zeros(len(nlist), dtype=float)
simpson_error = np.zeros(len(nlist), dtype=float)

for i, n in enumerate(nlist):
    left_approx = integrate.integ(g, c, d, n=n, mode=0)
    right_approx = integrate.integ(g, c, d, n=n, mode=1)
    trap_approx = integrate.integ(g, c, d, n=n, mode=2)
    simp_approx = integrate.integ(g, c, d, n=n, mode=3)

    left_error[i] = abs(left_approx - gint)
    right_error[i] = abs(right_approx - gint)
    trapezoidal_error[i] = abs(trap_approx - gint)
    simpson_error[i] = abs(simp_approx - gint)

# Plot 1: all four errors vs n
plt.figure()
plt.plot(nlist, left_error, label="left (mode 0)")
plt.plot(nlist, right_error, label="right (mode 1)")
plt.plot(nlist, trapezoidal_error, label="trapezoidal (mode 2)")
plt.plot(nlist, simpson_error, label="simpson (mode 3)")
plt.title("Integration error vs number of subintervals for g(x)=x^2 ln x on [0.5, 1.5]")
plt.xlabel("number of subintervals n")
plt.ylabel("absolute error |approx - exact|")
plt.legend()
plt.grid(True, linestyle=":")

# Plot 2: trapezoidal + Simpson only
plt.figure()
plt.plot(nlist, trapezoidal_error, label="trapezoidal (mode 2)")
plt.plot(nlist, simpson_error, label="simpson (mode 3)")
plt.title("Trapezoidal vs Simpson integration error on [0.5, 1.5]")
plt.xlabel("number of subintervals n")
plt.ylabel("absolute error |approx - exact|")
plt.legend()
plt.grid(True, linestyle=":")

plt.show()

input()

