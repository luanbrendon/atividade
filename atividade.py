import itertools

# Duração de fabricação de cada produto
duracao_producao = {
    'A': 6,
    'B': 4,
    'C': 8,
    'D': 2
}

# Data de entrega de cada produto
data_entrega = {
    'A': 9,
    'B': 12,
    'C': 15,
    'D': 8
}

# Função para calcular o atraso total de uma sequência de produção
def calcular_atraso(sequencia):
    tempo_total = 0
    atraso_total = 0
    
    for produto in sequencia:
        tempo_total += duracao_producao[produto]
        atraso = max(0, tempo_total - data_entrega[produto])
        atraso_total += atraso
        
    return atraso_total

# Função para gerar todos os vizinhos trocando a ordem de dois produtos
def gerar_vizinhos(sequencia):
    vizinhos = []
    for i in range(len(sequencia)):
        for j in range(i+1, len(sequencia)):
            vizinho = list(sequencia)
            vizinho[i], vizinho[j] = vizinho[j], vizinho[i]
            vizinhos.append(tuple(vizinho))
    return vizinhos

# Função para encontrar a melhor solução vizinha
def encontrar_melhor_vizinho(sequencia_atual):
    vizinhos = gerar_vizinhos(sequencia_atual)
    melhor_vizinho = sequencia_atual
    menor_atraso = calcular_atraso(sequencia_atual)
    
    for vizinho in vizinhos:
        atraso_vizinho = calcular_atraso(vizinho)
        if atraso_vizinho < menor_atraso:
            melhor_vizinho = vizinho
            menor_atraso = atraso_vizinho
    
    return melhor_vizinho, menor_atraso

# Solução inicial
solucao_inicial = ('A', 'B', 'C', 'D')

# Iteração 1
print("Iteração 1:")
melhor_vizinho_1, atraso_1 = encontrar_melhor_vizinho(solucao_inicial)
print(f"Melhor vizinho: {melhor_vizinho_1} com {atraso_1} dias de atraso")

# Iteração 2
print("\nIteração 2:")
melhor_vizinho_2, atraso_2 = encontrar_melhor_vizinho(melhor_vizinho_1)
print(f"Melhor vizinho: {melhor_vizinho_2} com {atraso_2} dias de atraso")