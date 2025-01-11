from solutions.get_inputs import read_inputs
from solutions.grid import Grid2D


def run_1(inputs):
    grid = Grid2D([i.strip() for i in inputs])
    regions = _create_regions(grid)
    
    result = 0
    for region_value, points_in_region in regions:
        area = len(points_in_region)
        perimiter = 0
        for x, y in points_in_region:
            for adjacent in [(x+1, y), (x-1, y), (x, y-1), (x, y+1)]:
                if grid.value_at_position(adjacent) != region_value:
                    perimiter += 1
        price = area * perimiter
        result += price
    return result


def run_2(inputs):
    grid = Grid2D([i.strip() for i in inputs])
    regions = _create_regions(grid)
    
    result = 0
    for region_value, points_in_region in regions:
        area = len(points_in_region)
        sides = []
        point = points_in_region.pop()
        queue = [point]
        while queue:
            x, y = queue.pop(0)
            for adjacent in [(x+1, y), (x-1, y), (x, y-1), (x, y+1)]:
                # If we haven't processed this yet, add it to queue
                if adjacent in points_in_region:
                    queue.append(adjacent)
                    points_in_region.remove(adjacent)
                # If this is on the perimeter and non-region is in adjacent's direction
                if grid.value_at_position(adjacent) != region_value:
                    outside_direction = (adjacent[0]-x, adjacent[1]-y)
                    # Check if there is already a side that includes this direction
                    # by looking in "sides" for adjacents perpendicular to the direction and seeing if
                    # they are on a side with a non-region in the direction
                    matching_side = _find_matching_side(x, y, outside_direction, sides, grid, region_value)
                    if matching_side is not None:
                        matching_side[1].add((x, y))
                    else:
                        # Else, create a new side with this point and direction
                        sides.append((outside_direction, {(x, y),}))

        price = area * len(sides)
        result += price
    return result


def _find_matching_side(x, y, outside_direction, sides, grid, region_value):
    """
    We aim to see if there is an existing "side" that (x,y) belongs to.
    To do this, we check every known side. If it's on a perimiter that matches our row or column
    and is facing in the same direction, we do an inefficient check to prove whether or not it's indeed
    the same side: for every known point in the side, we walk the entire edge between it and (x,y) and check
    if each of those points is on the same side.
    """
    for side in sides:
        side_direction, points = side
        if side_direction != outside_direction:
            continue
        for p_x, p_y in points:
            if p_y == y:
                betweens = [(min(x, p_x)+i, y) for i in range(abs(x - p_x))]
                if all(_is_on_perimiter_facing_specified_direction(b, grid, side_direction, region_value) for b in betweens):
                    return side
            elif p_x == x:
                betweens = [(x, min(y, p_y)+i) for i in range(abs(y - p_y))]
                if all(_is_on_perimiter_facing_specified_direction(b, grid, side_direction, region_value) for b in betweens):
                    return side

    return None


def _is_on_perimiter_facing_specified_direction(other, grid, side_direction, region_value):
    """
    True if "other" point is in the region and is on the perimiter that faces
    the specified direction. Else False.
    """
    if grid.value_at_position(other) != region_value:
        return False
    other_x, other_y = other
    adjacent = (other_x + side_direction[0], other_y + side_direction[1])
    if grid.value_at_position(adjacent) != region_value:
        return True
    return False


def _create_regions(grid):
    regions = []

    points = set(position for position, _ in grid)
    while points:
        p = points.pop()
        value = grid.value_at_position(p)
        queue = [p]
        points_in_region = set()
        while queue:
            x, y = queue.pop()
            points_in_region.add((x, y))
            for adjacent in [(x+1, y), (x-1, y), (x, y-1), (x, y+1)]:
                if grid.value_at_position(adjacent) == value and adjacent not in points_in_region:
                    queue.append(adjacent)
                    if adjacent in points:
                        points.remove(adjacent)
        regions.append((value, points_in_region))
    
    return regions


def run_tests():
    test_inputs = """
AAAA
BBCD
BBCC
EEEC
    """.strip().split('\n')

    result_1 = run_1(test_inputs)
    if result_1 != 140:
        raise Exception(f"Test 1 did not pass, got {result_1}")
    
    result_2 = run_2(test_inputs)
    if result_2 != 80:
        raise Exception(f"Test 2 did not pass, got {result_2}")
    
    test_inputs = """
RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE
    """.strip().split('\n')

    result_1 = run_1(test_inputs)
    if result_1 != 1930:
        raise Exception(f"Test 1.2 did not pass, got {result_1}")
    
    test_inputs = """
EEEEE
EXXXX
EEEEE
EXXXX
EEEEE
    """.strip().split('\n')

    result_2 = run_2(test_inputs)
    if result_2 != 236:
        raise Exception(f"Test 2.2 did not pass, got {result_2}")
    
    test_inputs = """
AAAAAA
AAABBA
AAABBA
ABBAAA
ABBAAA
AAAAAA
    """.strip().split('\n')

    result_2 = run_2(test_inputs)
    if result_2 != 368:
        raise Exception(f"Test 2.3 did not pass, got {result_2}")


if __name__ == "__main__":
    run_tests()

    input = read_inputs(12)

    result_1 = run_1(input)
    print(f"Finished 1 with result {result_1}")

    # 909877 too high
    # 845614 too low
    result_2 = run_2(input)
    print(f"Finished 2 with result {result_2}")
