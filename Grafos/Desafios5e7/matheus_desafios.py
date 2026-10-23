# desafios 5 e 7 - grafos
# aluno: matheus lopes rodrigues
# usei esse codigo so pra conferir as contas que fiz no papel

# ---------- desafio 5: isomorfismo ----------
g_vertices = [1, 2, 3, 4]
g_arestas = [(1, 2), (2, 3), (3, 4), (4, 1)]

h_vertices = ["a", "b", "c", "d"]
h_arestas = [("a", "c"), ("c", "b"), ("b", "d"), ("d", "a")]


def graus(vertices, arestas):
    g = {}
    for v in vertices:
        g[v] = 0
    for x, y in arestas:
        g[x] += 1
        g[y] += 1
    return g


print("G -> ordem:", len(g_vertices), "| tamanho:", len(g_arestas))
print("H -> ordem:", len(h_vertices), "| tamanho:", len(h_arestas))
print("graus de G:", graus(g_vertices, g_arestas))
print("graus de H:", graus(h_vertices, h_arestas))

# a correspondencia que eu achei
f = {1: "a", 2: "c", 3: "b", 4: "d"}

ok = True
for x, y in g_arestas:
    nx, ny = f[x], f[y]
    existe = (nx, ny) in h_arestas or (ny, nx) in h_arestas
    print("(", x, ",", y, ") vira (", nx, ",", ny, ") ->", existe)
    if not existe:
        ok = False
print("isomorfos?", ok)

# ---------- desafio 7: sequencia de graus ----------
arestas7 = [
    ("A", "B"), ("A", "C"), ("A", "D"), ("A", "E"), ("A", "F"), ("A", "G"),
    ("B", "C"), ("B", "D"), ("B", "E"),
    ("C", "D"), ("C", "E"),
    ("F", "H"),
]
vertices7 = ["A", "B", "C", "D", "E", "F", "G", "H"]

g7 = graus(vertices7, arestas7)
print()
for v in vertices7:
    print(v, "tem grau", g7[v])
sequencia = sorted(g7.values())
soma = sum(sequencia)
print("sequencia:", sequencia)
print("soma dos graus:", soma, "| arestas:", len(arestas7))
print("soma = 2 x arestas?", soma == 2 * len(arestas7))
