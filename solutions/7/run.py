from itertools import product

from solutions.get_inputs import read_inputs


def run_1(inputs):
    equations = _parse_inputs(inputs)
    result = 0
    for test_value, rights in equations:
        if _can_evaluate(test_value, rights):
            result += test_value
    return result


def run_2(inputs):
    equations = _parse_inputs(inputs)
    result = 0
    for test_value, rights in equations:
        if _can_evaluate_2(test_value, rights):
            result += test_value
            print(test_value, 'yes')
        else:
            print(test_value, 'no')
    return result


def _parse_inputs(inputs):
    return [(int(i.strip().split(':')[0]), tuple(int(j) for j in i.strip().split(':')[1].split(' ') if j)) for i in inputs]


def _can_evaluate(test_value, rights):
    combos = [i for i in product(['+', '*'], repeat=len(rights)-1)]
    for combo in combos:
        result = rights[0]
        for i in range(len(rights)-1):
            if combo[i] == '*':
                result *= rights[i+1]
            elif combo[i] == '+':
                result += rights[i+1]
            else:
                raise Exception(combo)
        if result == test_value:
            return True
    return False


def _can_evaluate_2(test_value, rights):
    combos = [i for i in product(['+', '*', '||'], repeat=len(rights)-1)]
    for combo in combos:
        result = rights[0]
        for i in range(len(rights)-1):
            if combo[i] == '*':
                result *= rights[i+1]
            elif combo[i] == '+':
                result += rights[i+1]
            elif combo[i] == '||':
                result = int(str(result) + str(rights[i+1]))
            else:
                raise Exception(combo)
        if result == test_value:
            return True
    return False


def run_tests():
    test_inputs = """
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
    """.strip().split('\n')

    result_1 = run_1(test_inputs)
    if result_1 != 3749:
        raise Exception(f"Test 1 did not pass, got {result_1}")

    result_2 = run_2(test_inputs)
    if result_2 != 11387:
        raise Exception(f"Test 2 did not pass, got {result_2}")


if __name__ == "__main__":
    run_tests()

    input = read_inputs(7)

    result_1 = run_1(input)
    print(f"Finished 1 with result {result_1}")

    result_2 = run_2(input)
    print(f"Finished 2 with result {result_2}")
