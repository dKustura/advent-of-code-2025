import os

# def is_repeated_substring(s: str) -> bool:
#     return s in (s + s)[1:-1]

def is_repeated_substring(s: str) -> bool:
    n = len(s)
    for i in range(1, n):
        if n % i == 0:  # i is a divisor of length
            substring = s[:i]
            if substring * (n // i) == s:
                return True
    return False

def is_invalid_id(num: int):
    s = str(num)
    return is_repeated_substring(s)


def day2_part2():
    with open(os.path.join(os.path.dirname(__file__), 'input')) as f:
        first_line = f.readline().strip()
        ranges = first_line.split(',')
        result = 0
        
        for r in ranges:
            lower, upper = map(int, r.split('-'))
            for num in range(lower, upper + 1):
                if is_invalid_id(num):
                    result += num
        
        return result
    
    
result = day2_part2()
print("Sum of invalid IDs:", result)