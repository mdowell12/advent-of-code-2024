from solutions.get_inputs import read_inputs


def run_1(inputs):
    result = 0
    for line in inputs:
        result += _process_line(line)
    return result


def run_2(inputs):
    result = 0
    for line in inputs:
        result += _process_line(line, always_do=False)
    return result


def _process_line(line, always_do=True):
    result = 0
    i = 0
    is_on = True
    while i < len(line):
        if line[i:i+4] == 'mul(':
            product, end_i = _parse_mul(line, i)

            if (always_do or is_on) and product is not None:
                result += product

            if end_i is not None:
                i = end_i + 1
            else:
                i += 4

        elif line[i:i+4] == 'do()':
            is_on = True
            i += 4
            print(line[i-8:i], line[i:i+8], is_on)
            # import pdb; pdb.set_trace()
        elif line[i:i+7] == "don't()":
            is_on = False
            i += 7
            print(line[i-8:i], line[i:i+8], is_on)
            # import pdb; pdb.set_trace()
        else:
            i += 1
    return result


def _parse_mul(line, i):
    left_digit, length = _get_digit(line, i+4)
    if left_digit is not None:
        comma = i+3+length+1
        if len(line) >= comma and line[comma] == ',':
            right_digit, length = _get_digit(line, comma+1)        
            if right_digit is not None and len(line) >= comma+length+1 and line[comma+length+1] == ')':
                result = left_digit * right_digit
                i = comma+length+1
                return result, i
    return None, None


def _get_digit(line, start):
    digits = ''
    i = start
    while i < len(line):
        if line[i].isdigit():
            digits = digits + line[i]
            i += 1
        else:
            break
    return (int(digits), i - start) if digits else (None, None)


def run_tests():
    test_inputs = """
xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
    """.strip().split('\n')

    result_1 = run_1(test_inputs)
    if result_1 != 161:
        raise Exception(f"Test 1 did not pass, got {result_1}")
    
    test_inputs = """
xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
    """.strip().split('\n')

    result_2 = run_2(test_inputs)
    if result_2 != 48:
        raise Exception(f"Test 2 did not pass, got {result_2}")


if __name__ == "__main__":
    run_tests()

    input = read_inputs(3)

    result_1 = run_1(input)
    print(f"Finished 1 with result {result_1}")

    result_2 = run_2(input)
    # 106762851 too high
    # 107991598 is too high
    print(f"Finished 2 with result {result_2}")
