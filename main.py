# Aluna: Ilca Mária Pereira da Luz
# RA: 10444474
# Conteúdo: Implementação do grafo de interações medicamentosas
# utilizando lista de adjacências.
#
# Histórico de alterações:
# 25/09/2026 - Ilca Mária Pereira da Luz - Implementação das
# funcionalidades do projeto.

class Grafo:
    def __init__(self, n=0):
        self.tipo = 2
        self.n = n
        self.m = 0
        self.vertices = {}
        self.listaAdj = [[] for i in range(self.n)]

    # Insere uma aresta na lista de adjacências
    def insereA(self, v, w, peso):
        self.listaAdj[v].append((w, peso))
        self.listaAdj[w].append((v, peso))
        self.m += 1

    # Remove uma aresta da lista de adjacências
    def removeA(self, v, w):
        peso_encontrado = None

        for vizinho, peso in self.listaAdj[v]:
            if vizinho == w:
                peso_encontrado = peso
                break

        if peso_encontrado is None:
            return None

        self.listaAdj[v] = [
            (vizinho, peso)
            for vizinho, peso in self.listaAdj[v]
            if vizinho != w
        ]

        self.listaAdj[w] = [
            (vizinho, peso)
            for vizinho, peso in self.listaAdj[w]
            if vizinho != v
        ]

        self.m -= 1
        return peso_encontrado

    # Opção A - Lê os dados do arquivo grafo.txt
    def ler_arquivo(self, nome_arquivo):
        with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
            self.tipo = int(arquivo.readline().strip())
            quantidade_vertices = int(arquivo.readline().strip())

            self.n = quantidade_vertices
            self.m = 0
            self.vertices = {}
            self.listaAdj = [[] for i in range(self.n)]

            for _ in range(self.n):
                linha = arquivo.readline().strip()
                numero, nome = linha.split(" ", 1)

                numero = int(numero)
                nome = nome.strip('"')

                self.vertices[numero] = nome

            quantidade_arestas = int(arquivo.readline().strip())

            for _ in range(quantidade_arestas):
                linha = arquivo.readline().strip()
                origem, destino, peso = map(int, linha.split())

                self.insereA(origem, destino, peso)

        print("\nArquivo grafo.txt lido com sucesso!")
        print("Quantidade de vértices:", self.n)
        print("Quantidade de arestas:", self.m)

    # Opção B - Grava os dados no arquivo grafo.txt
    def gravar_arquivo(self, nome_arquivo):
        with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
            arquivo.write(f"{self.tipo}\n")
            arquivo.write(f"{self.n}\n")

            for numero in range(self.n):
                arquivo.write(
                    f'{numero} "{self.vertices[numero]}"\n'
                )

            arquivo.write(f"{self.m}\n")

            arestas_gravadas = set()

            for origem in range(self.n):
                for destino, peso in self.listaAdj[origem]:
                    aresta = tuple(sorted((origem, destino)))

                    if aresta not in arestas_gravadas:
                        arquivo.write(
                            f"{origem} {destino} {peso}\n"
                        )
                        arestas_gravadas.add(aresta)

        print("\nDados gravados no arquivo grafo.txt com sucesso!")
        print("Quantidade de vértices:", self.n)
        print("Quantidade de arestas:", self.m)

    # Opção C - Insere um novo vértice no grafo
    def inserir_vertice(self, nome):
        for medicamento in self.vertices.values():
            if medicamento.lower() == nome.lower():
                print("\nEsse medicamento já existe no grafo.")
                return

        novo_numero = self.n

        self.vertices[novo_numero] = nome
        self.listaAdj.append([])
        self.n += 1

        print("\nVértice inserido com sucesso!")
        print("Número do vértice:", novo_numero)
        print("Medicamento:", nome)
        print("Quantidade de vértices:", self.n)

    # Opção D - Insere uma nova aresta no grafo
    def inserir_aresta(self, origem, destino, peso):
        if origem < 0 or origem >= self.n:
            print("\nUm ou ambos os vértices não existem.")
            return

        if destino < 0 or destino >= self.n:
            print("\nUm ou ambos os vértices não existem.")
            return

        if origem == destino:
            print("\nNão é permitido ligar um vértice a ele mesmo.")
            return

        for vizinho, _ in self.listaAdj[origem]:
            if vizinho == destino:
                print("\nJá existe uma interação entre esses medicamentos.")
                return

        self.insereA(origem, destino, peso)

        print("\nAresta inserida com sucesso!")
        print(
            "Medicamentos:",
            self.vertices[origem],
            "<->",
            self.vertices[destino]
        )
        print("Peso da interação:", peso)

        if peso == 1:
            print("Gravidade: Leve")
        elif peso == 2:
            print("Gravidade: Moderada")
        elif peso == 3:
            print("Gravidade: Grave")

    # Opção E - Remove um vértice e suas arestas
    def remover_vertice(self, numero):
        if numero < 0 or numero >= self.n:
            print("\nVértice não encontrado.")
            return

        nome = self.vertices[numero]
        arestas_removidas = len(self.listaAdj[numero])

        for vizinho, _ in list(self.listaAdj[numero]):
            self.removeA(numero, vizinho)

        del self.vertices[numero]
        del self.listaAdj[numero]

        novos_vertices = {}

        for antigo_numero, nome_medicamento in self.vertices.items():
            if antigo_numero < numero:
                novos_vertices[antigo_numero] = nome_medicamento
            else:
                novos_vertices[antigo_numero - 1] = nome_medicamento

        self.vertices = novos_vertices

        for i in range(len(self.listaAdj)):
            nova_lista = []

            for vizinho, peso in self.listaAdj[i]:
                if vizinho > numero:
                    nova_lista.append((vizinho - 1, peso))
                else:
                    nova_lista.append((vizinho, peso))

            self.listaAdj[i] = nova_lista

        self.n -= 1

        print("\nVértice removido com sucesso!")
        print("Número do vértice:", numero)
        print("Medicamento:", nome)
        print("Arestas removidas:", arestas_removidas)
        print("Quantidade de vértices:", self.n)

    # Opção F - Remove uma aresta entre dois vértices
    def remover_aresta(self, origem, destino):
        if origem < 0 or origem >= self.n:
            print("\nUm ou ambos os vértices não existem.")
            return

        if destino < 0 or destino >= self.n:
            print("\nUm ou ambos os vértices não existem.")
            return

        peso = self.removeA(origem, destino)

        if peso is None:
            print("\nNão existe interação entre esses medicamentos.")
            return

        print("\nAresta removida com sucesso!")
        print(
            "Medicamentos:",
            self.vertices[origem],
            "<->",
            self.vertices[destino]
        )
        print("Peso da interação removida:", peso)

    # Opção G - Mostra o conteúdo do arquivo grafo.txt
    def mostrar_arquivo(self, nome_arquivo):
        try:
            with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
                conteudo = arquivo.read()

            print("\nConteúdo do arquivo grafo.txt:")
            print("----------------------------------------------")
            print(conteudo)
            print("----------------------------------------------")

        except FileNotFoundError:
            print("\nArquivo grafo.txt não encontrado.")

    # Opção H - Mostra o grafo usando a lista de adjacências
    def mostrar_grafo(self):
        if self.n == 0:
            print("\nO grafo ainda não foi carregado.")
            return

        print("\nGrafo - Lista de adjacências:")
        print("Quantidade de vértices:", self.n)
        print("Quantidade de arestas:", self.m)
        print("----------------------------------------------")

        for i in range(self.n):
            print(f"\n{i} - {self.vertices[i]}")

            if len(self.listaAdj[i]) == 0:
                print("   Sem interações")
            else:
                for vizinho, peso in self.listaAdj[i]:
                    print(
                        f"   -> {vizinho} - "
                        f"{self.vertices[vizinho]} "
                        f"(peso {peso})"
                    )

        print("----------------------------------------------")

    # Opção I - Verifica se o grafo é conexo ou desconexo
    def verificar_conexidade(self):
        if self.n == 0:
            print("\nO grafo ainda não foi carregado.")
            return

        visitados = set()
        pilha = [0]

        while pilha:
            atual = pilha.pop()

            if atual not in visitados:
                visitados.add(atual)

                for vizinho, _ in self.listaAdj[atual]:
                    if vizinho not in visitados:
                        pilha.append(vizinho)

        print("\nConexidade do grafo:")
        print("----------------------------------------------")
        print("Quantidade de vértices:", self.n)
        print("Vértices alcançados:", len(visitados))

        if len(visitados) == self.n:
            print("Resultado: O grafo é conexo.")
        else:
            print("Resultado: O grafo é desconexo.")

        print("----------------------------------------------")


