def LPS_DP(S):
    n = len(S)
    if n == 0:
        return 0, ""
    
    # Matriz de DP para longitudes
    dp = [[0]*n for _ in range(n)]
    
    # Toda subcadena de longitud 1 es palíndroma
    for i in range(n):
        dp[i][i] = 1

    # Llenado de la tabla
    for sub_len in range(2, n+1):  # longitud de la subcadena
        for i in range(n - sub_len + 1):
            j = i + sub_len - 1
            
            if S[i] == S[j] and sub_len == 2:
                dp[i][j] = 2
            elif S[i] == S[j]:
                dp[i][j] = dp[i+1][j-1] + 2
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])
    
    # Reconstruir la subsecuencia palindrómica
    lps_length = dp[0][n-1]
    lps = [""] * lps_length  # arreglo para construir la subsecuencia
    
    # punteros para construir la subsecuencia desde ambos extremos
    start = 0
    end = lps_length - 1
    i, j = 0, n - 1
    
    while i <= j:
        # Si los caracteres coinciden
        if S[i] == S[j]:
            # Caso especial: un solo carácter en el centro
            if i == j:
                lps[start] = S[i]
            else:
                lps[start] = S[i]
                lps[end] = S[j]
            start += 1
            end -= 1
            i += 1
            j -= 1
        else:
            # Moverse hacia la dirección que tenga el valor mayor en la DP
            if dp[i+1][j] > dp[i][j-1]:
                i += 1
            else:
                j -= 1
    
    return lps_length, "".join(lps)

def main_dp():
    # Leer cadena desde consola
    S = input("Ingresa la cadena de caracteres: ").strip()
    
    # Calcular la subsecuencia palindrómica más larga (DP)
    length_lps, lps_str = LPS_DP(S)
    print("Subsecuencia Palindrómica Más Larga (DP):", lps_str)
    print("Longitud de la LPS (DP):", length_lps)

if __name__ == "__main__":
    main_dp()
