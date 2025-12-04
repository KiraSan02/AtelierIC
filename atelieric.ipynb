import networkx as nx
import matplotlib.pyplot as plt

def draw_graph(title, edges):
    """
    edges : liste de tuples (source, relation, target)
    """
    G = nx.DiGraph()

    # Add nodes and labeled edges
    for src, rel, tgt in edges:
        G.add_node(src)
        G.add_node(tgt)
        G.add_edge(src, tgt, label=rel)

    pos = nx.spring_layout(G, seed=42)

    plt.figure(figsize=(10, 6))
    nx.draw(G, pos, with_labels=True, node_size=2500, node_color="#E6F2FF",
            font_size=10, arrowsize=20, arrowstyle='-|>')

    # Draw edge labels
    edge_labels = {(u, v): d["label"] for u, v, d in G.edges(data=True)}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=9)

    plt.title(title)
    plt.show()


# -------------------------------
# EXERCICE 1
# -------------------------------
edges_ex1 = [
    ("Oiseau", "sorte de", "Animal"),
    ("Mammifère", "sorte de", "Animal"),
    ("Chauve-souris", "sorte de", "Oiseau"),
    ("Chauve-souris", "sorte de", "Mammifère"),
    ("Oiseau", "peut", "Voler"),
    ("Oiseau", "peut", "pondre"),
    ("Mammifère", "peut", "Allaiter"),
    ("Chauve-souris", "exclusion", "pondre")
]

"""
2- chauve-souris hérite peut voler, ne peut pas pondre
3- conflit est chauve-souris ne peut pas pondre
"""

# -------------------------------
# EXERCICE 2
# -------------------------------
edges_ex2 = [
    ("Poisson", "vit_dans", "Eau"),
    ("Animal_vivant_dans_Eau", "peut", "Nager"),
    ("Dauphin", "sorte de", "Mammifère"),
    ("Mammifère", "sorte de", "Animal"),
    ("Dauphin", "vit_dans", "Eau"),
    ("Animal_vivant_dans_Eau", "est", "Animal")
]

"""
Dauphin vit dans l'eau -> Dauphin est un mammifere  -> mammifere est un animal -> tout les animaux qui vivent das l'eau peuvent nager -> dauphin peut nager
"""

# -------------------------------
# EXERCICE 3
# -------------------------------
edges_ex3 = [
    ("Étudiant", "est", "Personne"),
    ("Enseignant", "est", "Personne"),
    ("Professeur", "sorte de", "Enseignant"),
    ("Professeur", "sorte de", "Chercheur"),
    ("Personne", "possede", "Âge"),
    ("Étudiant", "étudie", "Domaine"),
    ("Enseignant", "enseigne", "Domaine"),
    ("domaine_etudie" ,"est", "Domaine")
    ("doamine_enseigné" ,"est", "Domaine")
    ("doamine_enseigné" ,"est", "domaine_etudie")

]
"""
2- contrainte : le domaine enseigné doit être le même que le domaine étudié pour un même cours
"""
# -------------------------------
# EXERCICE 4
# -------------------------------
edges_ex4 = [
    ("Chien", "est", "Animal"),
    ("Chat", "est", "Animal"),
    ("Animal", "est", "ÊtreVivant"),
    ("Chien", "lié", "Os"),
    ("Chat", "lié", "Lait"),
    ("Os", "sorte de", "Nourriture")
]

"""
Étape 0 (activation initiale)
Chien = 1
Niveau 1 (activation × 0.5)
Depuis Chien :
Animal = 0.5
Os = 0.5
Niveau 2 (activation × 0.5² = 0.25)
Depuis Animal :
ÊtreVivant = 0.25
Depuis Os :
Nourriture = 0.25
Niveau 3 (activation × 0.5³ = 0.125)
Depuis ÊtreVivant : rien
Depuis Nourriture : rien
"""

# -------------------------------
# EXERCICE 5
# -------------------------------
edges_ex5 = [
    ("Oiseau", "peut", "Voler"),
    ("Oiseau", "peut", "vivre-eau"),
    ("OiseauNocturne", "sorte de", "Oiseau"),
    ("OiseauNocturne", "peut", "ChasserNuit"),
    ("Hibou", "sorte de", "OiseauNocturne"),
    ("Pingouin", "sorte de", "Oiseau"),
    ("Pingouin", "exclusion", "voler"),
    ("Hibou", "exclusion", "vivre-eau")
]

"""
Hibou ->  chasse la nuit et peut voler et ne vit pas dans l'eau
Pingouin -> vit dans l'eau et ne vole pas
"""

# -------------------------------
# EXERCICE 6
# -------------------------------
edges_ex6 = [
    ("Étudiant", "est", "Personne"),
    ("Étudiant", "est pas", "Travailleur"),
    ("Ali", "instanceOf", "Étudiant")
]

# -------------------------------
# EXERCICE 7
# -------------------------------
edges_ex7 = [
    ("Fièvre", "symptôme", "Maladie"),
    ("Toux", "symptôme", "MaladieRespiratoire"),
    ("Grippe", "isa", "MaladieRespiratoire"),
    ("Grippe", "hasSymptom", "Fièvre"),
    ("Grippe", "hasSymptom", "Toux"),
    ("Pneumonie", "isa", "MaladieRespiratoire"),
    ("Pneumonie", "hasSymptom", "Fièvre"),
    ("Pneumonie", "hasSymptom", "DouleurPoitrine")
]
"""
Si un patient présente la fièvre et toux , les maladies possible sont :
Grippe .
"""

# -----------------
# PRÉVISUALISATION 
# ------------------


draw_graph("Exercice 1", edges_ex1)
draw_graph("Exercice 2", edges_ex2)
draw_graph("Exercice 3", edges_ex3)
draw_graph("Exercice 4", edges_ex4)
draw_graph("Exercice 5", edges_ex5)
draw_graph("Exercice 6", edges_ex6)
draw_graph("Exercice 7", edges_ex7)

