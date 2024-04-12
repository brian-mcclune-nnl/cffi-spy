import argparse
import math
import sys
from typing import List

from _approx_pi import lib


def main(argv: List[str] = sys.argv[1:]):
    """Runs the Pi approximator for profiling demonstration.

    Args:
        argv: The list of command line arguments.
    """
    parser = argparse.ArgumentParser(description='Pi approximator')
    parser.add_argument(
        '-w', '--wallis', action='store_true',
        help='use wallis product only')
    parser.add_argument(
        '-l', '--leibniz', action='store_true',
        help='use leibniz formula only')
    parser.add_argument(
        'iterations', type=int, help='iterations count for formula or product')

    args = parser.parse_args(argv)
    if not args.wallis:
        approx_pi('leibniz', args.iterations)
    if not args.leibniz:
        approx_pi('wallis', args.iterations)


def approx_pi(method: str, iterations: int):
    """Runs the approximator function specified by `method`.

    Args:
        method: The name of the method to use.
        iterations: Max number of iterations to run.
    """
    approx_pi_func = getattr(lib, method)
    for log_iteration in range(math.ceil(math.log10(iterations))):
        iteration = 10 ** log_iteration
        approx_pi = approx_pi_func(iteration)
        print(
            f'Approximate value of pi ({method} method, '
            f'{iteration} iterations): {approx_pi}')
    approx_pi = approx_pi_func(iterations)
    print(
        f'Approximate value of pi ({method} method, '
        f'{iterations} iterations): {approx_pi}')


if __name__ == '__main__':
    main()
