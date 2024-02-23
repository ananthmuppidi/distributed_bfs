#!/usr/bin/env python3
"""reducer.py for BFS iteration"""
import sys

INF = 404  # We use 404 to represent "infinity"

def emit(node, distance, neighbors):
    # Emit the node with its distance and its adjacency list
    # The distance will be a string "INF" if it is INF, otherwise the integer distance
    print(f"{node} {distance}|{','.join(neighbors)}")

current_node = None
current_distance = INF
current_neighbors = []

for line in sys.stdin:
    line = line.strip()
    node_id, value = line.split(' ', 1)

    # Check if this is an update line (denoted by '@') or an adjacency list line
    if '@' in value:
        # This is a distance update, parse it accordingly
        new_distance = int(value.rstrip('@'))
        if current_node != node_id:
            # If moving to a new node, we emit the current node's information first
            if current_node is not None:
                emit(current_node, current_distance, current_neighbors)
            current_node = node_id
            current_distance = new_distance
        else:
            # If still on the same node, we update the current distance if it's smaller
            current_distance = min(current_distance, new_distance)
    else:
        # This is an adjacency list line, it may also contain a distance
        distance, neighbors = value.split('|')
        neighbors = neighbors.split(',')
        distance = int(distance)
        if current_node != node_id:
            # If this is a new node, emit the previous node if there was one
            if current_node is not None:
                emit(current_node, current_distance, current_neighbors)
            current_node = node_id
            current_distance = distance
            current_neighbors = neighbors
        else:
            # We only update the distance if it's smaller than the current distance
            if distance < current_distance:
                current_distance = distance
            # We always update the neighbors to ensure we have the latest list
            current_neighbors = neighbors

# Don't forget to emit the last node's information
if current_node is not None:
    emit(current_node, current_distance, current_neighbors)
