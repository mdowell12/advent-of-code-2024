from solutions.grid import Grid2D
from solutions.get_inputs import read_inputs


def run_1(inputs):
    rows = [list(line.strip()) for line in inputs]
    grid = Grid2D(rows)
    result = 0
    for (x, y), item in grid:
        attempts = [
            # right
            [(x+1, y), (x+2, y), (x+3, y)],
            # left
            [(x-1, y), (x-2, y), (x-3, y)],
            # down
            [(x, y+1), (x, y+2), (x, y+3)],
            # up
            [(x, y-1), (x, y-2), (x, y-3)],
            # down and right
            [(x+1, y+1), (x+2, y+2), (x+3, y+3)],
            # down and left
            [(x-1, y+1), (x-2, y+2), (x-3, y+3)],
            # up and right
            [(x+1, y-1), (x+2, y-2), (x+3, y-3)],
            # up and left
            [(x-1, y-1), (x-2, y-2), (x-3, y-3)]
        ]
        if item == 'X':
            for attempt in attempts:
                if grid.value_at_position(attempt[0]) == 'M' \
                    and grid.value_at_position(attempt[1]) == 'A' \
                    and grid.value_at_position(attempt[2]) == 'S':
                    result += 1
    return result


def run_2(inputs):
    rows = [list(line.strip()) for line in inputs]
    grid = Grid2D(rows)
    result = 0
    for (x, y), item in grid:
        if item == 'A':
            down_right = grid.value_at_position((x+1, y+1))
            up_left = grid.value_at_position((x-1, y-1))
            if (down_right == 'M' and up_left == 'S') or (up_left == 'M' and down_right == 'S'):
                down_left = grid.value_at_position((x-1, y+1))
                up_right = grid.value_at_position((x+1, y-1))
                if (down_left == 'M' and up_right == 'S') or (up_right == 'M' and down_left == 'S'):
                    result += 1        
    return result


def run_tests():
    test_inputs = """
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
    """.strip().split('\n')

    result_1 = run_1(test_inputs)
    if result_1 != 18:
        raise Exception(f"Test 1 did not pass, got {result_1}")

    result_2 = run_2(test_inputs)
    if result_2 != 9:
        raise Exception(f"Test 2 did not pass, got {result_2}")


if __name__ == "__main__":
    run_tests()

    input = read_inputs(4)

    result_1 = run_1(input)
    print(f"Finished 1 with result {result_1}")

    result_2 = run_2(input)
    print(f"Finished 2 with result {result_2}")
