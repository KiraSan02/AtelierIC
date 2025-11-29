import networkx as nx
import matplotlib.pyplot as plt


G = nx.DiGraph()

edges = [
    ("Chien", "est", "Animal"),
    ("Chat", "est", "Animal"),
    ("Animal", "est", "ÊtreVivant"),
    ("Chien", "lié", "Os"),
    ("Chat", "lié", "Lait"),
    ("Os", "sorte de", "Nourriture")
]

for src, rel, tgt in edges:
    G.add_edge(src, tgt, label=rel)

activation = {n: 0.0 for n in G.nodes()}
activation["Chien"] = 1.0

decay = 0.5
levels = 3

frontier = {"Chien"}

for _ in range(levels):
    new_frontier = set()
    for node in frontier:
        val = activation[node] * decay
        for neigh in G.successors(node):
            activation[neigh] = max(activation[neigh], val)
            new_frontier.add(neigh)
    frontier = new_frontier

# -----------------------------
# 3) Affichage ultra simple
# -----------------------------
pos = nx.spring_layout(G, seed=0)

plt.figure(figsize=(9, 6))

nx.draw(G, pos, with_labels=False, node_size=2000)

# Labels avec valeur d'activation
labels = {n: f"{n}\n({activation[n]:.2f})" for n in G.nodes()}
nx.draw_networkx_labels(G, pos, labels)

# Labels pour les relations
edge_labels = {(u, v): d["label"] for u, v, d in G.edges(data=True)}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

plt.axis("off")
plt.title("Propagation d'activation )
plt.show()
