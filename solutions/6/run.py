from solutions.get_inputs import read_inputs
from solutions.grid import Grid2D


DIRECTION_FACTORS = {
    '>': (1, 0),
    '<': (-1, 0),
    'v': (0, 1),
    '^': (0, -1),
}

DIRECTION_NEXT = {
    '>': 'v',
    '<': '^',
    'v': '<',
    '^': '>',
}


def run_1(inputs):
    grid = Grid2D([i.strip() for i in inputs])
    position, direction = _get_initial_position_and_value(grid)
    visited = set()
    while True:
        positions, exited_grid = _visit_next_positions(position, direction, grid)
        for p in positions:
            visited.add(p)
        if exited_grid:
            return len(visited)
        else:
            position = positions[-1]
            direction = DIRECTION_NEXT[direction]
    raise Exception()


def run_2(inputs):
    grid = Grid2D([i.strip() for i in inputs])
    start, direction = _get_initial_position_and_value(grid)
    result = 0
    # print(grid)
    for position, _ in grid:
        print(position)
        if _is_loop(grid, start, direction, position):
            result += 1
    return result


def _is_loop(grid, position, direction, new_obstacle):
    value = grid.value_at_position(new_obstacle)
    if value != '.':
        return False
    visited = set()
    while True:
        positions, exited_grid = _visit_next_positions(position, direction, grid, new_obstacle=new_obstacle)
        if exited_grid:
            return False
        for p in positions:
            if (p, direction) in visited:
                return True
            visited.add((p, direction))
        
        position = positions[-1] if positions else position
        direction = DIRECTION_NEXT[direction]
    
    raise Exception()


def _visit_next_positions(position, direction, grid, new_obstacle=None):
    visited = []
    while True:
        factor_x, factor_y = DIRECTION_FACTORS[direction]
        position = (position[0] + 1*factor_x, position[1] + 1*factor_y)
        next_value = grid.value_at_position(position) if position != new_obstacle else '#'
        if next_value is None:
            return visited, True
        elif next_value == '#':
            return visited, False
        else:
            visited.append(position)


def _get_initial_position_and_value(grid):
    for pos, value in grid:
        if value in {'>', '<', '^', 'v'}:
            return pos, value
    raise Exception(str(grid))


def run_tests():
    test_inputs = """
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
    """.strip().split('\n')

    result_1 = run_1(test_inputs)
    if result_1 != 41:
        raise Exception(f"Test 1 did not pass, got {result_1}")

    result_2 = run_2(test_inputs)
    if result_2 != 6:
        raise Exception(f"Test 2 did not pass, got {result_2}")


if __name__ == "__main__":
    run_tests()

    input = read_inputs(6)

    result_1 = run_1(input)
    print(f"Finished 1 with result {result_1}")

    result_2 = run_2(input)
    print(f"Finished 2 with result {result_2}")
