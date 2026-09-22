import re
from functools import partial
from operator import __and__, __or__, __xor__


def solve(filename="24.txt", part=1):
    with open(filename) as f:
        puzzle_input = f.read()

    values_txt, gates_txt = puzzle_input.strip().split("\n\n")

    initial_values = {}

    for line in values_txt.splitlines():
        wire, value = line.split(": ")
        initial_values[wire] = int(value)

    wire_map = {}

    for in1, op, in2, out in re.findall(
        r"(\w+) (AND|XOR|OR) (\w+) -> (\w+)",
        gates_txt
    ):
        wire_map[out] = (op, in1, in2)

    operators = {
        "AND": __and__,
        "OR": __or__,
        "XOR": __xor__,
    }

    def get_value(wire, values):
        if wire in values:
            return values[wire]

        op, in1, in2 = wire_map[wire]

        values[wire] = operators[op](
            get_value(in1, values),
            get_value(in2, values),
        )

        return values[wire]

    if part == 1:
        values = dict(initial_values)

        z_wires = sorted(
            [w for w in wire_map if w.startswith("z")],
            reverse=True,
        )

        bits = "".join(
            str(get_value(w, values))
            for w in z_wires
        )

        return int(bits, 2)
    
    def make_wire(char, i):
        return f"{char}{i:02}"

    make_x, make_y, make_z = [
        partial(make_wire, c)
        for c in "xyz"
    ]

    max_bit = max(
        int(w[1:])
        for w in wire_map
        if w.startswith("z")
    )

    null_values = {}

    for i in range(max_bit):
        null_values[make_x(i)] = 0
        null_values[make_y(i)] = 0

    def init_values(i, x, y, carry):
        x_values = {
            make_x(i): x,
            make_x(i - 1): carry,
        }

        y_values = {
            make_y(i): y,
            make_y(i - 1): carry,
        }

        return null_values | x_values | y_values

    def find_wire(op_needed, inputs_needed):
        for out, (op, in1, in2) in wire_map.items():
            if (
                op == op_needed
                and inputs_needed.issubset({in1, in2})
            ):
                return out

        return None

    def fix_bit(i):
        curr_x = make_x(i)
        curr_y = make_y(i)

        prev_x = make_x(i - 1)
        prev_y = make_y(i - 1)

        curr_xor = find_wire("XOR", {curr_x, curr_y})

        prev_xor = find_wire("XOR", {prev_x, prev_y})

        direct_carry = find_wire("AND", {prev_x, prev_y})

        recarry = find_wire("AND", {prev_xor})

        carry = find_wire(
            "OR",
            {direct_carry, recarry}
        )

        z = find_wire(
            "XOR",
            {curr_xor, carry}
        )

        if z is None:
            z_inputs = set(
                wire_map[make_z(i)][1:]
            )

            w1, w2 = (
                z_inputs ^
                {curr_xor, carry}
            )

        else:
            w1, w2 = {z, make_z(i)}

        wire_map[w1], wire_map[w2] = (
            wire_map[w2],
            wire_map[w1],
        )

        return {w1, w2}

    swapped = set()

    for bit in range(1, max_bit):

        broken = any(
            x ^ y ^ carry
            != get_value(
                make_z(bit),
                init_values(bit, x, y, carry)
            )
            for x in range(2)
            for y in range(2)
            for carry in range(2)
        )

        if broken:
            swapped |= fix_bit(bit)

    return ",".join(sorted(swapped))