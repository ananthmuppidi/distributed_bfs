#!/usr/bin/env python3
"""mapper.py for BFS iteration"""
import sys

# mapper needs to run one iteration of a bfs, and emit:
#   1. Any updates made to distances
#   2. The entire adjacency matrix, so that the output file contains that information still 


def emit(key, value):
    print(f"{key} {value}")

for line in sys.stdin:
    line = line.strip()
    node_id, value = line.split(' ', 1)
    distance, neighbours = value.split('|')
    distance = int(distance)
    neighbours = neighbours.split(',') if neighbours else []
    # if we know that the distance of the current node is less than infinity (represented by 404), we can update the distances of its neighbours
    if distance <  404:
        # then emit the updated distance and the adjacency list
        for neighbour in neighbours:
            # Emit message with updated distance for neighbors, emit: node_id distancce,adjacency_list
            emit(neighbour, f"{distance + 1}@")
    emit(node_id, f"{distance}|{','.join(neighbours)}")