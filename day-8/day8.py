

from math import sqrt
import os
from typing import List, Optional, Tuple

CUTOFF = 1000

def calc_distance(p1: Tuple[int, int, int], p2: Tuple[int, int, int]):
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    
    return sqrt((x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2)

def connect_junction_boxes(points: List[Tuple[int, int, int]], max_connections: Optional[int]):
    point_count = len(points)
        
    # Build all pairs with distances
    pairs = []
    for i in range(point_count):
        for j in range(i + 1, point_count):
            distance = calc_distance(points[i], points[j])
            pairs.append((i, j, distance))
    
    # Sort once instead of inserting in sorted order
    pairs.sort(key=lambda x: x[2])
    
    # circuit ID -> circuit size
    circuits = {}
    
    # points -> circuit ID
    point_to_circuit = {}
    
    circuit_id = 0
    k = 0
    
    while True:
        if max_connections is not None and k >= max_connections:
            break
        
        i, j, distance = pairs[k]
        p1 = points[i]
        p2 = points[j]
        
        if p1 in point_to_circuit and p2 in point_to_circuit:
            # both points are in a circuit, merge them if it's not the same one
            c1 = point_to_circuit[p1]
            c2 = point_to_circuit[p2]
            if c1 != c2:
                # merge smaller cirtcuit into larger to minimize updates
                if circuits[c1] < circuits[c2]:
                    c1, c2 = c2, c1
                
                circuits[c1] += circuits[c2]
                del circuits[c2]
                
                # only update points that belong to c2
                for p, c in point_to_circuit.items():
                    if c == c2:
                        point_to_circuit[p] = c1
                
        elif p1 in point_to_circuit:
            # p1 already in a circuit
            c = point_to_circuit[p1]
            # add p2 to the circuit of p1
            point_to_circuit[p2] = c
            circuits[c] += 1
        elif p2 in point_to_circuit:
            # p2 already in a circuit
            c = point_to_circuit[p2]
            # add p1 to the circuit of p2
            point_to_circuit[p1] = c
            circuits[c] += 1
        else:
            # new circuit created
            circuit_id += 1
            point_to_circuit[p1] = circuit_id
            point_to_circuit[p2] = circuit_id
            circuits[circuit_id] = 2
            
        k += 1
        
        if max_connections is None and len(circuits) == 1 and list(circuits.values())[0] == point_count:
            return p1[0] * p2[0]
    
    top_3 = sorted(circuits.values(), reverse=True)[:3]        
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
        
        
# part1 = day8_part1()
# print("Top 3 circuit sizes multiplied are:", part1)


part2 = day8_part2()
print("Distance from wall is:", part2)