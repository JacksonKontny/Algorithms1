import random
import copy
import sys
import time
from collections import defaultdict, OrderedDict

random.seed()

def find_shortest_path(node_to, node_from, explore_dict, explored_list):
    explored_list.append(node_from)
    nodes_to_explore = []
    nodes_to_explore.append(explore_dict[node_from])
    keep_going = True
    while keep_going == True:
        min_distance = float('inf')
        for node in nodes_to_explore:
            distance = int(node['distance'])
            network = node['network']
            for path in network:
                p = path.split(',')
                if p[0] not in explored_list:
                    if int(p[1]) + int(distance) < min_distance:
                        min_distance = int(p[1]) + int(distance)
                        next_node = p[0]
        if next_node == node_to:
            return min_distance
        explored_list.append(str(next_node))
        next_node = explore_dict[str(next_node)]
        next_node['distance'] = min_distance
        nodes_to_explore.append(next_node)
        if min_distance == float('inf'):
            return min_distance



with open('/home/jackson/Documents/Coursera/Algorithms1/Homework5/data.txt') as f:
    node_dict = {}
    for line in f.readlines():
        line = line.split('\t')
        line.pop()
        node = line.pop(0)
        node_dict[node] = {'distance':0, 'network':line}

solution_dict = {}
find_shortest_path_to = ['7','37','59','82','99','115','133','165','188','197']
for item in find_shortest_path_to:
    explored_list = []
    explore_dict = copy.deepcopy(node_dict)
    solution_dict[item] = find_shortest_path(item, '1', node_dict, explored_list)
    print item, solution_dict[item]
