import re


def string_to_program(string):
    pattern = re.compile('(\w+) (.\d+)')
    program = [
        (instruction, int(n))
        for (instruction, n)
        in pattern.findall(string)
    ]
    return program

def run(program):
    index = 0
    accumulator = 0
    indices = []
    while True:
        if index in indices:
            success = False
            break
        if index == len(program):
            success = True
            break
        indices.append(index)
        instruction, n = program[index]
        step = 1
        if instruction == 'acc':
            accumulator += n
        elif instruction == 'jmp':
            step = n
        index += step
    return success, accumulator


def modified_programs(text):
    program = string_to_program(text)
    indices = [i for (i, (op, _)) in enumerate(program) if op in ('nop', 'jmp')]
    for index in indices:
        modified = program[:]
        op, n = modified[index]
        op = 'nop' if op == 'jmp' else 'jmp'
        modified[index] = op, n
        yield modified


def fix(text):
    for program in modified_programs(text):
        success, acc = run(program)
        if success:
            return acc


if __name__ == "__main__":
    text_example = """nop +0
    acc +1
    jmp +4
    acc +3
    jmp -3
    acc -99
    acc +1
    jmp -4
    acc +6"""

    with open('input.txt') as f:
        text = f.read()

    # Part 1
    assert run(string_to_program(text_example)) == (False, 5)
    print(run(string_to_program(text))[1])

    # Part 2
    assert fix(text_example) == 8
    print(fix(text))
