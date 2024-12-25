from solutions.get_inputs import read_inputs


def run_1(inputs):
    left, right = _parse_inputs(inputs)
    left = sorted(left)
    right = sorted(right)
    result = 0
    for i in range(len(left)):
        result += abs(left[i] - right[i])
    return result


def run_2(inputs):
    left, right = _parse_inputs(inputs)
    frequencies = {}
    for i in right:
        if i not in frequencies:
            frequencies[i] = 0
        frequencies[i] += 1
    
    result = 0
    for j in left:
        result += j * frequencies.get(j, 0)
    return result


def _parse_inputs(inputs):
    left, right = [], []
    for line in inputs:
        parts = [i for i in line.strip().split(' ') if i]
        left.append(int(parts[0]))
        right.append(int(parts[1]))
    return left, right


def run_tests():
    test_inputs = """
    3   4
    4   3
    2   5
    1   3
    3   9
    3   3
    """.strip().split('\n')

    result_1 = run_1(test_inputs)
    if result_1 != 11:
        raise Exception(f"Test 1 did not pass, got {result_1}")

    result_2 = run_2(test_inputs)
    if result_2 != 31:
        raise Exception(f"Test 2 did not pass, got {result_2}")


if __name__ == "__main__":
    run_tests()

    input = read_inputs(1)

    result_1 = run_1(input)
    print(f"Finished 1 with result {result_1}")

    result_2 = run_2(input)
    print(f"Finished 2 with result {result_2}")
