from solutions.get_inputs import read_inputs


def run_1(inputs):
    rules, updates = _parse_inputs(inputs)

    must_precede = _build_precedes(rules)
    
    
    correct = []
    for update in updates:
        pages = [i for i in update]
        seen = set()
        valid = True
        while pages and valid:
            page = pages.pop(0)
            for p in must_precede.get(page, []):
                if p in seen:
                    valid = False
            seen.add(page)
        if valid:
            correct.append(update)
    
    result = 0
    for update in correct:
        result += update[len(update) // 2]
    return result


def run_2(inputs):
    rules, updates = _parse_inputs(inputs)

    must_precede = _build_precedes(rules)

    incorrect = []
    for update in updates:
        fixed, did_fix = fix(update, must_precede)
        if did_fix:
            while did_fix:
                fixed, did_fix = fix(fixed, must_precede)
            incorrect.append(fixed)

    result = 0
    for update in incorrect:
        result += update[len(update) // 2]
    return result


def fix(update, must_precede):
    pages = [i for i in update]
    seen = []
    while pages:
        page = pages.pop(0)
        for p in must_precede.get(page, []):
            if p in seen:
                seen.remove(p)
                return seen + [page] + [p] + pages, True
        seen.append(page)
    return update, False


def _parse_inputs(inputs):
    rules = [i for i in inputs if '|' in i]
    updates = [[int(j) for j in i.strip().split(',')] for i in inputs if ',' in i]
    return rules, updates


def _build_precedes(rules):
    must_precede = {}
    for rule in rules:
        left, right = [int(i) for i in rule.strip().split('|', 2)]
        if left not in must_precede:
            must_precede[left] = []
        must_precede[left].append(right)
    return must_precede


def run_tests():
    test_inputs = """
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
    """.strip().split('\n')

    result_1 = run_1(test_inputs)
    if result_1 != 143:
        raise Exception(f"Test 1 did not pass, got {result_1}")

    result_2 = run_2(test_inputs)
    if result_2 != 123:
        raise Exception(f"Test 2 did not pass, got {result_2}")


if __name__ == "__main__":
    run_tests()

    input = read_inputs(5)

    result_1 = run_1(input)
    print(f"Finished 1 with result {result_1}")

    result_2 = run_2(input)
    print(f"Finished 2 with result {result_2}")
