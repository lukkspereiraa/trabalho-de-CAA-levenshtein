def levenshtein_optimized(s1, s2):
    m, n = len(s1), len(s2)
    if m < n:
        s1, s2 = s2, s1
        m, n = n, m  # Garantir que s1 seja a maior string

    previous = list(range(n + 1))  # Armazena a linha anterior
    current = [0] * (n + 1)  # Armazena a linha atual

    for i in range(1, m + 1):
        current[0] = i
        for j in range(1, n + 1):
            cost = 0 if s1[i - 1] == s2[j - 1] else 1
            current[j] = min(
                current[j - 1] + 1,    # Inserção
                previous[j] + 1,       # Remoção
                previous[j - 1] + cost # Substituição
            )
        previous, current = current, previous  # Alterna as linhas
    
    return previous[n]


def sugerir_correcoes_otimizado(palavra, dicionario, limite=2, minimo_sugestoes=5):
    tam_palavra = len(palavra)
    candidatos = [termo for termo in dicionario if abs(len(termo) - tam_palavra) <= limite]
    
    sugestoes = []
    for termo in candidatos:
        dist = levenshtein_optimized(palavra, termo)
        if dist <= limite:
            sugestoes.append((termo, dist))
    
    sugestoes.sort(key=lambda x: x[1])  # Ordena por menor distância
    
    if len(sugestoes) < minimo_sugestoes:
        extras = sorted(
            [(termo, levenshtein_optimized(palavra, termo)) for termo in dicionario], key=lambda x: x[1]
        )
        sugestoes.extend(extras[:minimo_sugestoes - len(sugestoes)])
    
    return [s[0] for s in sugestoes[:minimo_sugestoes]]

# Exemplo de dicionário com 50 palavras
palavras = [
    "facam", "facanha", "facao", "face", "facial", "facil", "facilidade", "facho", "faca", "facaoes",
    "facetas", "fachadas", "faceiras", "faceiros", "facilima", "facilimo", "facilitacao", "facilitado",
    "facilitai", "facilitais", "facilitam", "facilitamos", "facilitando", "facilitante", "facilitantes",
    "facilitava", "facilitavam", "facilitando", "facilitaria", "facilitar", "facilitas", "facilite",
    "facilitou", "facilidade", "facilidades", "facilita", "facilitadora", "facilitadores", "facilitado",
    "facilitou", "fachada", "fachadas", "facho", "fachos", "facanhesco", "facanhesca", "facanhescos",
    "facanhescas", "facaozinho"
]

entrada = "fraca"
print("Sugestões de palavras próximas:", sugerir_correcoes_otimizado(entrada, palavras))
