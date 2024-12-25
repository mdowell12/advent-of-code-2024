from solutions.get_inputs import read_inputs


def run_1(inputs):
    reports = _parse_inputs(inputs)
    result = 0
    for report in reports:
        if _is_safe(report):
            result += 1
    return result


def run_2(inputs):
    reports = _parse_inputs(inputs)
    result = 0
    for report in reports:
        is_safe = _is_safe(report)
        if is_safe:
            result += 1
        else:
            for i in range(len(report)):
                without_i = report[:i] + report[i+1:]
                is_safe_without_i = _is_safe(without_i)
                if is_safe_without_i:
                    result += 1
                    break
    
    return result


def _is_safe(report):
    direction = None
    for i in range(1, len(report)):
        last = report[i-1]
        current = report[i]
        diff = current - last
        if not 1 <= abs(diff) <= 3:
            return False
        this_direction = 1 if diff >= 0 else -1
        if direction is None:
            direction = this_direction
        else:
            if this_direction != direction:
                return False
    return True


def _parse_inputs(inputs):
    results = []
    for line in inputs:
        results.append([int(i) for i in line.strip().split(' ')])
    return results


def run_tests():
    test_inputs = """
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
    """.strip().split('\n')

    result_1 = run_1(test_inputs)
    if result_1 != 2:
        raise Exception(f"Test 1 did not pass, got {result_1}")

    result_2 = run_2(test_inputs)
    if result_2 != 4:
        raise Exception(f"Test 2 did not pass, got {result_2}")


if __name__ == "__main__":
    run_tests()

    input = read_inputs(2)

    result_1 = run_1(input)
    print(f"Finished 1 with result {result_1}")

    result_2 = run_2(input)
    print(f"Finished 2 with result {result_2}")
