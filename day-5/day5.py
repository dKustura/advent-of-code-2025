from bisect import bisect_left
import os
from typing import List

# Returns an rray of start/end values of merged ranges.
# For example, ranges 1-5, 7-8, 10-20 would be represented by: [1, 5, 7, 8, 10, 20]
def merge_ranges(lines: List[str]):
    arr = []
    
    for range_line in lines:
            start, end = map(int, range_line.split('-'))
            insertion_start = bisect_left(arr, start)
            insertion_end = bisect_left(arr, end)
            if insertion_start == insertion_end:
                # Only insert if both start and end are outside existing ranges (even position)
                if insertion_start % 2 == 0:
                    arr.insert(insertion_start, start)
                    arr.insert(insertion_start + 1, end)
                # If both are inside (odd position), the new range is contained in an existing range, do nothing
            else:
                start_is_even = insertion_start % 2 == 0
                end_is_even = insertion_end % 2 == 0
                
                if not start_is_even and not end_is_even:
                    # Delete everything between insertion_start and insertion_end
                    del arr[insertion_start:insertion_end]
                elif start_is_even and end_is_even:     
                    # Delete everything between insertion_start and insertion_end
                    del arr[insertion_start:insertion_end]
                    # Insert start and end at the now-cleared position
                    arr.insert(insertion_start, start)
                    arr.insert(insertion_start + 1, end)
                elif start_is_even and not end_is_even:
                    # Add only start and delete everything between insertion_start and insertion_end
                    del arr[insertion_start:insertion_end]
                    arr.insert(insertion_start, start)
                else:
                    # Add only end and delete everything between insertion_start and insertion_end
                    del arr[insertion_start:insertion_end]
                    arr.insert(insertion_start, end)
            
    return arr
    

def day5_part1():
    with open(os.path.join(os.path.dirname(__file__), 'input')) as f:
        lines = f.read().splitlines()
        blank_index = lines.index('')

        range_lines = lines[:blank_index]
        ids = map(int, lines[blank_index + 1:])
        
        range_array = merge_ranges(range_lines)
        
        fresh = 0
        for id in ids:
            pos = bisect_left(range_array, id)
            if pos % 2 != 0:
                fresh += 1
            # matches a range start exactly
            elif pos < len(range_array) and range_array[pos] == id:
                fresh += 1
            
        return fresh
    
def day5_part1_brute():
    with open(os.path.join(os.path.dirname(__file__), 'input')) as f:
        lines = f.read().splitlines()
        blank_index = lines.index('')

        range_lines = lines[:blank_index]
        ids = map(int, lines[blank_index + 1:])
        
        fresh = 0
        
        for id in ids:
            for range_line in range_lines:
                start, end = map(int, range_line.split('-'))
                if start <= id <= end:
                    fresh += 1
                    break
            
        return fresh

def day5_part2():
    with open(os.path.join(os.path.dirname(__file__), 'input')) as f:
        lines = f.read().splitlines()
        blank_index = lines.index('')
        range_lines = lines[:blank_index]
        
        range_array = merge_ranges(range_lines)
        
        fresh = 0
        N = len(range_array)
        prev_end = -1
        
        for i in range(1, N, 2):
            start, end = range_array[i-1:i+1]
            fresh += end - start + 1
            
            if start == prev_end:
                fresh -= 1
                
            prev_end = end
            
        return fresh
        
        

part1_brute = day5_part1_brute()
print("Part1 Brute-Force Result:", part1_brute)

part1 = day5_part1()
print("Part1 Result:", part1)

part2 = day5_part2()
print("Part2 Result:", part2)