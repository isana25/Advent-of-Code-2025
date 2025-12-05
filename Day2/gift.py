# from pathlib import Path

# def is_invalid_id(num):
#     """
#     Check if a number is invalid (made of a sequence repeated twice).
#     Examples: 55 (5 repeated), 6464 (64 repeated), 123123 (123 repeated)
#     """
#     num_str = str(num)
#     length = len(num_str)
    
#     # Can only be repeated if even length
#     if length % 2 != 0:
#         return False
    
#     # Split in half and check if both halves are equal
#     mid = length // 2
#     first_half = num_str[:mid]
#     second_half = num_str[mid:]
    
#     return first_half == second_half

# def find_invalid_ids_in_range(start, end):
#     """
#     Find all invalid IDs in a given range.
#     """
#     invalid_ids = []
#     for num in range(start, end + 1):
#         if is_invalid_id(num):
#             invalid_ids.append(num)
#     return invalid_ids

# def solve_gift_shop(ranges_string):
#     """
#     Parse the ranges and find all invalid IDs.
#     """
#     # Parse the ranges
#     ranges = []
#     for range_str in ranges_string.split(','):
#         range_str = range_str.strip()
#         if range_str:
#             start, end = map(int, range_str.split('-'))
#             ranges.append((start, end))
    
#     # Find all invalid IDs
#     all_invalid_ids = []
#     for start, end in ranges:
#         invalid_in_range = find_invalid_ids_in_range(start, end)
#         all_invalid_ids.extend(invalid_in_range)
    
#     # Calculate sum
#     total = sum(all_invalid_ids)
#     return total

# # Read input file
# script_dir = Path(__file__).parent
# input_path = script_dir / 'input.txt'

# with open(input_path, 'r') as f:
#     ranges_input = f.read().strip()

# # Solve the puzzle
# answer = solve_gift_shop(ranges_input)
# print(f"Sum of all invalid IDs: {answer}")

from pathlib import Path

def is_invalid_id_part2(num):
    """
    Check if a number is invalid (made of a sequence repeated at least twice).
    Examples: 
    - 12341234 (1234 repeated 2 times)
    - 123123123 (123 repeated 3 times)
    - 1212121212 (12 repeated 5 times)
    - 1111111 (1 repeated 7 times)
    """
    num_str = str(num)
    length = len(num_str)
    
    # Try all possible pattern lengths from 1 to length//2
    # Pattern must repeat at least twice, so max pattern length is length//2
    for pattern_length in range(1, length // 2 + 1):
        # Check if the total length is divisible by pattern length
        if length % pattern_length == 0:
            # Extract the pattern
            pattern = num_str[:pattern_length]
            
            # Check if repeating this pattern gives us the original number
            num_repetitions = length // pattern_length
            if pattern * num_repetitions == num_str:
                # Must repeat at least twice
                if num_repetitions >= 2:
                    return True
    
    return False

def find_invalid_ids_in_range_part2(start, end):
    """
    Find all invalid IDs in a given range using part 2 rules.
    """
    invalid_ids = []
    for num in range(start, end + 1):
        if is_invalid_id_part2(num):
            invalid_ids.append(num)
    return invalid_ids

def solve_gift_shop_part2(ranges_string):
    """
    Parse the ranges and find all invalid IDs using part 2 rules.
    """
    # Parse the ranges
    ranges = []
    for range_str in ranges_string.split(','):
        range_str = range_str.strip()
        if range_str:
            start, end = map(int, range_str.split('-'))
            ranges.append((start, end))
    
    # Find all invalid IDs
    all_invalid_ids = []
    for start, end in ranges:
        invalid_in_range = find_invalid_ids_in_range_part2(start, end)
        all_invalid_ids.extend(invalid_in_range)
    
    # Calculate sum
    total = sum(all_invalid_ids)
    return total

# Read input file
script_dir = Path(__file__).parent
input_path = script_dir / 'input.txt'

with open(input_path, 'r') as f:
    ranges_input = f.read().strip()

# Solve part 2
answer = solve_gift_shop_part2(ranges_input)
print(f"Part 2 - Sum of all invalid IDs: {answer}")
