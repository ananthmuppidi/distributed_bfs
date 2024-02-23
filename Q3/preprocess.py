#!/usr/bin/env python3
import sys

SOURCE_NODE = '1'
MAX_DISTANCE = sys.maxsize  # Use a large number to represent infinity.

for line in sys.stdin:
    parts = line.strip().split()
    node = parts[0]
    neighbors = parts[1:]
    
    # The source node starts with distance 0, all others with MAX_DISTANCE.
    distance = 0 if node == SOURCE_NODE else MAX_DISTANCE
    neighbors_str = ' '.join(neighbors)
    
    print(f'{node}\t{distance}\t{neighbors_str}')
