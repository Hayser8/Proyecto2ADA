def LPS_DaC_str(S, i, j):
    """
    Retorna la subsecuencia palindrómica más larga en S[i..j].
    """
    # Caso base: rango inválido
    if i > j:
        return ""
    # Caso base: un solo carácter
    if i == j:
        return S[i]
    
    # Si los caracteres en los extremos coinciden
    if S[i] == S[j]:
        return S[i] + LPS_DaC_str(S, i+1, j-1) + S[j]
    else:
        # Omitir el extremo izquierdo o el derecho
        subseq_left = LPS_DaC_str(S, i+1, j)
        subseq_right = LPS_DaC_str(S, i, j-1)
        # Retornar la subsecuencia más larga
        return subseq_left if len(subseq_left) > len(subseq_right) else subseq_right

def main_dac():
    # Leer cadena desde consola
    S = input("Ingresa la cadena de caracteres: ").strip()
    
    # Calcular la subsecuencia palindrómica más larga (DaC)
    lps = LPS_DaC_str(S, 0, len(S) - 1)
    print("Subsecuencia Palindrómica Más Larga (DaC):", lps)
    print("Longitud de la LPS (DaC):", len(lps))

if __name__ == "__main__":
    main_dac()
