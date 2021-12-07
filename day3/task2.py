import numpy as np
import sys


def _find_most_or_least_common(input: np.ndarray, most: bool) -> np.ndarray:
    # Number of 1 occurances
    num_ones = np.sum(input, axis=0, keepdims=True)
    if most:
        return (num_ones >= (len(input)/2)).astype(int).squeeze()
    return (num_ones < (len(input)/2)).astype(int).squeeze()


def _convert_np_to_int(arr: np.ndarray) -> int:
    res = 0
    for e in arr:
        res *= 2
        res += e
    return res


def determine_rating(input, oxygen: bool) -> int:
    num_bits = input.shape[1]
    for i in range(num_bits):
        if len(input) == 1:
            break
        common = _find_most_or_least_common(input, oxygen)
        input = input[input[:, i] == common[i], :]
    return _convert_np_to_int(input.squeeze())

def main(args=sys.argv):
    try:
        filename = args[1]
    except IndexError:
        print("Please provide file")
        sys.exit()

    input = []
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            input.append(np.array([int(c) for c in line]))
    input = np.array(input)

    oxygen = determine_rating(input, True)
    co2 = determine_rating(input, False)
    print(f"Oxygen Rating = {oxygen}")
    print(f"CO2 Rating = {co2}")
    print(f"Life support rating = {oxygen * co2}")




if __name__ == "__main__":
    main()
