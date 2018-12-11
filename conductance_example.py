def gehpi_communities(k):
    G = nx.read_graphml('mmgephi graphs/mmgephi_' + str(k) +'.graphml')
    comms = {}
    for node in list(G.nodes()):
        mc = G.node[node]['Modularity Class']
        if comms.get(mc) is None:
            comms[mc] =  []
        comms[mc].append(node)
    subgraphs = [set(nodes) for num,nodes in comms.items()]
    return G, subgraphs

def conductances(G, communities):
    '''Compute conductance for a list of communities
    '''
    return [nx.algorithms.cuts.conductance(G, community) for community in communities]

ks = np.arange(10, 110, 10)


# G_community_list = [(G, <list of sets>), 
# (G, <list of sets>), ..., 
# (G, <list of sets>)]
G_community_list = [gehpi_communities(k) for k in ks]

conductance_list = [conductances(G, com) for G, com in G_community_list]

avg_conductances = []
std_conductances = []
for c in conductance_list:
    c_arr = np.array(c)
    avg_conductances.append(np.average(c_arr))
    std_conductances.append(np.std(c_arr))
