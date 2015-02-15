import timeit
import random
import copy
from collections import OrderedDict

min_cut = 200
random.seed()
def contraction_algorithm(nodes_dict):
    global min_cut
    while len(nodes_dict) > 2:
        node_1 = random.choice(nodes_dict.keys())
        node_1_connections = nodes_dict.pop(node_1)
        node_2 = random.choice(node_1_connections)
        for node_connection in node_1_connections:
            nodes_dict[node_connection].remove(node_1)
            if node_2 != node_connection:
                nodes_dict[node_2].append(node_connection)
                nodes_dict[node_connection].append(node_2)

    min_cut_for_this_iteration = len(nodes_dict[nodes_dict.keys()[0]])
    if min_cut > min_cut_for_this_iteration:
        min_cut = min_cut_for_this_iteration
        print min_cut
with open('/home/jackson/Documents/Coursera/Algorithms1/Homework3/input.txt') as f:
    node_dictionary = {}
    for line in f.readlines():
        line_items = line.split()
        node_dictionary[line_items[0]] = line_items[1::]

    for i in range(4000):
        dict_2 = copy.deepcopy(node_dictionary)
        contraction_algorithm(dict_2)
