import numpy as np
import sys

# Represent 2d coordinate: (2x1) horizontal, depth
def _parse_and_update(cmd_string: str, curr: np.ndarray, aim: int):
    action, amt = cmd_string.strip().split(" ")
    amt = int(amt)

    if (action == "forward"):
        curr += np.array([[amt, aim*amt]])
    elif (action == "down"):
        aim += amt
    elif (action == "up"):
        aim -= amt
    else:
        raise Exception("Unknown Command")
    return curr, aim
        

def main(args=sys.argv):
    try:
        filename = args[1]
    except IndexError:
        print("Please provide file")
        sys.exit()

    with open(filename, 'r') as f:
        curr = np.zeros((1, 2))
        aim = 0
        for val in f:
            curr, aim = _parse_and_update(val, curr, aim)

    print(curr)

    ans = curr[0, 0] * curr[0, 1]
    print(f'Answer is {ans}')

if __name__ == "__main__":
    main()

