def solve(filename='2.txt'):
    data = {}
    with open(filename, 'r') as f:
        for line in f.readlines():
            line = line.strip()

            game_details, subsets  = line.split(':')

            _, game_id = game_details.split(' ')
            data[game_id] = []

            

            for s in subsets.split(';'):
                subset = []
                for ball_detail in s.split(','):
                    n, color = ball_detail.strip().split(' ')
                    subset.append((int(n), color))

                data[game_id].append(subset)

    part1 = 0
    checks = dict(red=12, green=13, blue=14)
    min_cube_needed = []

    for game_id, subsets in data.items():
        valid = True

        cubes_need = dict(red=float('-inf'), green=float('-inf'), blue=float('-inf'))

        for subset in subsets:
            invalid = False
            for num, color in subset:
                if num > checks[color]:
                    if not invalid:
                        invalid = True

                cubes_need[color] = max(cubes_need[color], num)

            if invalid:
                valid = False

        if valid:
            part1 += int(game_id)

        min_cube_needed.append(cubes_need)

    import math
    part2 = sum([math.prod(cubes.values()) for cubes in min_cube_needed])

    return part1, part2


