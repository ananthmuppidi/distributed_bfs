import os
import sys
import heapq

def parse_line(line):
    """Parse a line and return node, distance, and neighbors."""
    node, rest = line.strip().split(' ', 1)
    distance, neighbors = rest.split('|')
    return node, int(distance), neighbors

def file_line_generator(filename):
    """Generator to yield node, distance, neighbors, and the original line from a file."""
    with open(filename, 'r') as file:
        for line in file:
            node, distance, neighbors = parse_line(line)
            yield node, distance, neighbors, line

def combine_outputs(input_dir, final_output_filename):
    file_generators = []
    current_lines = []

    # Initialize generators for each part file and get the first line from each
    for filename in os.listdir(input_dir):
        if filename.startswith('part-'):
            generator = file_line_generator(os.path.join(input_dir, filename))
            try:
                first_line = next(generator)
            except StopIteration:
                continue  # Skip empty files
            file_generators.append(generator)
            current_lines.append(first_line)

    # Use a heap to always get the smallest current node being processed
    heapq.heapify(current_lines)

    with open(final_output_filename, 'w') as final_file:
        while current_lines:
            # Get the smallest node from the heap
            node, distance, neighbors, line = heapq.heappop(current_lines)

            # Process all entries for this node
            min_distance = distance
            while current_lines and current_lines[0][0] == node:
                _, next_distance, _, _ = current_lines[0]
                min_distance = min(min_distance, next_distance)
                heapq.heappop(current_lines)  # Remove the processed entry

            # Emit the minimum distance and the last seen neighbors for this node
            distance_str = str(min_distance) if min_distance != float('inf') else 'INF'
            final_file.write(f"{node} {distance_str}|{neighbors}\n")

            # Advance generators that were pointing to the current node and get next lines
            for generator in file_generators:
                try:
                    next_line = next(generator)
                    heapq.heappush(current_lines, next_line)
                except StopIteration:
                    pass  # This file is done, continue with others

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 combine.py <input_directory> <final_output_file>")
        sys.exit(1)

    input_dir = sys.argv[1]
    final_output_filename = sys.argv[2]
    combine_outputs(input_dir, final_output_filename)
