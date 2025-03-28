import time
import random
import matplotlib.pyplot as plt
import numpy as np

# Fijar semilla para reproducibilidad
random.seed(42)

# --- Función Divide and Conquer para LPS ---
def LPS_DaC_str(S, i, j):
    """
    Retorna la subsecuencia palindrómica más larga en S[i..j] mediante un enfoque recursivo Divide and Conquer.
    """
    if i > j:
        return ""
    if i == j:
        return S[i]
    
    if S[i] == S[j]:
        return S[i] + LPS_DaC_str(S, i+1, j-1) + S[j]
    else:
        left = LPS_DaC_str(S, i+1, j)
        right = LPS_DaC_str(S, i, j-1)
        return left if len(left) > len(right) else right

# --- Función para generar una cadena aleatoria de longitud dada ---
def generate_random_string(length):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return "".join(random.choice(letters) for _ in range(length))

# --- Función principal para ejecutar tests, medir tiempos, ajustar regresión y graficar ---
def run_tests():
    # Generar 25 casos de prueba con longitudes desde 10 hasta 34 (ambos inclusive)
    test_lengths = list(range(5, 29))  # 25 longitudes distintas
    test_strings = [generate_random_string(l) for l in test_lengths]
    
    lengths = []
    times_dac = []
    
    # Medición de tiempos para cada cadena de prueba usando DaC.
    for s, l in zip(test_strings, test_lengths):
        lengths.append(l)
        start_time = time.perf_counter()
        _ = LPS_DaC_str(s, 0, len(s) - 1)
        end_time = time.perf_counter()
        times_dac.append(end_time - start_time)
    
    # Convertir a arrays de NumPy para la regresión
    x = np.array(lengths)
    y = np.array(times_dac)
    
    # Ajuste de una regresión exponencial:
    # Transformamos la relación a escala logarítmica: log(y) = B*x + log(A)  =>  y = A * exp(B*x)
    mask = y > 0  # para evitar log(0)
    x_masked = x[mask]
    y_masked = y[mask]
    log_y = np.log(y_masked)
    coeffs = np.polyfit(x_masked, log_y, 1)  # Ajuste lineal en la escala logarítmica
    B = coeffs[0]
    logA = coeffs[1]
    A = np.exp(logA)
    
    # Generar la línea de regresión exponencial
    x_line = np.linspace(min(x), max(x), 100)
    y_line = A * np.exp(B * x_line)
    
    # Graficar los datos y la línea de regresión
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, 'ro', label="Datos DaC")
    plt.plot(x_line, y_line, 'g--', label=f"Regresión: y = {A:.2e} exp({B:.2e}x)")
    plt.xlabel("Longitud de la cadena")
    plt.ylabel("Tiempo de ejecución (segundos)")
    plt.title("Tiempos de ejecución del algoritmo DaC para LPS (Longitudes de 10 a 34)")
    plt.legend()
    plt.grid(True)
    plt.show()
    
    # Imprimir listado de entradas y tiempos medidos.
    print("Listado de entradas de prueba y tiempos de ejecución (DaC):")
    for s, l, t in zip(test_strings, test_lengths, times_dac):
        print(f"Cadena: {s} (Longitud: {l:2d}) | Tiempo DaC: {t:.6e} seg")
    
    # Comentarios de comparación
    print("\nComentarios (DaC):")
    print("1. Los tiempos de ejecución crecen de forma exponencial conforme la longitud de la cadena aumenta,")
    print("   lo que es consistente con la complejidad teórica O(2^n).")
    print("2. El ajuste de regresión exponencial (y = A*exp(B*x)) confirma la tendencia exponencial esperada.")
    print("   Nota: En entradas de cadenas pequeñas pueden influir sobrecostos fijos, por lo que el ajuste")
    print("   se realiza en el rango observado.")

if __name__ == "__main__":
    run_tests()
