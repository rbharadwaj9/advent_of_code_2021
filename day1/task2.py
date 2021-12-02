import numpy as np
import sys

def main(args=sys.argv):
    try:
        filename = args[1]
    except IndexError:
        print("Please provide file")
        sys.exit()

    input = []
    with open(filename, 'r') as f:
        for line in f:
            input.append(float(line));

    prev = input[0]+input[1]+input[2]
    res = 0;
    [0, 1, 2, 3]
    for i in range(3, len(input)):
        curr = prev - input[i-3]
        curr += input[i];
        if (curr > prev):
            res += 1
        prev = curr
    print(res)

if __name__ == "__main__":
    main()

