#!/usr/bin/python3

if __name__ == "__main__":
    """Print the addition of all arguments."""
    import sys

    total = sum(int(sys.argv[i + 1]) for i in range(len(sys.argv) - 1))
    print(f"{total}")
