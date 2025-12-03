import os
from typing import List


def day3_part1():
    with open(os.path.join(os.path.dirname(__file__), 'input')) as f:
        banks = f.read().splitlines()
        total = 0
        
        for bank in banks:
            first = 0
            second = 0
            B = len(bank)
            
            for i in range(B):
                battery = bank[i]
                joltage = int(battery)
                
                if first == 0 or (first < joltage and i != B - 1):
                    first = joltage
                    second = 0
                elif second == 0 or second < joltage:
                    second = joltage
                
            total += first * 10 + second
        
        return total
    
    
def digits_to_number(digits: List[int]):
    result = 0
    for digit in digits:
        result = result * 10 + digit
    return result
    
    
def day3_part2():
    with open(os.path.join(os.path.dirname(__file__), 'input')) as f:
        banks = f.read().splitlines()
        total = 0
        
        for bank in banks:
            B = len(bank)
            digits = []
            
            for i in range(B):
                battery = bank[i]
                joltage = int(battery)
                
                replaced = False
                
                if len(digits) == 0:
                    digits.append(joltage)
                    replaced = True
                else:
                    leftover_count = B - i
                    start_index = max(0, 12 - leftover_count)
                    for j in range(start_index, len(digits)):
                        if digits[j] < joltage:
                            digits = digits[:j] + [joltage]
                            replaced = True
                            break
                
                if not replaced and len(digits) < 12:
                    digits.append(joltage)
                    
            total += digits_to_number(digits)
        
        return total
            
# result = day3_part1()
# print("Joltage:", result)

result = day3_part2()
print("Override Joltage:", result)
    