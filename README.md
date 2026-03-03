# Numerical-Calculus-Package


# Differentiate Module
The imported differentiate module contains four different differential methods, which can be accessed using the diff function.

0- _forward_diff
1- _backward_diff
2- _central_diff
3- _five_point_diff


```python
import numpy as np
from differentiate import diff

def f(x):
    return x**2
diff(f, x0, h, mode)

```

#Integrate function
