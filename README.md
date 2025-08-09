# S.O. 2025.1 - Atividade 2.02 - Gestão de memória

## Informações gerais

- **Objetivo do repositório**: Repositório para atividade avaliativa dos alunos
- **Assunto**: Gestão de memória
- **Público alvo**: alunos da disciplina de SO (Sistemas Operacionais) do curso de TADS (Superior em Tecnologia em Análise e Desenvolvimento de Sistemas) no CNAT-IFRN (Instituto Federal de Educação, Ciência e Tecnologia do Rio Grande do Norte - Campus Natal-Central).
- disciplina: **SO** [Sistemas Operacionais](https://github.com/sistemas-operacionais/)
- professor: [Leonardo A. Minora](https://github.com/leonardo-minora)
- Repositótio do aluno: [Rebeca Noemi](https://github.com/becadev)

## Tarefas do aluno
1. Fork desse repositório e atualizar a linha 10 com o nome e link do github
2. Ler a descrição da atividade
3. Montar a resposta no final deste arqivo, no tópico **Resposta**

---

## 1. Descrição da atividade
### 1.1. Objetivo
Praticar os conceitos de alocação de memória (best-fit), memória virtual e desfragmentação em um sistema com memória limitada.

---

### 1.2. Contexto
Um computador possui apenas **64 KB de RAM** e um **disco rígido para memória virtual**. O sistema operacional deve gerenciar 5 processos com tamanhos diferentes, cuja soma ultrapassa a capacidade da RAM.

#### 1.2.1. Processos iniciais

| Processo | Tamanho (KB) |
|----------|-------------|
| P1       | 20          |
| P2       | 15          |
| P3       | 25          |
| P4       | 10          |
| P5       | 18          |
| **Total**| **88 KB**   |

- **Memória RAM**: 64 KB (contígua, inicialmente vazia).  
- **Memória Virtual (Disco)**: Espaço ilimitado para paginação.

#### 1.2.2. Alocação Inicial com Best-Fit
Os alunos devem simular a alocação dos processos na RAM usando o algoritmo **best-fit**.  
- A memória RAM será representada como um bloco contíguo (ex: `[0KB - 64KB]`).  
- Devem alocar os processos nos menores espaços livres que atendam ao seu tamanho.  

**Alocação inicial**:  
1. P1 (20 KB) → Ocupa [0-20].  
2. P2 (15 KB) → Ocupa [20-15].  
3. _continuar a partir daqui_

#### 1.2.3. Simular Memória Virtual (Paginação)
- Os processos não alocados na RAM devem ser "paginados" no disco.  
- Criar uma tabela de páginas indicando quais partes estão na RAM e quais estão no disco.  

#### 1.2.4. Desfragmentação da RAM
- Desfragmentar a RAM para liberar espaço contíguo.
- Após desfragmentação (compactação), verificar quais processos podem ser alocado.  

### 1.3. Questões para Reflexão
1. Best-fit foi mais eficiente que first-fit ou worst-fit neste cenário?  
2. Como a memória virtual evitou um deadlock?  
3. Qual o impacto da desfragmentação no desempenho do sistema?  

---

## Resposta
### 1. Alocação Inicial com Best-Fit


``` shell
simulação de alocação...

✓ P1 alocado na RAM.
✓ P2 alocado na RAM.
✓ P3 alocado na RAM.
✗ P4 enviado para Memória Virtual (não coube na RAM).
✗ P5 enviado para Memória Virtual (não coube na RAM).

=== Estado Atual da RAM ===
  0 -  20 KB: P1
 20 -  35 KB: P2
 35 -  60 KB: P3
 60 -  64 KB: LIVRE

=== Processos na Memória Virtual ===
P4 (10 KB)
P5 (18 KB)
-----------------------------------

===> Desfragmentando a RAM...
✓ RAM desfragmentada.

=== Estado Atual da RAM ===
  0 -  20 KB: P1
 20 -  35 KB: P2
 35 -  60 KB: P3
 60 -  64 KB: LIVRE

=== Processos na Memória Virtual ===
P4 (10 KB)
P5 (18 KB)
-----------------------------------
✗ P4 enviado para Memória Virtual (não coube na RAM).
✗ P5 enviado para Memória Virtual (não coube na RAM).

=== Estado Atual da RAM ===
  0 -  20 KB: P1
 20 -  35 KB: P2
 35 -  60 KB: P3
 60 -  64 KB: LIVRE

=== Processos na Memória Virtual ===
P4 (10 KB)
P5 (18 KB)
```



### 2. Simular Memória Virtual (Paginação)


``` shell
=== Estado da RAM (por páginas) ===
P1 - Página 0 na RAM slot 0
P1 - Página 1 na RAM slot 1
P1 - Página 2 na RAM slot 2
P1 - Página 3 na RAM slot 3
P1 - Página 4 na RAM slot 4
P2 - Página 0 na RAM slot 5
P2 - Página 1 na RAM slot 6
P2 - Página 2 na RAM slot 7
P2 - Página 3 na RAM slot 8
P3 - Página 0 na RAM slot 9
P3 - Página 1 na RAM slot 10
P3 - Página 2 na RAM slot 11
P3 - Página 3 na RAM slot 12
P3 - Página 4 na RAM slot 13
P3 - Página 5 na RAM slot 14
P3 - Página 6 na RAM slot 15

=== Páginas na Memória Virtual ===
P4 - Página 0 no DISCO
P4 - Página 1 no DISCO
P4 - Página 2 no DISCO
P5 - Página 0 no DISCO
P5 - Página 1 no DISCO
P5 - Página 2 no DISCO
P5 - Página 3 no DISCO
P5 - Página 4 no DISCO

=== Tabela de Páginas ===
P1: Pg 0 (RAM), Pg 1 (RAM), Pg 2 (RAM), Pg 3 (RAM), Pg 4 (RAM)
P2: Pg 0 (RAM), Pg 1 (RAM), Pg 2 (RAM), Pg 3 (RAM)
P3: Pg 0 (RAM), Pg 1 (RAM), Pg 2 (RAM), Pg 3 (RAM), Pg 4 (RAM), Pg 5 (RAM), Pg 6 (RAM)
P4: Pg 0 (DISCO), Pg 1 (DISCO), Pg 2 (DISCO)
P5: Pg 0 (DISCO), Pg 1 (DISCO), Pg 2 (DISCO), Pg 3 (DISCO), Pg 4 (DISCO)

```

### 3. Desfragmentação da RAM



``` shell
=== Estado da RAM (por páginas) ===
Slot 0: P1 - Página 0
Slot 1: P1 - Página 1
Slot 2: P1 - Página 2
Slot 3: P1 - Página 3
Slot 4: P1 - Página 4
Slot 5: P2 - Página 0
Slot 6: P2 - Página 1
Slot 7: P2 - Página 2
Slot 8: P2 - Página 3
Slot 9: P3 - Página 0
Slot 10: P3 - Página 1
Slot 11: P3 - Página 2
Slot 12: P3 - Página 3
Slot 13: P3 - Página 4
Slot 14: P3 - Página 5
Slot 15: P3 - Página 6

=== Páginas na Memória Virtual ===
P4 - Página 0 no DISCO
P4 - Página 1 no DISCO
P4 - Página 2 no DISCO
P5 - Página 0 no DISCO
P5 - Página 1 no DISCO
P5 - Página 2 no DISCO
P5 - Página 3 no DISCO
P5 - Página 4 no DISCO

=== Tabela de Páginas ===
P1: Pg 0 (RAM), Pg 1 (RAM), Pg 2 (RAM), Pg 3 (RAM), Pg 4 (RAM)
P2: Pg 0 (RAM), Pg 1 (RAM), Pg 2 (RAM), Pg 3 (RAM)
P3: Pg 0 (RAM), Pg 1 (RAM), Pg 2 (RAM), Pg 3 (RAM), Pg 4 (RAM), Pg 5 (RAM), Pg 6 (RAM)
P4: Pg 0 (DISCO), Pg 1 (DISCO), Pg 2 (DISCO)
P5: Pg 0 (DISCO), Pg 1 (DISCO), Pg 2 (DISCO), Pg 3 (DISCO), Pg 4 (DISCO)

===> Desfragmentando a RAM...

=== Estado da RAM (por páginas) ===
Slot 0: P1 - Página 0
Slot 1: P1 - Página 1
Slot 2: P1 - Página 2
Slot 3: P1 - Página 3
Slot 4: P1 - Página 4
Slot 5: P2 - Página 0
Slot 6: P2 - Página 1
Slot 7: P2 - Página 2
Slot 8: P2 - Página 3
Slot 9: P3 - Página 0
Slot 10: P3 - Página 1
Slot 11: P3 - Página 2
Slot 12: P3 - Página 3
Slot 13: P3 - Página 4
Slot 14: P3 - Página 5
Slot 15: P3 - Página 6

=== Páginas na Memória Virtual ===
P4 - Página 0 no DISCO
P4 - Página 1 no DISCO
P4 - Página 2 no DISCO
P5 - Página 0 no DISCO
P5 - Página 1 no DISCO
P5 - Página 2 no DISCO
P5 - Página 3 no DISCO
P5 - Página 4 no DISCO

=== Tabela de Páginas ===
P1: Pg 0 (RAM), Pg 1 (RAM), Pg 2 (RAM), Pg 3 (RAM), Pg 4 (RAM)
P2: Pg 0 (RAM), Pg 1 (RAM), Pg 2 (RAM), Pg 3 (RAM)
P3: Pg 0 (RAM), Pg 1 (RAM), Pg 2 (RAM), Pg 3 (RAM), Pg 4 (RAM), Pg 5 (RAM), Pg 6 (RAM)
P4: Pg 0 (DISCO), Pg 1 (DISCO), Pg 2 (DISCO)
P5: Pg 0 (DISCO), Pg 1 (DISCO), Pg 2 (DISCO), Pg 3 (DISCO), Pg 4 (DISCO)

===> Tentando realocar páginas do disco...

=== Estado da RAM (por páginas) ===
Slot 0: P1 - Página 0
Slot 1: P1 - Página 1
Slot 2: P1 - Página 2
Slot 3: P1 - Página 3
Slot 4: P1 - Página 4
Slot 5: P2 - Página 0
Slot 6: P2 - Página 1
Slot 7: P2 - Página 2
Slot 8: P2 - Página 3
Slot 9: P3 - Página 0
Slot 10: P3 - Página 1
Slot 11: P3 - Página 2
Slot 12: P3 - Página 3
Slot 13: P3 - Página 4
Slot 14: P3 - Página 5
Slot 15: P3 - Página 6

=== Páginas na Memória Virtual ===
P4 - Página 0 no DISCO
P4 - Página 1 no DISCO
P4 - Página 2 no DISCO
P5 - Página 0 no DISCO
P5 - Página 1 no DISCO
P5 - Página 2 no DISCO
P5 - Página 3 no DISCO
P5 - Página 4 no DISCO

=== Tabela de Páginas ===
P1: Pg 0 (RAM), Pg 1 (RAM), Pg 2 (RAM), Pg 3 (RAM), Pg 4 (RAM)
P2: Pg 0 (RAM), Pg 1 (RAM), Pg 2 (RAM), Pg 3 (RAM)
P3: Pg 0 (RAM), Pg 1 (RAM), Pg 2 (RAM), Pg 3 (RAM), Pg 4 (RAM), Pg 5 (RAM), Pg 6 (RAM)
P4: Pg 0 (DISCO), Pg 1 (DISCO), Pg 2 (DISCO)
P5: Pg 0 (DISCO), Pg 1 (DISCO), Pg 2 (DISCO), Pg 3 (DISCO), Pg 4 (DISCO)

```


### 4. Questões para Reflexão

1. **O Best-fit foi mais eficiente que o First-fit ou o Worst-fit?**  
Nesse caso, o Best-fit apresentou um desempenho parecido com o First-fit, já que a memória RAM começou vazia e os processos foram alocados em ordem sequencial. A principal vantagem do Best-fit, que é diminuir a fragmentação externa, não ficou tão evidente nessa situação.  

2. **Como a memória virtual impediu um deadlock?**  
A memória virtual possibilitou que páginas que não cabiam na RAM fossem armazenadas no disco. Dessa forma, os processos não ficaram travados esperando por espaço na memória principal, evitando assim uma situação de espera circular, que é essencial para ocorrência de deadlocks.  

3. **Qual foi o efeito da desfragmentação no desempenho do sistema?**  
A desfragmentação organizou a memória, liberando blocos contíguos de espaço, o que facilitou a transferência de páginas do disco para a RAM e reduziu os page faults. No entanto, esse processo demandou um alto uso da CPU por um curto período e pode ter causado uma breve interrupção na execução dos processos.