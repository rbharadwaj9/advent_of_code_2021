import numpy as np
import sys

def main(args=sys.argv):
    try:
        filename = args[1]
    except IndexError:
        print("Please provide file")
        sys.exit()

    res = 0
    prev = np.Infinity
    with open(filename, 'r') as f:
        for val in f:
            if (float(val) > prev):
                res += 1
            prev = float(val)
    print(res)

if __name__ == "__main__":
    main()
