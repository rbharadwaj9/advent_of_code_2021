import numpy as np
import sys

def _update_num_ones(num_ones: np.ndarray, input_str: str):
    for i, c in enumerate(input_str):
        num_ones[i] += (1 if c == '1' else 0)
    return num_ones

def _convert_np_to_int(arr: np.ndarray):
    res = 0
    for e in arr:
        res *= 2
        res += e
    return res

def main(args=sys.argv):
    try:
        filename = args[1]
    except IndexError:
        print("Please provide file")
        sys.exit()

    num_ones = np.zeros(10)
    total_count = 0
    with open(filename, 'r') as f:
        checked = False
        for val in f:
            val = val.strip()
            # ensure that num ones is wide enough. Also check this only once
            if not checked and len(val) != num_ones.shape[0]:
                checked = True
                num_ones = np.zeros(len(val))
            checked = True

            num_ones = _update_num_ones(num_ones, val)
            total_count += 1

    gamma_arr = (num_ones > (total_count/2)).astype(int)
    gamma = _convert_np_to_int(gamma_arr)
    total = (2 ** len(gamma_arr) - 1)
    epsilon = total - gamma

    print(f"Ans: {gamma*epsilon}")


if __name__ == "__main__":
    main()
