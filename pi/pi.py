import random
from tqdm import tqdm


def pi(S: int = int(1e6)):
    """Calculate the value of π.

    Args:
        S (int, optional): Total experiment times of Monte Carlo method. Defaults to int(1e6).

    Returns:
        float: Value of π.
    """
    N = 0
    for i in tqdm(range(S)):
        x = random.random()
        y = random.random()
        d = (x-0.5)**2+(y-0.5)**2
        if d <= 0.5**2:
            N += 1
        else:
            pass
    PI = 4*N/S
    return PI


if __name__ == '__main__':
    print(pi())
