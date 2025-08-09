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

TOTAL_PAGES_RAM = RAM_SIZE // PAGE_SIZE
ram_paginas = [None] * TOTAL_PAGES_RAM
memoria_virtual = []
tabela_paginas = {}

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

def desfragmentar():
    print("\n===> Desfragmentando a RAM...")
    novas_paginas = [p for p in ram_paginas if p is not None]
    livres = TOTAL_PAGES_RAM - len(novas_paginas)
    novas_paginas.extend([None] * livres)
    ram_paginas[:] = novas_paginas

    # Atualizar tabela de páginas
    for processo, paginas in tabela_paginas.items():
        tabela_paginas[processo] = [
            (pg, "RAM") if (processo, pg) in ram_paginas else (pg, "DISCO")
            for pg, _ in paginas
        ]

def tentar_realocar_do_disco():
    print("\n===> Tentando realocar páginas do disco...")
    for processo, tamanho in processos.items():
        for pg_index, (pg_num, local) in enumerate(tabela_paginas[processo]):
            if local == "DISCO":
                try:
                    slot_livre = ram_paginas.index(None)
                    ram_paginas[slot_livre] = (processo, pg_num)
                    tabela_paginas[processo][pg_index] = (pg_num, "RAM")
                    memoria_virtual.remove((processo, pg_num))
                    print(f"Página {pg_num} de {processo} movida para RAM.")
                except ValueError:
                    return  # RAM cheia

def print_estado():
    print("\n=== Estado da RAM (por páginas) ===")
    for i, pagina in enumerate(ram_paginas):
        if pagina:
            print(f"Slot {i}: {pagina[0]} - Página {pagina[1]}")
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

desfragmentar()
print_estado()

tentar_realocar_do_disco()
print_estado()
