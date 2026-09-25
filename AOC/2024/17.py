# | Opcode | Name | Effect                             |
# | ------ | ---- | ---------------------------------- |
# | 0      | adv  | Divide A by 2^combo → store in A   |
# | 1      | bxl  | B = B XOR literal                  |
# | 2      | bst  | B = (combo % 8)                    |
# | 3      | jnz  | If A ≠ 0, jump instruction pointer |
# | 4      | bxc  | B = B XOR C                        |
# | 5      | out  | Output (combo % 8)                 |
# | 6      | bdv  | Divide A by 2^combo → store in B   |
# | 7      | cdv  | Divide A by 2^combo → store in C   |

# | Operand | Meaning                |
# | ------- | ---------------------- |
# | 0–3     | Literal values 0–3     |
# | 4       | Value of register A    |
# | 5       | Value of register B    |
# | 6       | Value of register C    |
# | 7       | Invalid (won’t appear) |

import re

def parse_input(filename):
    with open(filename) as f:
        text = f.read().strip()

    regs, prog = text.split("\n\n")

    registers = {}
    for line in regs.splitlines():
        name, value = line.split(": ")
        registers[name[-1].lower()] = int(value)

    program = list(map(int, re.findall(r"\d+", prog)))

    return registers, program


def run_vm(program, A, B=0, C=0):
    reg = {
        "a": A,
        "b": B,
        "c": C,
    }

    ip = 0
    output = []

    def combo(operand):
        if 0 <= operand <= 3:
            return operand
        if operand == 4:
            return reg["a"]
        if operand == 5:
            return reg["b"]
        if operand == 6:
            return reg["c"]
        raise ValueError("Invalid combo operand")

    while ip + 1 < len(program):
        opcode = program[ip]
        operand = program[ip + 1]

        jumped = False

        if opcode == 0:      # adv
            reg["a"] //= (1 << combo(operand))

        elif opcode == 1:    # bxl
            reg["b"] ^= operand

        elif opcode == 2:    # bst
            reg["b"] = combo(operand) % 8

        elif opcode == 3:    # jnz
            if reg["a"] != 0:
                ip = operand
                jumped = True

        elif opcode == 4:    # bxc
            reg["b"] ^= reg["c"]

        elif opcode == 5:    # out
            output.append(combo(operand) % 8)

        elif opcode == 6:    # bdv
            reg["b"] = reg["a"] // (1 << combo(operand))

        elif opcode == 7:    # cdv
            reg["c"] = reg["a"] // (1 << combo(operand))

        else:
            raise ValueError(f"Unknown opcode {opcode}")

        if not jumped:
            ip += 2

    return output


def find_minimum_A(program):
    candidates = [0]

    for needed_len in range(1, len(program) + 1):
        next_candidates = []

        for prefix in candidates:
            for digit in range(8):
                candidate = (prefix << 3) | digit

                out = run_vm(program, candidate)

                if out == program[-needed_len:]:
                    next_candidates.append(candidate)

        candidates = next_candidates

    return min(
        a
        for a in candidates
        if run_vm(program, a) == program
    )


def solve(filename="17.txt"):
    registers, program = parse_input(filename)

    part1_output = run_vm(
        program,
        registers["a"],
        registers["b"],
        registers["c"]
    )

    part1 = ",".join(map(str, part1_output))
    part2 = find_minimum_A(program)

    return part1, part2
