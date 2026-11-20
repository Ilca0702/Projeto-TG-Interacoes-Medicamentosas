# ------------------------------------------------------------
# Projeto: Análise de Interações Medicamentosas
# Disciplina: Teoria dos Grafos
# Parte 3 - Testes de Robustez
#
# Aluna: Ilca Mária Pereira da Luz
# RA: 10444474
#
# Descrição:
# Este programa realiza 15 testes automatizados para
# verificar a leitura, validação e gravação dos dados,
# além das funcionalidades desenvolvidas na Parte 3.
#
# Os testes avaliam o tratamento de arquivos inválidos,
# a análise de combinações de medicamentos, os graus
# dos vértices, a coloração, a conectividade e a remoção
# de vértices.
#
# O objetivo é verificar o comportamento da aplicação
# e a consistência dos dados nos cenários avaliados.
#
# Histórico de alterações:
# 18/11/2026 - Ilca Mária Pereira da Luz
# Organização e documentação do arquivo de testes.
# ------------------------------------------------------------

import importlib.util
from pathlib import Path
from tempfile import TemporaryDirectory

# Localiza os arquivos na mesma pasta deste programa.
PASTA = Path(__file__).resolve().parent

src = PASTA / 'main_parte3.py'
original = PASTA / 'grafo.txt'

# Confere se os arquivos necessarios existem.
if not src.is_file():
    raise FileNotFoundError(
        f'Coloque main_parte3.py na pasta: {PASTA}'
    )

if not original.is_file():
    raise FileNotFoundError(
        f'Coloque grafo.txt na pasta: {PASTA}'
    )

# Carrega a classe Grafo do programa principal.
spec = importlib.util.spec_from_file_location('principal', src)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

# Le o arquivo original sem modificar seu conteudo.
base = original.read_text(encoding='utf-8')
linhas = base.splitlines()

assert linhas[0] == '2', 'O grafo deve ser do tipo 2.'
assert linhas[1] == '80', 'Esperados 80 vertices.'

indice_m = 2 + 80

assert linhas[indice_m] == '220', 'Esperadas 220 arestas.'


def teste(nome, conteudo, deve_falhar=True):
    # Cada teste utiliza um arquivo temporario.
    with TemporaryDirectory() as tmp:
        caminho = Path(tmp) / 'grafo.txt'
        caminho.write_text(conteudo, encoding='utf-8')

        # Carrega o grafo original antes de cada teste.
        g = mod.Grafo()
        g.ler_arquivo(original)

        # Guarda o estado anterior para conferir se houve alteracao.
        antes = (g.n, g.m, list(g.arestas()), dict(g.vertices))

        try:
            g.ler_arquivo(caminho)

        except (ValueError, OSError, UnicodeError) as erro:
            assert deve_falhar, (
                f'{nome}: erro inesperado: {erro}'
            )

            depois = (
                g.n, g.m, list(g.arestas()), dict(g.vertices)
            )

            assert depois == antes, (
                f'{nome}: o grafo foi alterado apos o erro.'
            )

            print(f'OK - {nome}: erro identificado corretamente.')

        else:
            assert not deve_falhar, (
                f'{nome}: arquivo invalido foi aceito.'
            )

            print(f'OK - {nome}: arquivo aceito corretamente.')


print('\nINICIANDO TESTES DE ROBUSTEZ\n')

# Teste 1 - Arquivo correto.
teste('1. Arquivo valido', base, False)

# Teste 2 - Tipo de grafo invalido.
teste(
    '2. Tipo invalido',
    '3\n' + '\n'.join(linhas[1:])
)

# Teste 3 - Quantidade de vertices invalida.
teste(
    '3. Quantidade invalida',
    '2\nabc\n' + '\n'.join(linhas[2:])
)

# Teste 4 - Arquivo incompleto.
teste(
    '4. Arquivo incompleto',
    '\n'.join(linhas[:-1])
)

# Teste 5 - Aresta repetida.
teste(
    '5. Aresta duplicada',
    '\n'.join(
        linhas[:indice_m]
        + ['221']
        + linhas[indice_m + 1:]
        + [linhas[indice_m + 1]]
    )
)

# Teste 6 - Vertice ligado a ele mesmo.
teste(
    '6. Laco',
    '\n'.join(
        linhas[:indice_m + 1]
        + ['0 0 3']
        + linhas[indice_m + 2:]
    )
)

# Teste 7 - Peso diferente de 1, 2 ou 3.
teste(
    '7. Peso invalido',
    '\n'.join(
        linhas[:indice_m + 1]
        + ['0 1 8']
        + linhas[indice_m + 2:]
    )
)

# Teste 8 - Vertice que nao existe.
teste(
    '8. Vertice inexistente',
    '\n'.join(
        linhas[:indice_m + 1]
        + ['0 80 3']
        + linhas[indice_m + 2:]
    )
)

# Teste 9 - Conteudo extra no arquivo.
teste(
    '9. Conteudo extra',
    base + '\ntexto extra\n'
)

# Teste 10 - Gravacao e leitura dos dados.
with TemporaryDirectory() as tmp:
    g = mod.Grafo()
    g.ler_arquivo(original)

    destino = Path(tmp) / 'gravado.txt'
    g.gravar_arquivo(destino)

    g2 = mod.Grafo()
    g2.ler_arquivo(destino)

    assert (
        g.n,
        g.m,
        list(g.arestas()),
        g.vertices
    ) == (
        g2.n,
        g2.m,
        list(g2.arestas()),
        g2.vertices
    )

    print('OK - 10. Gravacao e releitura preservam os dados.')

# Teste 11 - Analise de combinacao de medicamentos.
g = mod.Grafo()
g.ler_arquivo(original)

interacoes = g.analisar_combinacao([0, 7, 79])

assert len(interacoes) == 2
assert all(peso == 3 for _, _, peso in interacoes)

print('OK - 11. Analise da combinacao correta.')


# Teste 12 - Calculo dos graus dos vertices.
graus = g.analisar_graus()

assert sum(grau for grau, _ in graus) == 2 * g.m
assert len(graus) == g.n

print('OK - 12. Graus calculados corretamente.')


# Teste 13 - Coloracao do grafo.
cores = g.coloracao()

assert len(cores) == g.n

for v, w, peso in g.arestas():
    assert cores[v] != cores[w], (
        'Vertices adjacentes receberam a mesma cor.'
    )

print('OK - 13. Coloracao valida.')


# Teste 14 - Componentes conexas.
componentes = g.componentes_conexas()

assert len(componentes) == 1
assert len(componentes[0]) == 80

print('OK - 14. Conectividade correta.')


# Teste 15 - Remocao de vertice.
g.remover_vertice(0)

assert g.n == 79
assert g.m == 141

for v, w, peso in g.arestas():
    assert 0 <= v < g.n
    assert 0 <= w < g.n

assert sum(len(vizinhos) for vizinhos in g.listaAdj) == 2 * g.m

print('OK - 15. Vertice removido sem inconsistencias.')


print('\nTODOS OS 15 TESTES PASSARAM!')

