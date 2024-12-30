from itertools import combinations

from solutions.get_inputs import read_inputs
from solutions.grid import Grid2D


def run_1(inputs):
    return _run(inputs, _find_antinodes)


def run_2(inputs):
    return _run(inputs, _find_antinodes_2)


def _run(inputs, find_antinodes_fn):
    grid = Grid2D([i for i in inputs])

    antennaes = {}
    for position, value in grid:
        if value != '.':
            if value not in antennaes:
                antennaes[value] = set()
            antennaes[value].add(position)
    
    antinodes = set()
    for positions in antennaes.values():
        pairs = combinations(positions, 2)
        for left, right in pairs:
            antinodes_for_pair = find_antinodes_fn(left, right, grid)
            antinodes = antinodes.union(antinodes_for_pair)
    
    return len(antinodes)


def _find_antinodes(left, right, grid):
    (left_x, left_y), (right_x, right_y) = left, right
    distance_x = left_x - right_x
    distance_y = left_y - right_y
    
    if distance_x < 0 and distance_y < 0:
        # Down and right
        antinodes = {(left_x + abs(distance_x) * 2, left_y + abs(distance_y) * 2), 
                     (left_x - abs(distance_x), left_y - abs(distance_y))}
    elif distance_x >= 0 and distance_y < 0:
        # Down and left
        antinodes = {(left_x - abs(distance_x) * 2, left_y + abs(distance_y) * 2), 
                     (left_x + abs(distance_x), left_y - abs(distance_y))}
    elif distance_x >= 0 and distance_y >= 0:
        # Up and left
        antinodes = {(left_x - abs(distance_x) * 2, left_y - abs(distance_y) * 2), 
                     (left_x + abs(distance_x), left_y + abs(distance_y))}
    elif distance_x < 0 and distance_y >= 0:
        # Up and right
        antinodes = {(left_x + abs(distance_x) * 2, left_y - abs(distance_y) * 2), 
                     (left_x - abs(distance_x), left_y + abs(distance_y))}

    return set(a for a in antinodes if grid.position_is_in_grid(a))

def _find_antinodes_2(left, right, grid):
    (left_x, left_y), (right_x, right_y) = left, right
    distance_x = left_x - right_x
    distance_y = left_y - right_y
    
    if distance_x < 0 and distance_y < 0:
        # Down and right
        mult = ((1, 1), (-1, -1))
    elif distance_x >= 0 and distance_y < 0:
        # Down and left
        mult = ((-1, 1), (1, -1))
    elif distance_x >= 0 and distance_y >= 0:
        # Up and left
        mult = ((-1, -1), (1, 1))
    elif distance_x < 0 and distance_y >= 0:
        # Up and right
        mult = ((1, -1), (-1, 1))

    antinodes = set()

    position = left
    i = 0
    while grid.position_is_in_grid(position):
        antinodes.add(position)
        i += 1
        position = (left_x + abs(distance_x)*i*mult[0][0], left_y + abs(distance_y)*i*mult[0][1])

    position = left
    i = 0
    while grid.position_is_in_grid(position):
        antinodes.add(position)
        i += 1
        position = (left_x + abs(distance_x)*i*mult[1][0], left_y + abs(distance_y)*i*mult[1][1])

    return antinodes


def run_tests():
    test_inputs = """
............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
    """.strip().split('\n')

    result_1 = run_1(test_inputs)
    if result_1 != 14:
        raise Exception(f"Test 1 did not pass, got {result_1}")

    result_2 = run_2(test_inputs)
    if result_2 != 34:
        raise Exception(f"Test 2 did not pass, got {result_2}")


if __name__ == "__main__":
    run_tests()

    input = read_inputs(8)

    result_1 = run_1(input)
    print(f"Finished 1 with result {result_1}")

    result_2 = run_2(input)
    print(f"Finished 2 with result {result_2}")
