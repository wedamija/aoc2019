
def calculate_fuel_for_mass(mass):
    fuel = (mass // 3) - 2
    if fuel > 0:
        return fuel + calculate_fuel_for_mass(fuel)
    else:
        return 0


def calculate_fuel():
    total = 0
    with open('input.txt') as f:
        for line in f.readlines():
            total += calculate_fuel_for_mass(int(line))
    return total

print(calculate_fuel())
