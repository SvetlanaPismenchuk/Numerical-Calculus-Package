# Numerical-Calculus-Package (Week 7)

## Differentiate (differentiate.py)

This repo contains a small Python module called differentiate.py that approximates derivatives using numerical differentiation.

The module includes four internal helper methods:
- _forward_diff
- _backward_diff
- _central_diff
- _five_point_diff

You should not call those helper functions directly. Instead, use the public function diff(), which selects a method using the mode argument:
- mode = 0: forward difference
- mode = 1: backward difference
- mode = 2: central difference
- mode = 3: five-point central difference

In `experiment.py`, the test function is:

- `g(x) = x^2 ln(x)`
- center point `a = 2`
- exact derivative at `a = 2` is stored as `gprime = 2 + 4 ln(2)`

Then the script creates a list of step sizes `hlist` and computes absolute errors for each mode:

```python
import numpy as np
import matplotlib.pyplot as plt
from differentiate import diff

def g(x):
    return (x**2 * np.log(x))

a = 2
gprime = 2 + 4 * np.log(2)

hlist = np.linspace(0.005, 0.5, 100)

forward_error = np.abs([diff(g, a, h=h, mode=0) for h in hlist] - gprime)
backward_error = np.abs([diff(g, a, h=h, mode=2) for h in hlist] - gprime)
central_error = np.abs([diff(g, a, h=h, mode=1) for h in hlist] - gprime)
five_point_error = np.abs([diff(g, a, h=h, mode=3) for h in hlist] - gprime)
```

What the plots show

The experiment produces two plots:

All methods vs step size

Forward, Backward, Central, and Five-Point error curves are plotted on the same figure.

The x-axis is reversed, so smaller step sizes appear to the right.

Central vs Five-Point

Only Central and Five-Point errors are plotted to compare the two most accurate methods.

These plots show how the numerical derivative accuracy changes depending on both the method (mode) and the chosen step size h.


##Integrate module (integrate.py)
The `integrate.py` file provides an `integ` function that numerically approximates a definite integral on an interval \([a,b]\). It is used in `experiment.py` to compare how the error changes as the number of subintervals `n` increases.

### What `integ` takes

`integ(f, a, b, n=100, mode=2)`

- `f`: function handle (a Python function), like `f(x)`
- `a`: lower limit of integration
- `b`: upper limit of integration
- `n`: number of subintervals (default `100`)
- `mode`: chooses the method (0–3)

### Mode choices (matches experiment.py)

- mode = 0: Left Riemann Sum  
- mode = 1: Right Riemann Sum  
- mode = 2: Trapezoidal Rule  
- mode = 3: Simpson’s Rule   

### How it’s used in the experiment

In `experiment.py`, the test function is:

- `g(x) = x^2 ln(x)`
- interval is `[c, d] = [0.5, 1.5]`
- the exact integral value is stored as `gint`

The script tests multiple `n` values (from 10 to 100, step 2) and computes the absolute error for each method:

```python
import numpy as np
import matplotlib.pyplot as plt
from integrate import integ

def g(x):
    return (x**2 * np.log(x))

c = 0.5
d = 1.5

# exact integral value 
gint = (27*np.log(27) - 26*np.log(8) - 26) / 72

nlist = list(range(10, 101, 2))

left_error = np.zeros(len(nlist))
right_error = np.zeros(len(nlist))
trapezoidal_error = np.zeros(len(nlist))
simpson_error = np.zeros(len(nlist))

for i, n in enumerate(nlist):
    left_approx = integ(g, c, d, n=n, mode=0)
    right_approx = integ(g, c, d, n=n, mode=1)
    trap_approx = integ(g, c, d, n=n, mode=2)
    simp_approx = integ(g, c, d, n=n, mode=3)

    left_error[i] = abs(left_approx - gint)
    right_error[i] = abs(right_approx - gint)
    trapezoidal_error[i] = abs(trap_approx - gint)
    simpson_error[i] = abs(simp_approx - gint)
```
What the plots show

The experiment produces two plots:

All methods vs number of subintervals

Left, Right, Trapezoidal, and Simpson errors are plotted on the same figure.

This shows how accuracy improves as n increases (more subintervals = finer approximation).

Trapezoidal vs Simpson

Only Trapezoidal and Simpson errors are plotted.

This highlights the two most accurate integration methods and makes it easier to compare them.

Overall, the plots demonstrate that increasing n generally decreases error, and higher-order methods (especially Simpson’s) typically converge faster than left/right sums.
