import random
import copy
import sys
import time
from collections import defaultdict, OrderedDict

sys.setrecursionlimit(100000)
t = 0
ranking_dict = OrderedDict()
explore_list = []
random.seed()
scc_dict = {}

def forward_dfs(large_ranking_node):
    global scc_dict
    global forward_node_dict
    global unexplored_nodes
    scc_size = 0
    while len(explore_list) > 0:
        should_i_continue = True
        start_node = explore_list[len(explore_list) - 1]
        if str(start_node) in unexplored_nodes:
            scc_size += 1
            unexplored_nodes.pop(str(start_node))
        explore_nodes = forward_node_dict[str(start_node)]
        for node in explore_nodes:
            if str(node) in unexplored_nodes:
                explore_list.append(node)
                should_i_continue = False
                break
        if should_i_continue:
            explore_list.pop()
    scc_dict[large_ranking_node] = scc_size

def reverse_dfs():
    global t
    global ranking_dict
    global backward_node_dict
    global unexplored_nodes

    while len(explore_list) > 0:
        should_i_continue = True
        start_node = explore_list[len(explore_list) - 1]
        explore_nodes = backward_node_dict[str(start_node)]
        for node in explore_nodes:
            if str(node) in unexplored_nodes:
                explore_list.append(node)
                unexplored_nodes.pop(str(node))
                should_i_continue = False
                break
        if should_i_continue:
            if start_node not in ranking_dict:
                ranking_dict[start_node] = t
                t += 1
            explore_list.pop()

with open('/home/jackson/Documents/Coursera/Algorithms1/Homework4/input.txt') as f:
    forward_node_dict = defaultdict(list)
    backward_node_dict = defaultdict(list)
    for line in f.readlines():
        line_items = line.split()
        forward_node_dict[line_items[0]].append(line_items[1])
        backward_node_dict[line_items[1]].append(line_items[0])

    unexplored_nodes = copy.deepcopy(backward_node_dict)
    for node in backward_node_dict.keys():
        if str(node) in unexplored_nodes:
            explore_list.append(node)
            unexplored_nodes.pop(str(node))
            reverse_dfs()
    unexplored_nodes = copy.deepcopy(forward_node_dict)
    for node in reversed(ranking_dict):
        explore_list.append(node)
        forward_dfs(node)

print sorted(scc_dict.values())
        

