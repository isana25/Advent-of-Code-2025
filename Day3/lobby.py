#############################

# Part One 

#############################
from pathlib import Path

def find_max_joltage(bank):
    """
    Find the maximum joltage from a bank by choosing exactly two batteries.
    The joltage is formed by concatenating the two chosen digits.
    We need to find the pair that produces the largest two-digit number.
    """
    max_joltage = 0
    
    # Try all pairs of positions (i, j) where i < j
    # This preserves the order of batteries (cannot rearrange)
    for i in range(len(bank)):
        for j in range(i + 1, len(bank)):
            # Form the number by concatenating digits at positions i and j
            joltage = int(bank[i] + bank[j])
            max_joltage = max(max_joltage, joltage)
    
    return max_joltage

def solve_lobby(banks):
    """
    Calculate the total output joltage from all battery banks.
    """
    total_joltage = 0
    
    for bank in banks:
        max_joltage = find_max_joltage(bank)
        total_joltage += max_joltage
    
    return total_joltage

# Read input file
script_dir = Path(__file__).parent
input_path = script_dir / 'input.txt'

with open(input_path, 'r') as f:
    banks = [line.strip() for line in f if line.strip()]

# Solve the puzzle
answer = solve_lobby(banks)
print(f"Total output joltage: {answer}")

#############################

# Part Two

#############################

from pathlib import Path

def find_max_joltage_part2(bank):
    """
    Find the maximum joltage by choosing exactly 12 batteries.
    Uses a greedy algorithm: at each position, select the largest digit
    that still leaves enough digits to complete the 12-digit number.
    """
    if len(bank) < 12:
        return 0  # Not enough batteries
    
    result = []
    start_index = 0
    
    # For each of the 12 positions in our result
    for pos in range(12):
        # Calculate how many digits we still need after this position
        remaining_after_this = 12 - len(result) - 1
        
        # Calculate the latest index we can choose from
        # We need to leave enough digits for the remaining positions
        latest_index = len(bank) - remaining_after_this - 1
        
        # Find the maximum digit in the valid range
        best_digit = '0'
        best_index = start_index
        
        for i in range(start_index, latest_index + 1):
            if bank[i] > best_digit:
                best_digit = bank[i]
                best_index = i
        
        result.append(best_digit)
        start_index = best_index + 1
    
    return int(''.join(result))

def solve_lobby_part2(banks):
    """
    Calculate the total output joltage from all battery banks for Part 2.
    """
    total_joltage = 0
    
    for bank in banks:
        max_joltage = find_max_joltage_part2(bank)
        total_joltage += max_joltage
    
    return total_joltage

# Read input file
script_dir = Path(__file__).parent
input_path = script_dir / 'input.txt'

with open(input_path, 'r') as f:
    banks = [line.strip() for line in f if line.strip()]

# Solve Part 2
answer = solve_lobby_part2(banks)
print(f"Part 2 - Total output joltage: {answer}")
