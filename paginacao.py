import math

RAM_SIZE = 64  # KB
PAGE_SIZE = 4  # KB

processos = {
    "P1": 20,
    "P2": 15,
    "P3": 25,
    "P4": 10,
    "P5": 18
}

# Quantidade de páginas na RAM
TOTAL_PAGES_RAM = RAM_SIZE // PAGE_SIZE

# Estado inicial da RAM (vazia)
ram_paginas = [None] * TOTAL_PAGES_RAM
memoria_virtual = []  # Páginas no disco

tabela_paginas = {}  # processo -> lista de (número_da_página, local)

def alocar_paginas():
    pagina_atual_ram = 0
    for processo, tamanho in processos.items():
        num_paginas = math.ceil(tamanho / PAGE_SIZE)
        tabela_paginas[processo] = []

        for pagina in range(num_paginas):
            if pagina_atual_ram < TOTAL_PAGES_RAM:
                ram_paginas[pagina_atual_ram] = (processo, pagina)
                tabela_paginas[processo].append((pagina, "RAM"))
                pagina_atual_ram += 1
            else:
                memoria_virtual.append((processo, pagina))
                tabela_paginas[processo].append((pagina, "DISCO"))

def print_estado():
    print("\n=== Estado da RAM (por páginas) ===")
    for i, pagina in enumerate(ram_paginas):
        if pagina:
            print(f"P{pagina[0][-1]} - Página {pagina[1]} na RAM slot {i}")
        else:
            print(f"Slot {i}: LIVRE")

    print("\n=== Páginas na Memória Virtual ===")
    for processo, pagina in memoria_virtual:
        print(f"{processo} - Página {pagina} no DISCO")

    print("\n=== Tabela de Páginas ===")
    for processo, paginas in tabela_paginas.items():
        paginas_str = ", ".join([f"Pg {pg} ({loc})" for pg, loc in paginas])
        print(f"{processo}: {paginas_str}")

# Execução
alocar_paginas()
print_estado()
