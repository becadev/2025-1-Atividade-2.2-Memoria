RAM_SIZE = 64

processos = {
    "P1": 20,
    "P2": 15,
    "P3": 25,
    "P4": 10,
    "P5": 18
}

# Início com memória 100% livre
memoria_ram = [{"inicio": 0, "fim": RAM_SIZE, "processo": None}]
memoria_virtual = []

def print_estado():
    print("\n=== Estado Atual da RAM ===")
    for bloco in memoria_ram:
        status = bloco['processo'] if bloco['processo'] else "LIVRE"
        print(f"{bloco['inicio']:>3} - {bloco['fim']:>3} KB: {status}")
    print("\n=== Processos na Memória Virtual ===")
    for p in memoria_virtual:
        print(f"{p} ({processos[p]} KB)")
    print("-" * 35)

def best_fit(processo):
    tamanho = processos[processo]
    melhor_espaco = None

    for i, bloco in enumerate(memoria_ram):
        if bloco['processo'] is None:
            espaco_livre = bloco['fim'] - bloco['inicio']
            if espaco_livre >= tamanho:
                if melhor_espaco is None or espaco_livre < (memoria_ram[melhor_espaco]['fim'] - memoria_ram[melhor_espaco]['inicio']):
                    melhor_espaco = i

    if melhor_espaco is not None:
        bloco = memoria_ram[melhor_espaco]
        inicio = bloco['inicio']
        fim = inicio + tamanho
        novo_bloco = {"inicio": inicio, "fim": fim, "processo": processo}
        memoria_ram[melhor_espaco] = {"inicio": fim, "fim": bloco['fim'], "processo": None}
        memoria_ram.insert(melhor_espaco, novo_bloco)
        print(f"✓ {processo} alocado na RAM.")
    else:
        memoria_virtual.append(processo)
        print(f"✗ {processo} enviado para Memória Virtual (não coube na RAM).")

def desfragmentar():
    print("\n===> Desfragmentando a RAM...")
    novos_blocos = []
    posicao = 0

    for bloco in memoria_ram:
        if bloco['processo'] is not None:
            tamanho = bloco['fim'] - bloco['inicio']
            novos_blocos.append({
                "inicio": posicao,
                "fim": posicao + tamanho,
                "processo": bloco['processo']
            })
            posicao += tamanho

    if posicao < RAM_SIZE:
        novos_blocos.append({"inicio": posicao, "fim": RAM_SIZE, "processo": None})

    memoria_ram.clear()
    memoria_ram.extend(novos_blocos)
    print("✓ RAM desfragmentada.")

# -------------------------
# Execução
# -------------------------

print("Iniciando simulação de alocação...\n")

for processo in processos:
    best_fit(processo)

print_estado()

# Desfragmentar e tentar novamente
desfragmentar()
print_estado()

# Tentar alocar os processos que ficaram no disco
na_virtual = memoria_virtual[:]
memoria_virtual.clear()
for processo in na_virtual:
    best_fit(processo)

print_estado()
