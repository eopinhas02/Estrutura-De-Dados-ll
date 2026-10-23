import networkx as nx

# ---------- atividade 1 e 2 ----------
g = nx.MultiGraph()  # multigraph porque tem laco
g.add_nodes_from([1, 2, 3, 4, 5])
g.add_edges_from([(1, 2), (1, 4), (1, 5), (2, 3), (3, 4), (4, 4)])

print("ordem |V| =", g.number_of_nodes())
print("tamanho |E| =", g.number_of_edges())
print("tem laco?", nx.number_of_selfloops(g) > 0)
for v in g.nodes:
    # no networkx o laco ja conta 2 no grau
    vizinhos = sorted(set(g.neighbors(v)))
    print("vertice", v, "| grau", g.degree(v), "| adjacentes", vizinhos)

# ---------- atividade 4 ----------
ruas = nx.DiGraph()
ruas.add_edges_from([("A", "B"), ("B", "C"), ("C", "D"),
                     ("D", "A"), ("B", "D"), ("E", "A")])
print("\nvertice B -> entrada:", ruas.in_degree("B"), "| saida:", ruas.out_degree("B"))

# ---------- atividade 5 ----------
G = nx.Graph([(1, 2), (2, 3), (3, 4), (4, 1)])
H = nx.Graph([("a", "c"), ("c", "b"), ("b", "d"), ("d", "a")])
f = {1: "a", 2: "c", 3: "b", 4: "d"}
preserva = True
for x, y in G.edges:
    if not H.has_edge(f[x], f[y]):
        preserva = False
print("\nmeu mapeamento preserva as arestas?", preserva)
print("networkx tambem diz que sao isomorfos?", nx.is_isomorphic(G, H))

# ---------- atividade 7 ----------
g7 = nx.Graph()
g7.add_edges_from([("A", "B"), ("A", "C"), ("A", "D"), ("A", "E"),
                   ("A", "F"), ("A", "G"), ("B", "C"), ("B", "D"),
                   ("B", "E"), ("C", "D"), ("C", "E"), ("F", "H")])
sequencia = sorted(grau for v, grau in g7.degree)
print("\nsequencia obtida:", sequencia)
print("bate com a pedida?", sequencia == [1, 1, 2, 3, 3, 4, 4, 6])
