from operator import add, mul

def run_intcode(addr_1, addr_2):
    total = 0
    with open('input.txt') as f:
        program = list(map(int, f.read().split(',')))

    program[1] = addr_1
    program[2] = addr_2

    pos = 0
    while pos < len(program):
        opcode = program[pos]
        if opcode == 99:
            break
        else:
            operator = add if opcode == 1 else mul
            program[program[pos + 3]] = operator(program[program[pos + 1]], program[program[pos + 2]])
        pos += 4


    return program[0]

def find_output(expected, noun_upper, verb_upper):
    for i in range(noun_upper):
        for j in range(verb_upper):
            result = run_intcode(i, j)
            if result == expected:
                return i * 100 + j

print(find_output(19690720, 99, 99))
