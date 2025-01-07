from solutions.get_inputs import read_inputs


def run_1(inputs, iter=25):
    stones = {}
    for i in inputs[0].strip().split(' '):
        value = int(i)
        if value not in stones:
            stones[value] = 0
        stones[value] += 1

    for _ in range(iter):
        new_stones = {}
        for stone, freq in stones.items():
            stone_string = str(stone)
            if stone == 0:
                new_stones[1] = new_stones.get(1, 0) + freq
            elif len(stone_string) % 2 == 0:
                left = stone_string[:len(stone_string)//2]
                right = stone_string[len(stone_string)//2:]
                new_stones[int(left)] = new_stones.get(int(left), 0) + freq
                new_stones[int(right)] = new_stones.get(int(right), 0) + freq
            else:
                new_stones[stone * 2024] = new_stones.get(stone * 2024, 0) + freq
        stones = new_stones

    return sum(stones.values())


def run_tests():
    test_inputs = """
125 17
    """.strip().split('\n')

    result_1 = run_1(test_inputs, iter=6)
    if result_1 != 22:
        raise Exception(f"Test 1 did not pass, got {result_1}")
    
    result_1 = run_1(test_inputs)
    if result_1 != 55312:
        raise Exception(f"Test 1.1 did not pass, got {result_1}")


if __name__ == "__main__":
    run_tests()

    input = read_inputs(11)

    result_1 = run_1(input)
    print(f"Finished 1 with result {result_1}")

    result_2 = run_1(input, iter=75)
    print(f"Finished 2 with result {result_2}")