# Menu da aplicação
def menu():
    print("\n==============================================")
    print("   ANÁLISE DE INTERAÇÕES MEDICAMENTOSAS")
    print("==============================================")
    print("a) Ler dados do arquivo grafo.txt")
    print("b) Gravar dados no arquivo grafo.txt")
    print("c) Inserir vértice")
    print("d) Inserir aresta")
    print("e) Remover vértice")
    print("f) Remover aresta")
    print("g) Mostrar conteúdo do arquivo")
    print("h) Mostrar grafo")
    print("i) Apresentar conexidade do grafo")
    print("j) Encerrar a aplicação")
    print("==============================================")


# Executa o menu e as opções escolhidas
grafo = Grafo()

while True:
    menu()
    opcao = input("\nEscolha uma opção: ").lower()

    # Opção A - Lê os dados do arquivo grafo.txt
    if opcao == "a":
        try:
            grafo.ler_arquivo("grafo.txt")
        except FileNotFoundError:
            print("\nArquivo grafo.txt não encontrado.")

    # Opção B - Grava os dados no arquivo grafo.txt
    elif opcao == "b":
        if grafo.n == 0:
            print("\nPrimeiro carregue o grafo usando a opção A.")
        else:
            grafo.gravar_arquivo("grafo.txt")

    # Opção C - Insere um novo vértice no grafo
    elif opcao == "c":
        if grafo.n == 0:
            print("\nPrimeiro carregue o grafo usando a opção A.")
        else:
            nome = input("Digite o nome do medicamento: ").strip()

            if nome == "":
                print("\nO nome do medicamento não pode ficar vazio.")
            else:
                grafo.inserir_vertice(nome)

    # Opção D - Insere uma nova aresta no grafo
    elif opcao == "d":
        if grafo.n == 0:
            print("\nPrimeiro carregue o grafo usando a opção A.")
        else:
            try:
                origem = int(
                    input("Digite o número do primeiro vértice: ")
                )
                destino = int(
                    input("Digite o número do segundo vértice: ")
                )
                peso = int(
                    input(
                        "Digite a gravidade "
                        "(1 = Leve, 2 = Moderada, 3 = Grave): "
                    )
                )

                if peso not in [1, 2, 3]:
                    print("\nPeso inválido. Utilize somente 1, 2 ou 3.")
                else:
                    grafo.inserir_aresta(origem, destino, peso)

            except ValueError:
                print("\nEntrada inválida. Digite somente números.")

    # Opção E - Remove um vértice e suas arestas
    elif opcao == "e":
        if grafo.n == 0:
            print("\nPrimeiro carregue o grafo usando a opção A.")
        else:
            try:
                numero = int(
                    input(
                        "Digite o número do vértice que deseja remover: "
                    )
                )
                grafo.remover_vertice(numero)

            except ValueError:
                print("\nEntrada inválida. Digite somente números.")

    # Opção F - Remove uma aresta entre dois vértices
    elif opcao == "f":
        if grafo.n == 0:
            print("\nPrimeiro carregue o grafo usando a opção A.")
        else:
            try:
                origem = int(
                    input("Digite o número do primeiro vértice: ")
                )
                destino = int(
                    input("Digite o número do segundo vértice: ")
                )

                grafo.remover_aresta(origem, destino)

            except ValueError:
                print("\nEntrada inválida. Digite somente números.")

    # Opção G - Mostra o conteúdo do arquivo grafo.txt
    elif opcao == "g":
        grafo.mostrar_arquivo("grafo.txt")

    # Opção H - Mostra o grafo usando a lista de adjacências
    elif opcao == "h":
        grafo.mostrar_grafo()

    # Opção I - Verifica se o grafo é conexo ou desconexo
    elif opcao == "i":
        grafo.verificar_conexidade()

    # Opção J - Encerra a aplicação
    elif opcao == "j":
        print("\nAplicação encerrada.")
        break

    else:
        print("\nOpção inválida.")