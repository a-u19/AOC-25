import open_input

test = 0
inp = open_input.open_as_list('day11sample.txt') if test else open_input.open_as_list('day11.txt')
inp2 = open_input.open_as_list('day11sample2.txt') if test else open_input.open_as_list('day11.txt')
dirs = {}
for row in inp:
    src, dest = row.split(":")
    dirs[src] = dest.strip().split(" ")
dirs2 = {}
for row in inp2:
    src, dest = row.split(":")
    dirs2[src] = dest.strip().split(" ")


def find_paths(curr_node):
    if curr_node == 'out':
        return [['out']]  # list containing one path: ['out']

    paths = []
    for child in dirs.get(curr_node, []):
        for child_path in find_paths(child):
            paths.append([curr_node] + child_path)
    return paths

def main_part_one():
    all_paths = find_paths('you')
    print(f"the ans to part one is {len(all_paths)}")


def find_paths_with_dac_fft(curr_node, visited_required):
    if curr_node == 'out':
        if all(req in visited_required for req in ['dac', 'fft']):
            return 1  # Count this path
        else:
            return 0  # Invalid path

    total = 0
    new_visited = set(visited_required)

    for child in dirs2.get(curr_node, []):
        total += find_paths_with_dac_fft(child, new_visited)

    return total


def main_part_two():
    print(f"the ans to part two is {find_paths_with_dac_fft('svr', set())}")

main_part_two()