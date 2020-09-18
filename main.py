import numpy
import timeit

from ch2 import insertionSort


def time(n):
    pass


if __name__ == '__main__':

    for n in [1e1, 1e2, 1e3, 1e4]:
        A = numpy.random.randint(0, 100, int(n))
        print(
            f"n={n}",
            timeit.timeit(
                'insertionSort(A)', 'from __main__ import insertionSort, A', number=1),
            "seconds")
