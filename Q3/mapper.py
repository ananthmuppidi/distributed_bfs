#!/usr/bin/env python3
import sys

SOURCE_NODE = '1'  # Define the source node
MAX_DISTANCE = 404  # Infinity representation

def emit(key, value):
    print(f"{key}\t{value}")
try:

    for line in sys.stdin:
        line = line.strip()
        if '|' in line:
            node_id, value = line.split(' ', 1)
            distance, neighbours = value.split('|', 1)
            distance = int(distance)
        else:
            # Processing initial input, no '|' found
            parts = line.split()
            node_id = parts[0]
            neighbours = parts[1:]

        # Set initial distance for the source node or others
            distance = 0 if node_id == SOURCE_NODE else MAX_DISTANCE
        # Convert neighbours list to a string for consistent output
            neighbours = ','.join(neighbours)

    # Emit the current node with its distance and adjacency list
        emit(node_id, f"{distance}|{neighbours}")

    # If this is not the initial input, also check and emit updates for neighbours
        if distance < MAX_DISTANCE:
            for neighbour in neighbours.split(','):
            # Emit potential distance update for each neighbour
                emit(neighbour, f"{distance + 1}@")
except Exception as e:
    sys.stderr.write(f"ERROR: {str(e)}\n")