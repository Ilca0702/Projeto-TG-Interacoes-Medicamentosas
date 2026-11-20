# ------------------------------------------------------------
# Projeto: Análise de Interações Medicamentosas
# Disciplina: Teoria dos Grafos
# Parte 3 - Visualização do Grafo
#
# Aluna: Ilca Mária Pereira da Luz
# RA: 10444474
#
# Descrição:
# Este programa gera imagens do grafo de interações
# medicamentosas utilizando as bibliotecas NetworkX
# e Matplotlib.
#
# A primeira imagem apresenta o grafo completo, com
# 80 medicamentos e 220 interações.
#
# A segunda imagem apresenta um subgrafo formado pelos
# medicamentos de identificadores 0, 7 e 79, mostrando
# suas conexões e os respectivos pesos.
#
# As arestas são representadas por cores diferentes
# conforme a gravidade das interações registradas.
#
# Histórico de alterações:
# 18/11/2026 - Ilca Mária Pereira da Luz
# Organização e documentação do código de visualização.
# ------------------------------------------------------------
from pathlib import Path
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D


# Arquivos do projeto
PASTA = Path(__file__).resolve().parent
ARQUIVO = PASTA / "grafo.txt"

# Cores conforme a gravidade
CORES = {
    1: "#39A96B",  # Leve
    2: "#F2B84B",  # Moderada
    3: "#D9534F"   # Grave
}


def carregar_grafo():
    # Le os dados do arquivo
    with open(ARQUIVO, "r", encoding="utf-8-sig") as arquivo:
        linhas = [
            linha.strip()
            for linha in arquivo
            if linha.strip()
        ]

    # Formato esperado:
    # tipo do grafo
    # quantidade de vertices
    # identificador e nome de cada medicamento
    # quantidade de arestas
    # vertice1 vertice2 peso

    pos = 0

    tipo = int(linhas[pos])
    pos += 1

    if tipo != 2:
        raise ValueError("O grafo deve ser nao orientado.")

    n = int(linhas[pos])
    pos += 1

    grafo = nx.Graph()

    # Adiciona os medicamentos
    for _ in range(n):
        partes = linhas[pos].split(maxsplit=1)
        pos += 1

        identificador = int(partes[0])
        nome = partes[1].strip('"') if len(partes) > 1 else str(identificador)

        grafo.add_node(identificador, nome=nome)

    # Quantidade de interacoes
    m = int(linhas[pos])
    pos += 1

    # Adiciona as interacoes e seus pesos
    for _ in range(m):
        v, w, peso = map(int, linhas[pos].split())
        pos += 1

        if v not in grafo or w not in grafo:
            raise ValueError("Interacao com vertice inexistente.")

        if peso not in CORES:
            raise ValueError("Peso de interacao invalido.")

        if grafo.has_edge(v, w):
            raise ValueError("Interacao duplicada.")

        grafo.add_edge(v, w, weight=peso)

    return grafo


def desenhar_arestas(grafo, posicoes):
    # Desenha cada gravidade com uma cor
    for peso, cor in CORES.items():
        arestas = [
            (v, w)
            for v, w, dados in grafo.edges(data=True)
            if dados["weight"] == peso
        ]

        nx.draw_networkx_edges(
            grafo,
            posicoes,
            edgelist=arestas,
            edge_color=cor,
            width=1.5,
            alpha=0.7
        )


def adicionar_legenda():
    itens = [
        Line2D([0], [0], color=CORES[1], lw=3, label="Leve (1)"),
        Line2D([0], [0], color=CORES[2], lw=3, label="Moderada (2)"),
        Line2D([0], [0], color=CORES[3], lw=3, label="Grave (3)")
    ]

    plt.legend(
        handles=itens,
        loc="upper right",
        fontsize=10
    )


def figura_grafo_completo(grafo):
    # Organiza os vertices na imagem
    posicoes = nx.spring_layout(
        grafo,
        seed=42,
        iterations=200
    )

    plt.figure(figsize=(17, 13))

    desenhar_arestas(grafo, posicoes)

    nx.draw_networkx_nodes(
        grafo,
        posicoes,
        node_color="#A9D6E5",
        node_size=400,
        edgecolors="#24536B",
        linewidths=1
    )

    # Mostra os identificadores dos medicamentos
    nx.draw_networkx_labels(
        grafo,
        posicoes,
        font_size=7,
        font_weight="bold"
    )

    plt.title(
        "Grafo de Interacoes Medicamentosas\n"
        "80 medicamentos e 220 interacoes",
        fontsize=16
    )

    adicionar_legenda()
    plt.axis("off")
    plt.tight_layout()

    destino = PASTA / "figura_grafo_completo.png"

    plt.savefig(
        destino,
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()
    print(f"Figura salva: {destino.name}")


def figura_subgrafo(grafo):
    # Medicamentos utilizados no teste
    selecionados = [0, 7, 79]

    for vertice in selecionados:
        if vertice not in grafo:
            raise ValueError(
                f"Medicamento {vertice} nao encontrado."
            )

    subgrafo = grafo.subgraph(selecionados).copy()

    posicoes = {
        0: (0, 1.5),
        7: (-1.5, 0),
        79: (1.5, 0)
    }

    plt.figure(figsize=(11, 7))

    desenhar_arestas(subgrafo, posicoes)

    nx.draw_networkx_nodes(
        subgrafo,
        posicoes,
        node_color="#A9D6E5",
        node_size=3000,
        edgecolors="#24536B",
        linewidths=2
    )

    # Nome dos medicamentos
    nomes = {
        v: f"{v}\n{dados['nome']}"
        for v, dados in subgrafo.nodes(data=True)
    }

    nx.draw_networkx_labels(
        subgrafo,
        posicoes,
        labels=nomes,
        font_size=9,
        font_weight="bold"
    )

    # Mostra o peso das interacoes
    pesos = nx.get_edge_attributes(
        subgrafo,
        "weight"
    )

    nx.draw_networkx_edge_labels(
        subgrafo,
        posicoes,
        edge_labels=pesos,
        font_size=12,
        font_color="#A52A2A"
    )

    plt.title(
        "Subgrafo de Interacoes Medicamentosas\n"
        "Medicamentos 0, 7 e 79",
        fontsize=15
    )

    adicionar_legenda()
    plt.axis("off")
    plt.tight_layout()

    destino = PASTA / "figura_subgrafo_0_7_79.png"

    plt.savefig(
        destino,
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()
    print(f"Figura salva: {destino.name}")


def main():
    try:
        grafo = carregar_grafo()

        print(
            f"Arquivo carregado: "
            f"{grafo.number_of_nodes()} vertices, "
            f"{grafo.number_of_edges()} arestas"
        )

        figura_grafo_completo(grafo)
        figura_subgrafo(grafo)

        print("Figuras geradas com sucesso!")

    except FileNotFoundError:
        print("Erro: arquivo grafo.txt nao encontrado.")

    except (ValueError, IndexError) as erro:
        print(f"Erro ao ler os dados: {erro}")


if __name__ == "__main__":
    main()
