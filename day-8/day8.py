

from math import sqrt
import os
from typing import List, Optional, Tuple

CUTOFF = 1000

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
            
        return self.parent[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        
        if self.size[px] < self.size[py]:
            px, py = py, px
            
        self.parent[py] = px
        self.size[px] += self.size[py]
        
        return True

def calc_distance(p1: Tuple[int, int, int], p2: Tuple[int, int, int]):
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    
    return (x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2

def connect_junction_boxes(points: List[Tuple[int, int, int]], max_connections: Optional[int]):
    point_count = len(points)
        
    # Build all pairs with distances
    pairs = []
    for i in range(point_count):
        for j in range(i + 1, point_count):
            distance = calc_distance(points[i], points[j])
            pairs.append((distance, i, j))
    
    pairs.sort()
    
    uf = UnionFind(point_count)
    groups = point_count
    
    for k, (distance, i, j) in enumerate(pairs):
        if max_connections is not None and k >= max_connections:
            break
        
        if uf.union(i, j):
            groups -= 1
            if max_connections is None and groups == 1:
                return points[i][0] * points[j][0]
    
    top_3 = sorted(uf.size, reverse=True)[:3]        
    return top_3[0] * top_3[1] * top_3[2]

def day8_part1():
    with open(os.path.join(os.path.dirname(__file__), 'input')) as f:
        lines = f.read().splitlines()
        
        points = [tuple(map(int, line.split(','))) for line in lines]
        return connect_junction_boxes(points, CUTOFF)
    
def day8_part2():
    with open(os.path.join(os.path.dirname(__file__), 'input')) as f:
        lines = f.read().splitlines()
        
        points = [tuple(map(int, line.split(','))) for line in lines]
        return connect_junction_boxes(points, None)
        
        
part1 = day8_part1()
print("Top 3 circuit sizes multiplied are:", part1)


part2 = day8_part2()
print("Distance from wall is:", part2)