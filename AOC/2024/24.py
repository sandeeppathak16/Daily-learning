def solve(filename='24.txt'):
    import copy
    wires, gates = {}, {}
    with open(filename, 'r') as f:
        for line in f.readlines():
            line = line.strip()
            if '->' in line:
                inputs, output = line.strip().split('->')
                x, ops, y = inputs.strip().split(' ')
                gates[output.strip()] = (x, ops, y)
            elif line:
                gate, value = line.split(':')
                wires[gate.strip()] = int(value.strip())

    # print(gates)
    # print(wires)


    while gates:
        processed = False
        copy_gates = copy.deepcopy(gates)
        check = set(wires.keys())

        for item, value in copy_gates.items():
            x, ops, y = value

            if x in check and y in check:
                x = wires[x]
                y = wires[y]
                if ops == 'OR':
                    wires[item] = x | y
                elif ops == 'AND':
                    wires[item] = x & y
                else:
                    wires[item] = x ^ y

                del gates[item]
                processed = True

        if not processed:
            raise ValueError("Cannot resolve remaining gates")

    wires = sorted(wires.items(), key= lambda item: item[0])
    ans = [value for key , value in wires if key.startswith('z')]
    print(len(ans))

    number = 0

    for i, val in enumerate(ans):
        number += int(val) * (2**i)

    print(number)

    
                

        

solve()
