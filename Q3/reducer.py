#!/usr/bin/env python3
import sys

INF = 404  # Use 404 to represent "infinity"

def emit(node, distance, neighbors):
    # Emit the node with its distance and its adjacency list
    distance_str = str(distance) if distance != INF else "INF"
    print(f"{node}\t{distance_str}|{','.join(neighbors)}")

current_node = None
current_distance = INF
current_neighbors = []

for line in sys.stdin:
    line = line.strip()
    node_id, value = line.split('\t', 1)

    if '@' in value:
        # This is a distance update, parse it accordingly
        new_distance = int(value.rstrip('@'))
    else:
        # This is an adjacency list line; it may also contain a distance
        distance, neighbors_str = value.split('|', 1)
        new_distance = int(distance)
        neighbors = neighbors_str.split(',') if neighbors_str else []

    if current_node is None or current_node != node_id:
        # If this is a new node, emit the previous node if there was one
        if current_node is not None:
            emit(current_node, current_distance, current_neighbors)
        current_node = node_id
        current_distance = new_distance
        current_neighbors = neighbors
    else:
        # Update the current distance if the new one is smaller
        current_distance = min(current_distance, new_distance)
        # Update neighbors if this isn't just a distance update
        if '@' not in value:
            current_neighbors = neighbors

# Don't forget to emit the last node's information
if current_node is not None:
    emit(current_node, current_distance, current_neighbors)
