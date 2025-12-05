# from pathlib import Path

# def count_adjacent_rolls(grid, row, col):
#     """
#     Count the number of paper rolls (@) in the 8 adjacent positions.
#     """
#     rows = len(grid)
#     cols = len(grid[0])
#     count = 0
    
#     # Check all 8 adjacent positions (including diagonals)
#     for dr in [-1, 0, 1]:
#         for dc in [-1, 0, 1]:
#             # Skip the center position
#             if dr == 0 and dc == 0:
#                 continue
            
#             new_row = row + dr
#             new_col = col + dc
            
#             # Check if the position is within bounds
#             if 0 <= new_row < rows and 0 <= new_col < cols:
#                 if grid[new_row][new_col] == '@':
#                     count += 1
    
#     return count

# def count_accessible_rolls(grid_lines):
#     """
#     Count how many paper rolls can be accessed by forklifts.
#     A roll can be accessed if there are fewer than 4 rolls in adjacent positions.
#     """
#     grid = [list(line) for line in grid_lines]
#     rows = len(grid)
#     cols = len(grid[0])
    
#     accessible_count = 0
    
#     for row in range(rows):
#         for col in range(cols):
#             if grid[row][col] == '@':
#                 adjacent_count = count_adjacent_rolls(grid, row, col)
#                 if adjacent_count < 4:
#                     accessible_count += 1
    
#     return accessible_count

# # Read input file
# script_dir = Path(__file__).parent
# input_path = script_dir / 'input.txt'

# with open(input_path, 'r') as f:
#     grid_lines = [line.rstrip('\n') for line in f]

# # Solve the puzzle
# answer = count_accessible_rolls(grid_lines)
# print(f"Number of accessible rolls: {answer}")

from pathlib import Path

def count_adjacent_rolls(grid, row, col):
    """
    Count the number of paper rolls (@) in the 8 adjacent positions.
    """
    rows = len(grid)
    cols = len(grid[0])
    count = 0
    
    # Check all 8 adjacent positions (including diagonals)
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            # Skip the center position
            if dr == 0 and dc == 0:
                continue
            
            new_row = row + dr
            new_col = col + dc
            
            # Check if the position is within bounds
            if 0 <= new_row < rows and 0 <= new_col < cols:
                if grid[new_row][new_col] == '@':
                    count += 1
    
    return count

def find_accessible_rolls(grid):
    """
    Find all rolls that can be accessed by forklifts (have < 4 adjacent rolls).
    """
    rows = len(grid)
    cols = len(grid[0])
    accessible = []
    
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == '@':
                adjacent_count = count_adjacent_rolls(grid, row, col)
                if adjacent_count < 4:
                    accessible.append((row, col))
    
    return accessible

def remove_all_possible_rolls(grid_lines):
    """
    Keep removing accessible rolls until no more can be removed.
    Returns the total number of rolls removed.
    """
    grid = [list(line) for line in grid_lines]
    total_removed = 0
    
    while True:
        # Find all accessible rolls
        accessible = find_accessible_rolls(grid)
        
        if not accessible:
            # No more rolls can be removed
            break
        
        # Remove all accessible rolls
        for row, col in accessible:
            grid[row][col] = '.'
        
        total_removed += len(accessible)
    
    return total_removed

# Read input file
script_dir = Path(__file__).parent
input_path = script_dir / 'input.txt'

with open(input_path, 'r') as f:
    grid_lines = [line.rstrip('\n') for line in f]

# Solve Part 2
answer = remove_all_possible_rolls(grid_lines)
print(f"Part 2 - Total rolls removed: {answer}")
