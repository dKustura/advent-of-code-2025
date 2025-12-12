import math
import os
from typing import List, Set

def parse_scheme(line: str):
    parts = line.split(' ')
    scheme = [i == '#' for i in parts[0][1:-1]]

    toggle_sets: List[Set[int]] = []

    for t in parts[1:-1]:
        toggle_sets.append(set(map(int, t[1:-1].split(','))))

    return scheme, toggle_sets

def min_combinations(line: str):
        scheme, toggle_sets = parse_scheme(line)
        init_state = [False] * len(scheme)

        def go(state: List[bool], index: int, count: int):
            if state == scheme:
                return count
            
            if index == len(toggle_sets):
                return math.inf
            
            skipped = go(state.copy(), index + 1, count)

            toggle_set = toggle_sets[index]
            for t in toggle_set:
                state[t] = not state[t]
            not_skipped = go(state.copy(), index + 1, count + 1)

            return min(skipped, not_skipped)

        return go(init_state, 0, 0)



def day10_part1():
    with open(os.path.join(os.path.dirname(__file__), 'input')) as f:
        lines = f.read().splitlines()

        res = 0

        for line in lines:
            res += min_combinations(line)

        return res
        
part1 = day10_part1()
print('Part 1: ', part1)