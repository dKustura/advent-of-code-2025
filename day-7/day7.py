import os
from typing import Counter

SOURCE = 'S'
SPLITTER = '^'
SPACE = '.'

def day7_part1():
    with open(os.path.join(os.path.dirname(__file__), 'input')) as f:
        lines = f.read().splitlines()
        
        width = len(lines[0])
        source_index = lines[0].find(SOURCE)
        
        beams = set()
        beams.add(source_index)
        
        count = 0
        
        for line in lines[2:]:
            for i in range(width):
                p = line[i]
                if p == SPLITTER and i in beams:
                    count += 1
                    beams.remove(i)
                    if i > 0:
                        beams.add(i - 1)
                    if i < width - 1:
                        beams.add(i + 1)
        
        return count
    
def day7_part2():
    with open(os.path.join(os.path.dirname(__file__), 'input')) as f:
        lines = f.read().splitlines()
        
        width = len(lines[0])
        source_index = lines[0].find(SOURCE)
        
        # each beam is stored as its index and the number of timelines it exists in
        beams = Counter()
        beams[source_index] = 1
        
        for line in lines[2:]:
            for i in range(width):
                p = line[i]
                if p == SPLITTER and i in beams:
                    c = beams[i]
                    del beams[i]
                    
                    if i > 0:
                        beams[i - 1] += c
                    if i < width - 1:
                        beams[i + 1] += c
        
        return sum(beams.values())
    
part1 = day7_part1()
print('Beam has been split {times} times.'.format(times=part1))


part2 = day7_part2()
print('Beam created {timelines} timelines.'.format(timelines=part2))