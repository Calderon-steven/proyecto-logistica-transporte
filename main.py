from flota import leer_paquetes, crear_flota, asignar_paquetes
from rutas import crear_grafo_ciudad, calcular_ruta_mas_corta

# Cargar datos
paquetes = leer_paquetes("paquetes.csv")
flota = crear_flota()

print("Paquetes cargados:", len(paquetes))
print("Vehiculos en la flota:", len(flota))

print("\nIniciando asignacion de paquetes...")
no_asignados = asignar_paquetes(paquetes, flota)

print("\n--- Resumen de vehiculos ---")
for v in flota:
    if v.paquetes:
        print(v.tipo, "- Peso:", v.peso_usado, "kg - Volumen:", v.volumen_usado, "m3")

if no_asignados:
    print("\nPaquetes que no se pudieron asignar:", len(no_asignados))

# Rutas
print("\n--- Calculo de rutas ---")
G = crear_grafo_ciudad()

# Buscamos el primer vehiculo que tenga paquetes para mostrar su ruta
vehiculo_ejemplo = None
for v in flota:
    if len(v.paquetes) > 0:
        vehiculo_ejemplo = v
        break

if vehiculo_ejemplo:
    print("Ruta para el vehiculo:", vehiculo_ejemplo.tipo)
    distancia_total = 0
    
    for p in vehiculo_ejemplo.paquetes:
        ruta, dist = calcular_ruta_mas_corta(G, "Deposito", p["id"])
        if ruta:
            # Imprimimos el camino unido por flechas
            camino = " -> ".join(ruta)
            print("Paquete", p["id"], ":", camino, "(", dist, "km )")
            distancia_total += dist
            
    print("Distancia total de la ruta:", distancia_total, "km")