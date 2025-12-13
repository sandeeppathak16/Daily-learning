from itertools import combinations

machines = []

with open("10dec.txt") as f:
    for line in f:
        line = line.strip()

        start_sq = line.index('[')
        end_sq = line.index(']')
        pattern = line[start_sq + 1:end_sq]
        target = [1 if c == '#' else 0 for c in pattern]

        start_btn = end_sq + 1
        start_curly = line.index('{')
        button_part = line[start_btn:start_curly].strip()

        buttons = []
        i = 0
        while i < len(button_part):
            if button_part[i] == '(':
                j = i + 1
                while button_part[j] != ')':
                    j += 1
                button = list(map(int, button_part[i+1:j].split(',')))
                buttons.append(button)
                i = j
            i += 1

        machines.append({
            "target": target,
            "buttons": buttons
        })

ans = 0
for idx, m in enumerate(machines, 1):
    button = m["buttons"]
    target = m["target"]
    button_i = list(range(len(button)))

    all_combos = []
    for r in range(1, len(button_i) + 1):
        all_combos.extend(combinations(button_i, r))

    for comb in all_combos:
        start = [0] * len(target)
        for i in comb:
            for b in button[i]:
                start[b] = 1 if start[b] == 0 else 0

        if start == target:
            ans += len(comb)
            break

print(ans)
