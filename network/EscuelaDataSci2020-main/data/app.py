import networkx as nx
import matplotlib.pylab as plt

g = nx.read_graphml("contact_network.graphml")



print(len(g.nodes()),len((g.edges()))) # num. nodos
# num. aristas

# # Grafica temprana
# nx.draw(g)
# plt.show()

# Exportamos la red
nx.write_graphml(file="red_mis.graphml")
