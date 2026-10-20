import networkx as nx

def crear_grafo_ciudad():
    G = nx.Graph()
    
    # Conexiones: (Nodo Origen, Nodo Destino, Distancia en km)
    conexiones = [
        ("Deposito", "P001", 3.2),
        ("Deposito", "P002", 4.5),
        ("Deposito", "P003", 6.1),
        ("P001", "P004", 2.0),
        ("P002", "P005", 3.8),
        ("P003", "P006", 1.5),
        ("P004", "P007", 2.7),
        ("P005", "P008", 2.2),
        ("P006", "P009", 3.0),
        ("P007", "P010", 1.8),
        ("P008", "P011", 4.0),
        ("P009", "P012", 2.5),
        ("P010", "P013", 1.9),
        ("P011", "P014", 3.3),
        ("P012", "P015", 2.1),
        ("P013", "P015", 4.2),
        ("P014", "P001", 5.0),
    ]
    G.add_weighted_edges_from(conexiones)
    return G

def calcular_ruta_mas_corta(G, origen, destino):
    try:
        # Uso del algoritmo de Dijkstra provisto por NetworkX
        ruta = nx.shortest_path(G, source=origen, target=destino, weight="weight")
        distancia = nx.shortest_path_length(G, source=origen, target=destino, weight="weight")
        return ruta, distancia
    except nx.NetworkXNoPath:
        return None, None

if __name__ == "__main__":
    print("=== CÁLCULO DE RUTAS ÓPTIMAS ===")
    G = crear_grafo_ciudad()
    print(f"Nodos en el grafo: {G.number_of_nodes()}")
    print(f"Aristas (conexiones): {G.number_of_edges()}")

    destinos = ["P003", "P007", "P012"]
    
    for destino in destinos:
        ruta, distancia = calcular_ruta_mas_corta(G, "Deposito", destino)
        if ruta:
            print(f"\nRuta hacia {destino}:")
            print(f"  Camino: {' -> '.join(ruta)}")
            print(f"  Distancia total: {distancia:.2f} km")
        else:
            print(f"\nNo hay ruta hacia {destino}") 