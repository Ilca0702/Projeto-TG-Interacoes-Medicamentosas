# ------------------------------------------------------------
# Projeto: Análise de Interações Medicamentosas
# Disciplina: Teoria dos Grafos
# Parte 3 - Programa Principal
#
# Aluna: Ilca Mária Pereira da Luz
# RA: 10444474
#
# Descrição:
# Este programa representa interações medicamentosas por
# meio de um grafo não orientado e ponderado, utilizando
# listas de adjacências. Permite ler, gravar e modificar
# o grafo, além de analisar combinações de medicamentos,
# graus dos vértices, conectividade, componentes conexas
# e coloração gulosa baseada no algoritmo Welsh-Powell.
#
# Histórico de alterações:
# 18/11/2026 - Ilca Mária Pereira da Luz
# Atualização das funcionalidades da Parte 3 e
# organização da documentação do código.
# ------------------------------------------------------------

from collections import Counter
from pathlib import Path

GRAVIDADE = {1: 'Leve', 2: 'Moderada', 3: 'Grave'}
ARQUIVO = Path(__file__).resolve().parent / 'grafo.txt'


class Grafo:
    def __init__(self, n=0):
        self.tipo = 2
        self.n = n
        self.m = 0
        self.vertices = {}
        self.listaAdj = [[] for _ in range(n)]

    def _validar_aresta(self, v, w, peso):
        if not (0 <= v < self.n and 0 <= w < self.n):
            raise ValueError('Um ou ambos os vértices não existem.')
        if v == w:
            raise ValueError('Não é permitido ligar um vértice a ele mesmo.')
        if peso not in GRAVIDADE:
            raise ValueError('Peso inválido. Utilize somente 1, 2 ou 3.')
        if any(vizinho == w for vizinho, _ in self.listaAdj[v]):
            raise ValueError('Já existe uma interação entre esses medicamentos.')

    def insereA(self, v, w, peso):
        self._validar_aresta(v, w, peso)
        self.listaAdj[v].append((w, peso))
        self.listaAdj[w].append((v, peso))
        self.m += 1

    def removeA(self, v, w):
        if not (0 <= v < self.n and 0 <= w < self.n):
            return None
        peso = next((p for viz, p in self.listaAdj[v] if viz == w), None)
        if peso is None:
            return None
        self.listaAdj[v] = [(viz, p) for viz, p in self.listaAdj[v] if viz != w]
        self.listaAdj[w] = [(viz, p) for viz, p in self.listaAdj[w] if viz != v]
        self.m -= 1
        return peso

    def ler_arquivo(self, nome_arquivo):
        # Lê primeiro em um grafo temporário, sem alterar o grafo atual.
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            linhas = [(i, linha.strip()) for i, linha in enumerate(arquivo, 1)
                      if linha.strip()]
        pos = 0

        def proxima():
            nonlocal pos
            if pos >= len(linhas):
                raise ValueError('Arquivo incompleto: faltam linhas.')
            numero_linha, conteudo = linhas[pos]
            pos += 1
            return numero_linha, conteudo

        def inteiro(rotulo):
            numero_linha, conteudo = proxima()
            try:
                return int(conteudo)
            except ValueError as erro:
                raise ValueError(f'Linha {numero_linha}: {rotulo} inválido.') from erro

        tipo = inteiro('tipo do grafo')
        if tipo != 2:
            raise ValueError('O projeto exige grafo não orientado ponderado (tipo 2).')
        n = inteiro('quantidade de vértices')
        if n < 0:
            raise ValueError('A quantidade de vértices não pode ser negativa.')
        temporario = Grafo(n)
        for esperado in range(n):
            numero_linha, conteudo = proxima()
            partes = conteudo.split(' ', 1)
            if len(partes) != 2:
                raise ValueError(f'Linha {numero_linha}: vértice sem identificador e nome.')
            try:
                identificador = int(partes[0])
            except ValueError as erro:
                raise ValueError(f'Linha {numero_linha}: identificador inválido.') from erro
            nome = partes[1].strip()
            if len(nome) < 2 or not (nome.startswith('"') and nome.endswith('"')):
                raise ValueError(f'Linha {numero_linha}: nome deve estar entre aspas.')
            nome = nome[1:-1].strip()
            if identificador != esperado or not nome:
                raise ValueError(f'Linha {numero_linha}: identificador ou nome inválido.')
            if nome.casefold() in (v.casefold() for v in temporario.vertices.values()):
                raise ValueError(f'Linha {numero_linha}: medicamento repetido.')
            temporario.vertices[identificador] = nome
        m = inteiro('quantidade de arestas')
        if m < 0:
            raise ValueError('A quantidade de arestas não pode ser negativa.')
        for _ in range(m):
            numero_linha, conteudo = proxima()
            partes = conteudo.split()
            if len(partes) != 3:
                raise ValueError(f'Linha {numero_linha}: aresta deve ter origem, destino e peso.')
            try:
                v, w, peso = map(int, partes)
                temporario.insereA(v, w, peso)
            except ValueError as erro:
                raise ValueError(f'Linha {numero_linha}: {erro}') from erro
        if pos != len(linhas):
            raise ValueError(f'Linha {linhas[pos][0]}: conteúdo extra após as arestas.')
        self.__dict__.update(temporario.__dict__)
        print(f'\nArquivo lido com sucesso! Vértices: {self.n} | Arestas: {self.m}')

    def arestas(self):
        for v in range(self.n):
            for w, peso in self.listaAdj[v]:
                if v < w:
                    yield v, w, peso

    def gravar_arquivo(self, nome_arquivo):
        arestas = list(self.arestas())
        if len(arestas) != self.m:
            raise ValueError('Inconsistência entre contagem e lista de arestas.')
        destino = Path(nome_arquivo)
        temporario = destino.with_name(destino.name + '.tmp')
        try:
            with open(temporario, 'w', encoding='utf-8') as arquivo:
                arquivo.write(f'{self.tipo}\n{self.n}\n')
                for numero in range(self.n):
                    arquivo.write(f'{numero} "{self.vertices[numero]}"\n')
                arquivo.write(f'{len(arestas)}\n')
                for v, w, peso in arestas:
                    arquivo.write(f'{v} {w} {peso}\n')
            temporario.replace(destino)
        finally:
            if temporario.exists():
                temporario.unlink()
        print(f'\nDados gravados com sucesso! Vértices: {self.n} | Arestas: {self.m}')

    def inserir_vertice(self, nome):
        nome = nome.strip()
        if not nome or '"' in nome or '\n' in nome:
            raise ValueError('Nome inválido para o formato do arquivo.')
        if any(valor.casefold() == nome.casefold() for valor in self.vertices.values()):
            raise ValueError('Esse medicamento já existe no grafo.')
        self.vertices[self.n] = nome
        self.listaAdj.append([])
        self.n += 1
        print(f'\nVértice inserido: {self.n - 1} - {nome}')

    def inserir_aresta(self, origem, destino, peso):
        self.insereA(origem, destino, peso)
        print(f'\nInteração inserida: {self.vertices[origem]} <-> '
              f'{self.vertices[destino]} | {GRAVIDADE[peso]}')

    def remover_vertice(self, numero):
        if not 0 <= numero < self.n:
            raise ValueError('Vértice não encontrado.')
        nome = self.vertices[numero]
        removidas = len(self.listaAdj[numero])
        for vizinho, _ in list(self.listaAdj[numero]):
            self.removeA(numero, vizinho)
        del self.listaAdj[numero]
        self.vertices = {i: self.vertices[antigo] for i, antigo in
                         enumerate(v for v in range(self.n) if v != numero)}
        for i in range(len(self.listaAdj)):
            self.listaAdj[i] = [(viz - (viz > numero), p)
                                for viz, p in self.listaAdj[i]]
        self.n -= 1
        print(f'\nVértice removido: {nome} | Arestas removidas: {removidas}')

    def remover_aresta(self, origem, destino):
        peso = self.removeA(origem, destino)
        if peso is None:
            raise ValueError('Não existe interação entre esses vértices.')
        print(f'\nAresta removida: {self.vertices[origem]} <-> '
              f'{self.vertices[destino]} | Peso {peso}')

    def mostrar_arquivo(self, nome_arquivo):
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            print('\nConteúdo do arquivo:\n' + arquivo.read())

    def mostrar_grafo(self):
        if not self.n:
            print('\nO grafo ainda não foi carregado.')
            return
        print(f'\nLista de adjacências | {self.n} vértices | {self.m} arestas')
        for v in range(self.n):
            print(f'\n{v} - {self.vertices[v]}')
            if not self.listaAdj[v]:
                print('   Sem interações')
            for w, peso in self.listaAdj[v]:
                print(f'   -> {w} - {self.vertices[w]} (peso {peso}: {GRAVIDADE[peso]})')

    def componentes_conexas(self):
        visitados = set()
        componentes = []
        for inicio in range(self.n):
            if inicio in visitados:
                continue
            pilha = [inicio]
            componente = []
            visitados.add(inicio)
            while pilha:
                v = pilha.pop()
                componente.append(v)
                for w, _ in self.listaAdj[v]:
                    if w not in visitados:
                        visitados.add(w)
                        pilha.append(w)
            componentes.append(sorted(componente))
        return componentes

    def verificar_conexidade(self):
        if not self.n:
            print('\nO grafo ainda não foi carregado.')
            return
        componentes = self.componentes_conexas()
        print(f'\nComponentes conexas: {len(componentes)}')
        print('Resultado: grafo conexo.' if len(componentes) == 1
              else 'Resultado: grafo desconexo.')

    def analisar_combinacao(self, selecionados):
        # Subgrafo induzido: analisa todas as interações entre os vértices escolhidos.
        if len(selecionados) < 2 or len(set(selecionados)) != len(selecionados):
            raise ValueError('Informe pelo menos dois vértices distintos.')
        if any(not 0 <= v < self.n for v in selecionados):
            raise ValueError('Há identificadores de vértices inválidos.')
        conjunto = set(selecionados)
        interacoes = [(v, w, p) for v, w, p in self.arestas()
                      if v in conjunto and w in conjunto]
        contagem = Counter(p for _, _, p in interacoes)
        print('\nANÁLISE DA COMBINAÇÃO (subgrafo induzido)')
        print('Medicamentos:', ', '.join(self.vertices[v] for v in selecionados))
        print(f'Interações registradas: {len(interacoes)}')
        for v, w, p in sorted(interacoes, key=lambda item: (-item[2], item[0], item[1])):
            print(f'  {self.vertices[v]} <-> {self.vertices[w]}: {GRAVIDADE[p]} ({p})')
        for peso in (3, 2, 1):
            print(f'{GRAVIDADE[peso]}: {contagem[peso]}')
        print('Maior gravidade registrada:',
              GRAVIDADE[max(contagem)] if contagem else 'nenhuma interação no arquivo')
        print('A ausência de aresta não comprova segurança clínica.')
        return interacoes

    def analisar_graus(self):
        graus = sorted(((len(self.listaAdj[v]), v) for v in range(self.n)), reverse=True)
        print('\nGRAU DOS VÉRTICES (número de interações registradas)')
        for grau, v in graus[:10]:
            print(f'  {v} - {self.vertices[v]}: grau {grau}')
        print(f'Soma dos graus: {sum(g for g, _ in graus)} (2 x {self.m})')
        return graus

    def coloracao(self):
        # Algoritmo guloso Welsh-Powell: ordem decrescente de grau.
        ordem = sorted(range(self.n), key=lambda v: (-len(self.listaAdj[v]), v))
        cores = {}
        for v in ordem:
            usadas = {cores[w] for w, _ in self.listaAdj[v] if w in cores}
            cor = 0
            while cor in usadas:
                cor += 1
            cores[v] = cor
        grupos = {}
        for v, cor in cores.items():
            grupos.setdefault(cor, []).append(v)
        print(f'\nCOLORAÇÃO GULOSA (Welsh-Powell): {len(grupos)} cores utilizadas')
        for cor, membros in sorted(grupos.items()):
            print(f'  Grupo {cor + 1} ({len(membros)}): ' +
                  ', '.join(self.vertices[v] for v in sorted(membros)))
        print('A coloração é heurística: não garante o número mínimo de cores.')
        print('Grupos sem arestas registradas não representam segurança clínica.')
        return cores

    def mostrar_componentes(self):
        componentes = self.componentes_conexas()
        print(f'\nCOMPONENTES CONEXAS: {len(componentes)}')
        for i, comp in enumerate(componentes, 1):
            print(f'  Componente {i} ({len(comp)} vértices): ' +
                  ', '.join(self.vertices[v] for v in comp))
        return componentes


