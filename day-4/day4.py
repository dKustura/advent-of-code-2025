import os
from typing import List

ROLL = '@'
DIRECTIONS = [-1, 0, 1]
THRESHOLD = 4

def find_removable(grid: List[List[str]]):
    N = len(grid)
    M = len(grid[0])
    
    def check(i, j):
            if grid[i][j] != ROLL:
                return False
            
            adj_rolls = 0
            
            for dr in DIRECTIONS:
                for dc in DIRECTIONS:
                    r = i + dr
                    c = j + dc
                    
                    if 0 <= r < N and 0 <= c < M and (dr != 0 or dc != 0):
                        if grid[r][c] == ROLL:
                            adj_rolls += 1
                            if adj_rolls >= THRESHOLD:
                                return False
                            
            return True
        
    result = set()
        
    for i in range(N):
        for j in range(M):
            if check(i, j):
                result.add((i, j))
            
    return result
    

def day4_part1() -> int:
    with open(os.path.join(os.path.dirname(__file__), 'input')) as f:
        lines = f.read().splitlines()
        grid = [[char for char in line] for line in lines]
      
        return len(find_removable(grid))
    
def day4_part2():
    with open(os.path.join(os.path.dirname(__file__), 'input')) as f:
        lines = f.read().splitlines()
        grid = [[char for char in line] for line in lines]
        result = 0
        
        def remove_from_grid(grid, removable):
            for rem in removable:
                grid[rem[0]][rem[1]] = '.'
                
            return grid
        
        while True:
            removable = find_removable(grid)
            size = len(removable)
            
            if size == 0:
                break
            
            result += size
            grid = remove_from_grid(grid, removable)
      
        return result
    
part1_result = day4_part1()
print("Part 1 result:", part1_result)
    
part2_result = day4_part2()
print("Part 2 result:", part2_result)
            
            