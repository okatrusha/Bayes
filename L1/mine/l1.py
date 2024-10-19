import json
from l1animal import topology, data 
#from l1asia import topology, data 

parents = {root for root, child in topology}
children = {child for root, child in topology}
# Select roots that are not children
roots = parents - children
parsed_nodes = {}
parsed_nodes_full = {}

def parse_node(node, parent):
    global parsed_nodes
    if node not in parsed_nodes:
        parsed_nodes[node] = {}
        for state in data[node]:                
            state_probability = 0
            for parent_state in data[node][state]:
                state_probability += parsed_nodes[parent][parent_state] * data[node][state][parent_state]
            parsed_nodes[node][state] = state_probability        

    for c in [child for parent, child in topology if parent == node]:
        parse_node(c, node)            

for r in roots:
    states = {}
    for s in data[r]:
        states[s] = data[r][s]
    parsed_nodes[r] = states
        
    parse_node(r, None)

# print("Nodes probabilities >>>>>>>>>>>>>>>")
# for pn in parsed_nodes:
#     for s in parsed_nodes[pn]:
#         print("Node: {}, State: {}, probability: {}".format(pn, s, parsed_nodes[pn][s]))
# print("<<<<<<<<<<<<<<< Nodes probabilities")

print("Nodes probabilities >>>>>>>>>>>>>>>")
for pn in parsed_nodes:
    for s in parsed_nodes[pn]:
        print("Node: {}, State: {}, probability: {}".format(pn, s, parsed_nodes[pn][s]))
print("<<<<<<<<<<<<<<< Nodes probabilities")

# all_states = []
# for pn in parsed_nodes:
#     for s in parsed_nodes[pn]:
#         all_states.append((pn, s))