def menu():
    print('\n========== ANÁLISE DE INTERAÇÕES MEDICAMENTOSAS ==========')
    print('a) Ler dados do arquivo grafo.txt')
    print('b) Gravar dados no arquivo grafo.txt')
    print('c) Inserir vértice')
    print('d) Inserir aresta')
    print('e) Remover vértice')
    print('f) Remover aresta')
    print('g) Mostrar conteúdo do arquivo')
    print('h) Mostrar grafo')
    print('i) Apresentar conexidade do grafo')
    print('j) Analisar combinações e identificar interações graves')
    print('k) Analisar graus dos vértices')
    print('l) Aplicar coloração de grafos (Welsh-Powell)')
    print('m) Identificar componentes conexas')
    print('n) Encerrar a aplicação')

def executar():
    grafo = Grafo()
    while True:
        menu()
        opcao = input('\nEscolha uma opção: ').strip().lower()
        if opcao == 'n':
            print('\nAplicação encerrada.')
            break
        try:
            if opcao == 'a':
                grafo.ler_arquivo(ARQUIVO)
            elif opcao == 'g':
                grafo.mostrar_arquivo(ARQUIVO)
            elif opcao in 'bcdefhijklm' and len(opcao) == 1 and grafo.n == 0:
                print('\nPrimeiro carregue o grafo usando a opção A.')
            elif opcao == 'b':
                grafo.gravar_arquivo(ARQUIVO)
            elif opcao == 'c':
                grafo.inserir_vertice(input('Nome do medicamento: '))
            elif opcao == 'd':
                v = int(input('Número do primeiro vértice: '))
                w = int(input('Número do segundo vértice: '))
                p = int(input('Gravidade (1 = Leve, 2 = Moderada, 3 = Grave): '))
                grafo.inserir_aresta(v, w, p)
            elif opcao == 'e':
                grafo.remover_vertice(int(input('Número do vértice: ')))
            elif opcao == 'f':
                v = int(input('Número do primeiro vértice: '))
                w = int(input('Número do segundo vértice: '))
                grafo.remover_aresta(v, w)
            elif opcao == 'h':
                grafo.mostrar_grafo()
            elif opcao == 'i':
                grafo.verificar_conexidade()
            elif opcao == 'j':
                print('Exemplo de entrada: 0,7,79')
                ids = [int(item.strip()) for item in
                       input('IDs dos medicamentos separados por vírgula: ').split(',')]
                grafo.analisar_combinacao(ids)
            elif opcao == 'k':
                grafo.analisar_graus()
            elif opcao == 'l':
                grafo.coloracao()
            elif opcao == 'm':
                grafo.mostrar_componentes()
            else:
                print('\nOpção inválida.')
        except (ValueError, OSError, UnicodeError, KeyError) as erro:
            print(f'\nOperação não realizada: {erro}')
        except EOFError:
            print('\nEntrada encerrada.')
            break


if __name__ == '__main__':
    executar()
