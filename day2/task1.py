import numpy as np
import sys

# Represent 2d coordinate: (2x1) horizontal, depth
def _parse_and_update(cmd_string: str, curr: np.ndarray):
    action, amt = cmd_string.strip().split(" ")
    amt = int(amt)

    if (action == "forward"):
        curr += np.array([[amt, 0]])
    elif (action == "down"):
        curr += np.array([[0, amt]])
    elif (action == "up"):
        curr += np.array([[0, -amt]])
    else:
        raise Exception("Unknown Command")
    return curr
        

def main(args=sys.argv):
    try:
        filename = args[1]
    except IndexError:
        print("Please provide file")
        sys.exit()

    with open(filename, 'r') as f:
        curr = np.zeros((1, 2))
        for val in f:
            curr = _parse_and_update(val, curr)

    print(curr)

    ans = curr[0, 0] * curr[0, 1]
    print(f'Answer is {ans}')

if __name__ == "__main__":
    main()
