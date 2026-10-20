import csv

class Vehiculo:
    def __init__(self, tipo, peso_max, volumen_max):
        self.tipo = tipo
        self.peso_max = peso_max
        self.volumen_max = volumen_max
        self.peso_usado = 0
        self.volumen_usado = 0
        self.paquetes = []

    def puede_llevar(self, paquete):
        if self.peso_usado + paquete["peso"] > self.peso_max:
            return False
        if self.volumen_usado + paquete["volumen"] > self.volumen_max:
            return False
        return True

    def asignar(self, paquete):
        self.paquetes.append(paquete)
        self.peso_usado += paquete["peso"]
        self.volumen_usado += paquete["volumen"]

    def mostrar_resumen(self):
        print(f"\n--- Vehículo: {self.tipo} ---")
        print(f"Peso usado: {self.peso_usado:.2f} / {self.peso_max} kg")
        print(f"Volumen usado: {self.volumen_usado:.4f} / {self.volumen_max} m3")
        print(f"Paquetes asignados: {len(self.paquetes)}")
        for p in self.paquetes:
            print(f"  - {p['id']} ({p['peso']} kg)")

def leer_paquetes(ruta_archivo):
    paquetes = []
    with open(ruta_archivo, newline="", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            peso = float(fila["peso_kg"])
            alto = float(fila["alto_cm"])
            ancho = float(fila["ancho_cm"])
            prof = float(fila["profundidad_cm"])
            
            volumen = (alto * ancho * prof) / 1000000
            paquetes.append({
                "id": fila["id_paquete"],
                "peso": peso,
                "volumen": volumen,
                "lat": float(fila["latitud"]),
                "lon": float(fila["longitud"])
            })
    return paquetes

def crear_flota():
    flota = []
    for i in range(3):
        flota.append(Vehiculo(f"Turbo_{i+1}", 80, 0.3))
    for i in range(4):
        flota.append(Vehiculo(f"Moto_{i+1}", 25, 0.08))
    for i in range(8):
        flota.append(Vehiculo(f"Van_{i+1}", 300, 2.5))
    flota.append(Vehiculo("Camion_1", 300, 6.0))
    return flota

def asignar_paquetes(paquetes, flota):
    # Ordenamos de mayor a menor volumen (Heurística First Fit Decreasing)
    paquetes_ordenados = sorted(paquetes, key=lambda p: p["volumen"], reverse=True)
    no_asignados = []
    
    for paquete in paquetes_ordenados:
        asignado = False
        for vehiculo in flota:
            if vehiculo.puede_llevar(paquete):
                vehiculo.asignar(paquete)
                asignado = True
                break
        if not asignado:
            no_asignados.append(paquete)
            
    return no_asignados

if __name__ == "__main__":
    print("=== SISTEMA DE ASIGNACIÓN DE PAQUETES ===")
    paquetes = leer_paquetes("paquetes.csv")
    print(f"Paquetes leídos: {len(paquetes)}")
    
    flota = crear_flota()
    print(f"Vehículos disponibles: {len(flota)}")
    
    no_asignados = asignar_paquetes(paquetes, flota)
    
    print("\n=== RESULTADOS POR VEHÍCULO ===")
    for v in flota:
        if len(v.paquetes) > 0:
            v.mostrar_resumen()
            
    if no_asignados:
        print(f"\nPaquetes NO asignados: {len(no_asignados)}")
        for p in no_asignados:
            print(f"  - {p['id']} ({p['peso']} kg, {p['volumen']:.4f} m3)")
    else:
        print("\nTodos los paquetes fueron asignados.")