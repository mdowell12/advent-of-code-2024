from solutions.get_inputs import read_inputs


def run_1(inputs):
    disk_map = [int(i) for i in inputs[0].strip()]
    leftmost_free = disk_map[0]
    rightmost_value = -1
    memory = {}
    file_id = 0
    for i, value in enumerate(disk_map):
        is_file = i % 2 == 0
        if is_file:
            for j in range(value):
                memory[rightmost_value + 1 + j] = file_id
            rightmost_value = rightmost_value + 1 + j
            file_id += 1
        else:
            rightmost_value += value

    num_occupied = len(memory)
    while leftmost_free < num_occupied:
        leftmost_free, rightmost_value, memory = _reorder(leftmost_free, rightmost_value, memory)
            
    return _checksum(memory, leftmost_free)


def run_2(inputs):
    disk_map = [int(i) for i in inputs[0].strip()]
    files = []
    file_id = 0
    rightmost_value = -1
    for i, value in enumerate(disk_map):
        is_file = i % 2 == 0
        if is_file:
            left = rightmost_value + 1
            right = left + value - 1
            files.append((file_id, (left, right)))
            rightmost_value = right
            file_id += 1
        else:
            rightmost_value += value

    files_copy = [i for i in files]

    for f in range(file_id-1, 0, -1):
        file_begin, file_end = files[f][1][0], files[f][1][1]
        file_length = file_end - file_begin + 1
        other_file_end = files_copy[0][1][1]
        i = 0
        while other_file_end < file_begin:
            i += 1
            next_file = files_copy[i]
            gap_size = next_file[1][0] - other_file_end - 1
            if gap_size >= file_length:
                moved_file_id = files[f][0]
                moved_file = (moved_file_id, (other_file_end + 1, other_file_end + file_length))
                files_copy = files_copy[:i] + [moved_file] + [j for j in files_copy[i:] if j[0] != moved_file_id]
                break
            else:
                other_file_end = next_file[1][1]
    
    result = 0
    for file_id, (start, end) in files_copy:
        for i in range(start, end+1):
            result += i*file_id
    return result


def _reorder(leftmost_free, rightmost_value, memory):
    val = memory[rightmost_value]
    del memory[rightmost_value]

    while rightmost_value not in memory:
        rightmost_value -= 1

    memory[leftmost_free] = val
    
    while leftmost_free in memory:
        leftmost_free += 1

    return leftmost_free, rightmost_value, memory


def _checksum(memory, leftmost_free):
    result = 0
    for i in range(leftmost_free):
        result += i*memory[i]
    return result


def _print_memory(memory):
    max_position = max(memory.keys())
    result = ''
    for i in range(max_position + 1):
        result += str(memory.get(i, '.'))
    print(result)


def run_tests():
    test_inputs = """
2333133121414131402
    """.strip().split('\n')

    result_1 = run_1(test_inputs)
    if result_1 != 1928:
        raise Exception(f"Test 1 did not pass, got {result_1}")

    result_2 = run_2(test_inputs)
    if result_2 != 2858:
        raise Exception(f"Test 2 did not pass, got {result_2}")


if __name__ == "__main__":
    run_tests()

    input = read_inputs(9)

    result_1 = run_1(input)
    print(f"Finished 1 with result {result_1}")

    result_2 = run_2(input)
    print(f"Finished 2 with result {result_2}")
