import os
from typing import List

ADDITION = '+'
MULTIPLICATION = '*'
SPACE = ' '

def day6_part1():
    with open(os.path.join(os.path.dirname(__file__), 'input')) as f:
        lines = f.read().splitlines()
        
        data = [line.split() for line in lines]
        
        operators = data[-1]
        problem_count = len(operators)
        operand_count = len(lines) - 1
        
        total = 0
        
        for p in range(problem_count):
            operator = operators[p]
            is_addition = operator == ADDITION
            sub_total = 0 if is_addition else 1
            for o in range(operand_count):
                operand = int(data[o][p])
                sub_total = sub_total + operand if is_addition else sub_total * operand
            
            total += sub_total
            
        return total
    

def read_line(line: str, lengths: List[int]):
    res = []
    i = 0
    
    for l in lengths:
        res.append(line[i:i+l])
        i += l + 1
    
    return res
            

def day6_part2():
    with open(os.path.join(os.path.dirname(__file__), 'input')) as f:
        lines = f.read().splitlines()
        data = [line.split() for line in lines]
        
        operators = data[-1]
        problem_count = len(operators)
        operand_count = len(lines) - 1
        
        lengths = [max(len(data[o][p]) for o in range(operand_count)) for p in range(problem_count)]
        
        indented_data = [read_line(line, lengths) for line in lines[:-1]]
        
        total = 0
            
        for p in range(problem_count):
            operator = operators[p]
            length = lengths[p]
            is_addition = operator == ADDITION
            sub_total = 0 if is_addition else 1
            raw_operands = [indented_data[o][p] for o in range(operand_count)]
            
            for i in range(length - 1, -1, -1):
                operand = int(''.join(operand[i] for operand in raw_operands if operand[i] != SPACE))
                sub_total = sub_total + operand if is_addition else sub_total * operand
            
            total += sub_total
            
        return total
    
part1 = day6_part1()
print("Part1 result:", part1)

part2 = day6_part2()
print("Part2 result:", part2)
