'''
The integrate folder will contain three
different methods of integration.

'''

import numpy as np

def _trapezoidal(f, a, b, n=100):
    """
    Approximate integral_a^b f(x) dx using the trapezoidal rule with n subintervals.

    Inputs:
      f : function handle (callable), f(x)
      a : left limit (number)
      b : right limit (number)
      n : number of subintervals (int, default 100)

    Output:
      Approximation to ∫_a^b f(x) dx 
    """
    n = int(n)
    if n <= 0:
        raise ValueError("n must be a positive integer.")
    h = (b - a) / n

    x0 = a
    xn = b
    s = 0.0
    for i in range(1, n):
        xi = a + i * h
        s += f(xi)

    return h * (0.5 * f(x0) + s + 0.5 * f(xn))


def _left(f, a, b, n=100):
    """
    Approximate integral_a^b f(x) dx using the left-endpoint Riemann sum.

    Inputs/Output: same as _trapezoidal
    """
    n = int(n)
    if n <= 0:
        raise ValueError("n must be a positive integer.")
    h = (b - a) / n

    s = 0.0
    for i in range(0, n):
        xi = a + i * h
        s += f(xi)

    return h * s


def _right(f, a, b, n=100):
    """
    Approximate integral_a^b f(x) dx using the right-endpoint Riemann sum.

    Inputs/Output: same as _trapezoidal
    """
    n = int(n)
    if n <= 0:
        raise ValueError("n must be a positive integer.")
    h = (b - a) / n

    s = 0.0
    for i in range(1, n + 1):
        xi = a + i * h
        s += f(xi)

    return h * s


def _simpson(f, a, b, n=100):
    """
    Approximate integral_a^b f(x) dx using Simpson's rule.

    Note: Simpson's rule requires n to be even.

    Inputs/Output: same as _trapezoidal
    """
    n = int(n)
    if n <= 0:
        raise ValueError("n must be a positive integer.")
    if n % 2 != 0:
        raise ValueError("Simpson's rule requires n to be even.")

    h = (b - a) / n

    s_odd = 0.0   # f(x1) + f(x3) + ... + f(x_{n-1})
    s_even = 0.0  # f(x2) + f(x4) + ... + f(x_{n-2})

    for i in range(1, n):
        xi = a + i * h
        if i % 2 == 1:
            s_odd += f(xi)
        else:
            s_even += f(xi)

    return (h / 3.0) * (f(a) + 4.0 * s_odd + 2.0 * s_even + f(b))


def integ(f, a, b, n=100, mode=2):
    """
    Numerically approximate integral_a^b f(x) dx.

    Inputs:
      f    : function handle (callable), f(x)
      a    : left limit
      b    : right limit
      n    : number of subintervals (int, default 100)
      mode : which method to use (int, default 2)
             0 -> _left
             1 -> _right
             2 -> _trapezoidal
             3 -> _simpson

    Output:
      Approximation to ∫_a^b f(x) dx (float)
    """
    if mode == 0:
        return _left(f, a, b, n)
    elif mode == 1:
        return _right(f, a, b, n)
    elif mode == 2:
        return _trapezoidal(f, a, b, n)
    elif mode == 3:
        return _simpson(f, a, b, n)
    else:
        raise ValueError("mode must be 0 (_left), 1 (_right), 2 (_trapezoidal), or 3 (_simpson).")