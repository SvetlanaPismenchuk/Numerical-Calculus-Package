'''
The differentiate file will compose of five different differential
functions, each accepting the same three parameters with an exception,
function diff has a fourth parameter "mode".

The three parameters are:
f - function handle
x0 - center
h - optional step size h, set at default 0.01

Exception Parameter
mode- range (0-3)


The five different functions are:

_forward_diff() - Implements the forward 
difference approximation

_backward_diff()- Implements the backward 
difference approximation 

_central_diff()- Implements the central 
difference approximation

_five_point_diff()- Implements the five-point 
central difference approximation

diff() - lets user choose which function to return
'''






def _forward_diff(f, x0, h=0.01):
    return (f(x0 + h) - f(x0)) / h

def _backward_diff(f, x0, h=0.01):
    return (f(x0) - f(x0 - h)) / h

def _central_diff(f, x0, h=0.01):
    return (f(x0 + h) - f(x0 - h)) / (2*h)


def _five_point_diff(f, x0, h=0.01):
    return (
        f(x0 - 2*h)
        - 8*f(x0 - h)
        + 8*f(x0 + h)
        - f(x0 + 2*h)
    ) / (12*h)

def diff(f, x0, h=0.01, mode=0):

    '''
    All of the four functions have three parameters (f,x0, h = 0.01).

    The three parameters are:
    f - function handle
    x0 - center
    h - optional step size h, set at default 0.01

    Function diff has an additional parameter mode, which is 
    used to choose which differentiating function the user
    wants to use.

    Mode Choices:
    0 - _forward_diff
    1- _backward_diff
    2- _central_diff
    3- _five_point_diff

    '''

    if mode == 0:
        return _forward_diff(f, x0, h)

    elif mode == 1:
        return _central_diff(f, x0, h)

    elif mode == 2:
        return _backward_diff(f, x0, h)

    elif mode == 3:
        return _five_point_diff(f, x0, h)

    else:
        return "Please enter a number 0-3."