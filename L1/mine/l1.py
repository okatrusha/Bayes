import json
import itertools
#from l1animal import topology, data, netwrok     
from l1asia import topology, data, netwrok     

parents = {root for root, child in topology}
children = {child for root, child in topology}
# Select roots that are not children
roots = parents - children
nodes_prob = {}
parsed_nodes_full = {}

def parse_node(node, parent):
    global nodes_prob
    if node not in nodes_prob:
        nodes_prob[node] = {}
        for state in data[node]:                
            state_probability = 0
            for parent_state in data[node][state]:
                state_probability += nodes_prob[parent][parent_state.split('.')[1]] * data[node][state][parent_state]
            nodes_prob[node][state] = state_probability        

    for c in [child for parent, child in topology if parent == node]:
        parse_node(c, node)            

for r in roots:
    states = {}
    for s in data[r]:
        states[s] = data[r][s]
    nodes_prob[r] = states
        
    parse_node(r, None)

# print("Nodes probabilities >>>>>>>>>>>>>>>")
# for pn in parsed_nodes:
#     for s in parsed_nodes[pn]:
#         print("Node: {}, State: {}, probability: {}".format(pn, s, parsed_nodes[pn][s]))
# print("<<<<<<<<<<<<<<< Nodes probabilities")
print("NETWORK: " + netwrok + "\n")

print("Nodes probabilities >>>>>>>>>>>>>>>")
for pn in nodes_prob:
    for s in nodes_prob[pn]:
        print("Node: {}, State: {}, probability: {}".format(pn, s, nodes_prob[pn][s]))
print("<<<<<<<<<<<<<<< Nodes probabilities\n")

with open("L1/mine/" + netwrok + "_nodes_probability.txt", 'w') as file:  # 'w' mode to overwrite the file
    for pn in nodes_prob:
        for s in nodes_prob[pn]:
            file.write("Node: {}, State: {}, probability: {}".format(pn, s, nodes_prob[pn][s]) + "\n")
            

# Generate combinations of states per node
nodes = nodes_prob.keys()
states = [list(node_states.keys()) for node_states in nodes_prob.values()]

# Cartesian product of all states per node
combinations = list(itertools.product(*states))

def find_parents(node):
    # Find all parents for the given node
    parents = [parent for parent, child in topology if child == node]
    return parents

# Display combinations
all_states = []
for combo in combinations:
    all_states.append(dict(zip(nodes, combo)))


print("Full probabilities >>>>>>>>>>>>>>>")

probsum = 0
prob_comblist = []
with open("L1/mine/" + netwrok + "_full_probability.txt", 'w') as file:  # 'w' mode to overwrite the file
    for combination in all_states:
        probability = 1        
        prob_comb =[]
        for node in combination:
            if node in roots:
                probability *= data[node][combination[node]]
                prob_comb.append(node + " " + combination[node] + " : " + str(data[node][combination[node]]))        
            else:
                for parent in find_parents(node):
                    probability *= data[node][combination[node]][parent + '.' + combination[parent]]
                    prob_comb.append(node + " " + combination[node] + " "+ parent + '.' + combination[parent] +
                                    " : " + str(data[node][combination[node]][parent + '.' + combination[parent]]))
        #if (probability != 0):
        probsum += probability
        if (probability != 0):
            print(str(combination) + " Probability: " + str(probability))
        file.write(str(combination) + " Probability: " + str(probability) + "\n")
        #print()
    #prob_comblist.append(combination + [probability])

        #print(combination, " ", probability)
print("<<<<<<<<<<<<<<<< Full probabilities")
        

#print("Node: {}, State: {}, probability: {}".format(pn, s, nodes_prob[pn][s]))
#print(all_states)