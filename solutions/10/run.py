from solutions.get_inputs import read_inputs
from solutions.grid import Grid2D


def run_1(inputs):
    grid = Grid2D([i.strip() for i in inputs], map_fn=int)
    trailheads = grid.positions_from_value(0)
    result = 0
    for trailhead in trailheads:
        result += _score_trailhead(grid, trailhead)
    return result


def run_2(inputs):
    grid = Grid2D([i.strip() for i in inputs], map_fn=int)
    trailheads = grid.positions_from_value(0)
    result = 0
    for trailhead in trailheads:
        result += _rate_trailhead(grid, trailhead)
    return result


def _score_trailhead(grid, trailhead):
    reachable_nines = set()
    # [current position, {previous path including this position}]
    queue = [(trailhead, {trailhead,})]
    while queue:
        position, previous_path = queue.pop(0)
        x, y = position
        current_value = grid.value_at_position(position)
        for next_position in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
            next_value = grid.value_at_position(next_position)
            if next_position in previous_path:
                continue
            if next_value == current_value + 1:
                if next_value == 9:
                    reachable_nines.add(next_position)
                else:
                    queue.append((next_position, previous_path.union({next_position,})))
            else:
                continue
    return len(reachable_nines)


def _rate_trailhead(grid, trailhead):
    unique_trails = set()
    # [current position, [previous path including this position]]
    queue = [(trailhead, [trailhead,])]
    while queue:
        position, previous_path = queue.pop(0)
        x, y = position
        current_value = grid.value_at_position(position)
        for next_position in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
            next_value = grid.value_at_position(next_position)
            if next_value == current_value + 1:
                updated_path = previous_path + [next_position]
                if next_value == 9:
                    unique_trails.add(''.join(str(i) for i in updated_path))
                else:
                    queue.append((next_position, updated_path))
            else:
                continue
    return len(unique_trails)


def run_tests():
    test_inputs = """
0123
1234
8765
9876
    """.strip().split('\n')

    result_1 = run_1(test_inputs)
    if result_1 != 1:
        raise Exception(f"Test 0 did not pass, got {result_1}")

    test_inputs = """
89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732
    """.strip().split('\n')

    result_1 = run_1(test_inputs)
    if result_1 != 36:
        raise Exception(f"Test 1 did not pass, got {result_1}")

    result_2 = run_2(test_inputs)
    if result_2 != 81:
        raise Exception(f"Test 2 did not pass, got {result_2}")


if __name__ == "__main__":
    run_tests()

    input = read_inputs(10)

    result_1 = run_1(input)
    print(f"Finished 1 with result {result_1}")

    result_2 = run_2(input)
    print(f"Finished 2 with result {result_2}")
