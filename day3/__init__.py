import math

def calculate_closest_crossed_wires():
    with open('input.txt') as f:
        wire_1, wire_2 = [line.split(',') for line in f.readlines()]

    hit_coords = set()
    coord = (0, 0)
    for instruction in wire_1:
        for coord in get_coordinates_from_instruction(coord, instruction):
            hit_coords.add(coord)

    shortest_distance = math.inf
    coord = (0, 0)
    for instruction in wire_2:
        for coord in get_coordinates_from_instruction(coord, instruction):
            if coord in hit_coords:
                shortest_distance = min(shortest_distance,  sum(map(abs, coord)))
    return shortest_distance


def calculate_shortest_wire_intersection():
    with open('input.txt') as f:
        wire_1, wire_2 = [line.split(',') for line in f.readlines()]

    hit_coords = {}
    coord = (0, 0)
    steps = 0
    for instruction in wire_1:
        for coord in get_coordinates_from_instruction(coord, instruction):
            steps += 1
            hit_coords[coord] = steps

    lowest_total_steps = math.inf

    coord = (0, 0)
    steps = 0
    for instruction in wire_2:
        for coord in get_coordinates_from_instruction(coord, instruction):
            steps += 1
            if coord in hit_coords:
                lowest_total_steps = min(steps + hit_coords[coord], lowest_total_steps)

    return lowest_total_steps

directions = {
    'R': (1, 0),
    'L': (-1, 0),
    'U': (0, 1),
    'D': (0, -1),
}


def get_coordinates_from_instruction(location, instruction):
    direction = directions[instruction[0]]
    amount = int(instruction[1:])
    for i in range(1, amount + 1):
        yield location[0] + direction[0] * i, location[1] + direction[1] * i


print(calculate_closest_crossed_wires())
print(calculate_shortest_wire_intersection())
