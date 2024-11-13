# The main function provides a commandline interface for the package.
# This way you can use it via python -m modulename.

# Include necessary modules.
# User defined modules.
from pymatroh import intmatrix as imat
# Std modules.
import argparse

def main():
    """Parameter declaration."""
    # Declaring parameters.
    parser = argparse.ArgumentParser()
    arggroup = parser.add_argument_group(title = "IntMatrix")
    arggroup.add_argument("-row", "--row", type=int, help=("Row count."))
    arggroup.add_argument("-col", "--column", type=int, help=("Column count."))
    arggroup.add_argument("-irng", "--irange", type=int, help=("Integer range. Default = 100."))

    args = parser.parse_args()

    #Catching parameters.
    if args.row and args.column and not args.irange:
        im = imat.IntMatrix(args.row, args.column)
        print(im.create_matrix())
    elif args.row and args.column and args.irange:
        im = imat.IntMatrix(args.row, args.column, args.irange)
        print(im.create_matrix())

if __name__ == '__main__':
    main()