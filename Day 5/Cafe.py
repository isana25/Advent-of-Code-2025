###############################################

## Part One

###############################################
from pathlib import Path

def is_fresh(ingredient_id, fresh_ranges):
    """
    Check if an ingredient ID is fresh by checking if it falls into any range.
    Ranges are inclusive, and an ID is fresh if it's in ANY range.
    """
    for start, end in fresh_ranges:
        if start <= ingredient_id <= end:
            return True
    return False

def count_fresh_ingredients(database_text):
    """
    Parse the database and count how many available ingredients are fresh.
    """
    lines = database_text.strip().split('\n')
    
    # Find the blank line that separates ranges from available IDs
    blank_line_index = lines.index('')
    
    # Parse fresh ID ranges
    fresh_ranges = []
    for i in range(blank_line_index):
        start, end = map(int, lines[i].split('-'))
        fresh_ranges.append((start, end))
    
    # Parse available ingredient IDs
    available_ids = []
    for i in range(blank_line_index + 1, len(lines)):
        if lines[i].strip():
            available_ids.append(int(lines[i].strip()))
    
    # Count fresh ingredients
    fresh_count = 0
    for ingredient_id in available_ids:
        if is_fresh(ingredient_id, fresh_ranges):
            fresh_count += 1
    
    return fresh_count

# Read input file
script_dir = Path(__file__).parent
input_path = script_dir / 'input.txt'

with open(input_path, 'r') as f:
    database_text = f.read()

# Solve the puzzle
answer = count_fresh_ingredients(database_text)
print(f"Number of fresh ingredients: {answer}")

###############################################

## Part two

###############################################


from pathlib import Path

def merge_ranges(ranges):
    """
    Merge overlapping ranges to avoid double-counting IDs.
    Returns a list of non-overlapping ranges.
    """
    if not ranges:
        return []
    
    # Sort ranges by start point
    sorted_ranges = sorted(ranges)
    
    merged = [sorted_ranges[0]]
    
    for current_start, current_end in sorted_ranges[1:]:
        last_start, last_end = merged[-1]
        
        # Check if current range overlaps or is adjacent to the last merged range
        if current_start <= last_end + 1:
            # Merge by extending the end if necessary
            merged[-1] = (last_start, max(last_end, current_end))
        else:
            # No overlap, add as new range
            merged.append((current_start, current_end))
    
    return merged

def count_all_fresh_ids(database_text):
    """
    Count all ingredient IDs that are considered fresh according to the ranges.
    Ignores the available ingredient IDs section.
    """
    lines = database_text.strip().split('\n')
    
    # Find the blank line
    blank_line_index = lines.index('')
    
    # Parse fresh ID ranges
    fresh_ranges = []
    for i in range(blank_line_index):
        start, end = map(int, lines[i].split('-'))
        fresh_ranges.append((start, end))
    
    # Merge overlapping ranges to avoid double-counting
    merged_ranges = merge_ranges(fresh_ranges)
    
    # Count total IDs in all merged ranges
    total_fresh = 0
    for start, end in merged_ranges:
        total_fresh += (end - start + 1)
    
    return total_fresh

# Read input file
script_dir = Path(__file__).parent
input_path = script_dir / 'input.txt'

with open(input_path, 'r') as f:
    database_text = f.read()

# Solve Part 2
answer = count_all_fresh_ids(database_text)
print(f"Part 2 - Total fresh ingredient IDs: {answer}")
