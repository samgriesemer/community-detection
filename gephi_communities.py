# put together communities
def gehpi_communities():
    G = nx.read_graphml('data/metagraph.graphml')
    comms = {}
    for node in list(G.nodes()):
        mc = G.node[node]['Modularity Class']
        if comms.get(mc) is None:
            comms[mc] =  []
        comms[mc].append(node)
    subgraphs = [set(nodes) for num,nodes in comms.items()]
    return subgraphs
