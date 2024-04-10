import argparse
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
        help='use wallis product rather than leibniz formula')
    parser.add_argument(
        'iterations', type=int, help='iterations count for formula or product')

    args = parser.parse_args(argv)
    if args.wallis:
        method = 'wallis'
        approx_pi = lib.wallis(args.iterations)
    else:
        method = 'leibniz'
        approx_pi = lib.leibniz(args.iterations)

    print(
        f'Approximate value of pi ({method} method, '
        f'{args.iterations} iterations): {approx_pi}')


if __name__ == '__main__':
    main()
