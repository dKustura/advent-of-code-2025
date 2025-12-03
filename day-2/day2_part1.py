import os

def should_count(id_string: str):
    N = len(id_string)
    
    if N % 2 != 0:
        return False
    
    half = N // 2
    return id_string[:half] == id_string[half:]
    
def get_next_lower_bound(number: int):
    s = str(number)
    N = len(s)
    
    if N % 2 != 0:
        return get_next_lower_bound(pow(10, N))
    
    half_len = N // 2
    potential = int(s[:half_len] + s[:half_len])    
    
    if potential > number:
        return potential
    else:
        first_half_num = int(s[:half_len])
        if first_half_num == pow(10, half_len) - 1:
          return get_next_lower_bound(number + 1)
      
        first_half_num += 1
        first_half_str = str(first_half_num)
        return int(first_half_str + first_half_str)
        
    

def sum_invalid(lower_bound: int, upper_bound: int):
    res = 0
    
    while lower_bound <= upper_bound:    
        s = str(lower_bound)
        
        if should_count(s):
            res += lower_bound
        
        lower_bound = get_next_lower_bound(lower_bound)
        
    return res

def day2_part1():
    with open(os.path.join(os.path.dirname(__file__), 'input')) as f:
        first_line = f.readline().strip()
        ranges = first_line.split(',')
        result = 0
        
        for r in ranges:
            lower, upper = map(int, r.split('-'))
            s = sum_invalid(lower, upper)
            result += s
        
        return result
    
    
result = day2_part1()
print("Sum of invalid IDs:", result)