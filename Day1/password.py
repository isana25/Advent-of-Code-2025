########################

# Part One

########################

from pathlib import Path

def solve_dial_puzzle_part2(rotations):
    position = 50
    zero_count = 0
    
    for rotation in rotations:
        direction = rotation[0]
        distance = int(rotation[1:])
        
        if direction == 'L':
            # Moving left (decreasing)
            # Count how many times we pass through 0
            # We pass through 0 when we cross from 0 to 99
            new_position = (position - distance) % 100
            
            # Calculate number of complete wraps + final crossing
            # If distance >= position, we cross 0 at least once
            crossings = distance // 100
            if distance % 100 > position:
                crossings += 1
                
        else:  # direction == 'R'
            # Moving right (increasing)
            new_position = (position + distance) % 100
            
            # Calculate crossings when moving right
            # We cross 0 when going from 99 to 0
            crossings = distance // 100
            if position + (distance % 100) >= 100:
                crossings += 1
        
        zero_count += crossings
        position = new_position
    
    return zero_count

# Test with the example
example_rotations = ['L68', 'L30', 'R48', 'L5', 'R60', 'L55', 'L1', 'L99', 'R14', 'L82']
password = solve_dial_puzzle_part2(example_rotations)
print(f"Part 2 Password: {password}")  # Should output 6

# Read actual input
script_dir = Path(__file__).parent
input_path = script_dir / 'input.txt'

with open(input_path, 'r') as f:
    my_rotations = [line.strip() for line in f if line.strip()]
    
actual_password = solve_dial_puzzle_part2(my_rotations)
print(f"Actual Part 2 Password: {actual_password}")


########################

# Part Two

########################

from pathlib import Path

def solve_dial_puzzle_part2(rotations):
    position = 50
    zero_count = 0
    
    for rotation in rotations:
        direction = rotation[0]
        distance = int(rotation[1:])
        
        if direction == 'L':
            # Moving left (decreasing)
            # Count how many times we pass through 0
            # We pass through 0 when we cross from 0 to 99
            new_position = (position - distance) % 100
            
            # Calculate number of complete wraps + final crossing
            # If distance >= position, we cross 0 at least once
            crossings = distance // 100
            if distance % 100 > position:
                crossings += 1
                
        else:  # direction == 'R'
            # Moving right (increasing)
            new_position = (position + distance) % 100
            
            # Calculate crossings when moving right
            # We cross 0 when going from 99 to 0
            crossings = distance // 100
            if position + (distance % 100) >= 100:
                crossings += 1
        
        zero_count += crossings
        position = new_position
    
    return zero_count

# Test with the example
example_rotations = ['L68', 'L30', 'R48', 'L5', 'R60', 'L55', 'L1', 'L99', 'R14', 'L82']
password = solve_dial_puzzle_part2(example_rotations)
print(f"Part 2 Password: {password}")  # Should output 6

# Read actual input
script_dir = Path(__file__).parent
input_path = script_dir / 'input.txt'

with open(input_path, 'r') as f:
    my_rotations = [line.strip() for line in f if line.strip()]
    
actual_password = solve_dial_puzzle_part2(my_rotations)
print(f"Actual Part 2 Password: {actual_password}")


