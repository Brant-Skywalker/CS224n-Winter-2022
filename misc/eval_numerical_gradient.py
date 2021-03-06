import numpy as np


def eval_numerical_gradient(f, x):
    """
    A naive implementation of numerical gradient of f at x
    :param f: a function that takes a single argument
    :param x: the point (numpy array) to evaluate the gradient at
    :return: numerical gradient (numpy array)
    """
    fx = f(x)  # evaluate function value at original point
    grad = np.zeros(x.shape)
    h = 0.00001

    # iterate over all indexes in x
    it = np.nditer(x, flags=["multi_index"], op_flags=["readwrite"])

    while not it.finished:
        # evaluate function at x+h
        ix = it.multi_index
        old_value = x[ix]
        x[ix] = old_value + h  # increment by h
        fxh_left = f(x)  # evaluate f(x + h)
        x[ix] = old_value - h  # decrement by h
        fxh_right = f(x)  # evaluate f(x - h)
        x[ix] = old_value  # restore to previous value (very important!)

        # compute the partial derivative
        grad[ix] = (fxh_left - fxh_right) / (2 * h)  # the slope
        it.iternext()  # step to next dimension

        return grad
