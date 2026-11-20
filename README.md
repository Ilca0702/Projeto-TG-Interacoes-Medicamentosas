# Projeto de Teoria dos Grafos - Interações Medicamentosas

## Descrição

Projeto desenvolvido na disciplina de Teoria dos Grafos com o objetivo de representar e analisar interações entre medicamentos utilizando conceitos e algoritmos da Teoria dos Grafos.

Os medicamentos são representados por vértices e as interações medicamentosas por arestas. O modelo utiliza um grafo não orientado e ponderado, no qual os pesos indicam os níveis de gravidade das interações registradas.

A aplicação permite analisar a estrutura da rede e investigar as interações existentes entre combinações de medicamentos selecionados.

## Dados

Os dados utilizados foram obtidos a partir da base DDInter (Drug-Drug Interaction Database).

O conjunto analisado contém:

- **80 vértices:** medicamentos.
- **220 arestas:** interações medicamentosas.
- **Peso 1:** interação leve.
- **Peso 2:** interação moderada.
- **Peso 3:** interação grave.

Os dados estão armazenados no arquivo `grafo.txt`.

## Implementação

A aplicação foi desenvolvida em Python, utilizando uma classe `Grafo` e listas de adjacências para representar as conexões entre os medicamentos.

### Funcionalidades básicas

- Leitura e gravação dos dados do grafo.
- Inserção e remoção de vértices.
- Inserção e remoção de arestas.
- Exibição dos dados e das listas de adjacências.
- Verificação da conexidade do grafo.
- Validação de entradas e tratamento de erros.

### Funcionalidades desenvolvidas na Parte 3

**1. Análise de combinações de medicamentos**

Permite selecionar medicamentos por seus identificadores e analisar o subgrafo induzido por eles, identificando as interações registradas e seus níveis de gravidade.

**2. Análise dos graus dos vértices**

Calcula a quantidade de conexões de cada medicamento, permitindo identificar os vértices com maior número de interações registradas.

**3. Coloração de grafos**

Aplica uma estratégia gulosa baseada na ideia do algoritmo Welsh-Powell, utilizando a ordem decrescente dos graus dos vértices.

**4. Identificação de componentes conexas**

Identifica os conjuntos de vértices conectados por caminhos, permitindo analisar a conectividade da rede.

## Resultados

A execução das funcionalidades sobre o conjunto de dados apresentou os seguintes resultados:

- 80 medicamentos e 220 interações.
- Soma dos graus dos vértices: 440.
- Grau médio: 5,5.
- Uma componente conexa formada pelos 80 vértices.
- Coloração gulosa utilizando cinco cores.
- Identificação de interações leves, moderadas e graves entre medicamentos selecionados.

Os resultados descrevem as relações registradas no conjunto de dados utilizado. A ausência de uma interação no grafo não comprova segurança clínica, e a coloração não constitui uma recomendação de uso conjunto de medicamentos.

## Testes automatizados

O arquivo `testes_robustez_parte3.py` contém 15 testes automatizados para verificar:

- Leitura de arquivos válidos e inválidos.
- Validação da estrutura do arquivo.
- Identificação de arestas duplicadas, laços e pesos inválidos.
- Tratamento de vértices inexistentes.
- Gravação e releitura dos dados.
- Análise de combinações de medicamentos.
- Cálculo dos graus dos vértices.
- Validação da coloração.
- Identificação de componentes conexas.
- Consistência após remoção de vértices.

Na execução realizada com o conjunto de dados do projeto, os 15 testes foram aprovados.

## Visualização

O arquivo `visualizar_grafo.py` utiliza as bibliotecas NetworkX e Matplotlib para gerar:

- `figura_grafo_completo.png`: representação dos 80 medicamentos e das 220 interações, com arestas diferenciadas por gravidade.
- `figura_subgrafo_0_7_79.png`: representação do subgrafo induzido pelos medicamentos Dexamethasone, Levofloxacin e Ciprofloxacin.

## Arquivos do projeto

- `main_parte3.py`: programa principal atualizado da Parte 3.
- `testes_robustez_parte3.py`: testes automatizados.
- `visualizar_grafo.py`: geração das representações gráficas.
- `grafo.txt`: conjunto de dados utilizado na aplicação.
- `main.py`: código da etapa anterior do projeto.
- `projetoTG_parte2_templateRelatorio.pdf`: relatório da Parte 2.
- `rastreabilidade_projeto_grafos_parte3.xlsx`: planilha de rastreabilidade dos 80 medicamentos e das 220 interações.
- `projetoTG_parte3_templateRelatório.pdf`: relatório final da Parte 3.
  
## Como executar

**Requisito:** Python 3.

Mantenha `main_parte3.py` e `grafo.txt` na mesma pasta.

Para executar a aplicação principal:

```bash
python main_parte3.py
```

No menu, selecione a opção `a` para carregar os dados antes de executar as análises.

Para executar os testes automatizados:

```bash
python testes_robustez_parte3.py
```

Para gerar as figuras, instale as bibliotecas necessárias:

```bash
python -m pip install networkx matplotlib
```

Depois, execute:

```bash
python visualizar_grafo.py
```

## Autora
# Projeto de Teoria dos Grafos - Interações Medicamentosas

## Descrição

Projeto desenvolvido na disciplina de Teoria dos Grafos com o objetivo de representar e analisar interações entre medicamentos utilizando conceitos e algoritmos da Teoria dos Grafos.

Os medicamentos são representados por vértices e as interações medicamentosas por arestas. O modelo utiliza um **grafo não orientado e ponderado**, no qual os pesos indicam os níveis de gravidade das interações registradas.

A aplicação permite analisar a estrutura da rede e investigar as interações existentes entre combinações de medicamentos selecionados.

## Dados

Os dados utilizados foram obtidos a partir da base DDInter (Drug-Drug Interaction Database).

O conjunto analisado contém:

- **80 vértices:** medicamentos.
- **220 arestas:** interações medicamentosas.
- **Peso 1:** interação leve.
- **Peso 2:** interação moderada.
- **Peso 3:** interação grave.

Os dados estão armazenados no arquivo `grafo.txt`.

## Implementação

A aplicação foi desenvolvida em Python, utilizando uma classe `Grafo` e listas de adjacências para representar as conexões entre os medicamentos.

### Funcionalidades básicas

- Leitura e gravação dos dados do grafo.
- Inserção e remoção de vértices.
- Inserção e remoção de arestas.
- Exibição dos dados e das listas de adjacências.
- Verificação da conexidade do grafo.
- Validação de entradas e tratamento de erros.

### Funcionalidades desenvolvidas na Parte 3

**1. Análise de combinações de medicamentos**

Permite selecionar medicamentos por seus identificadores e analisar o subgrafo induzido por eles, identificando as interações registradas e seus níveis de gravidade.

**2. Análise dos graus dos vértices**

Calcula a quantidade de conexões de cada medicamento, permitindo identificar os vértices com maior número de interações registradas.

**3. Coloração de grafos**

Aplica uma estratégia gulosa baseada na ideia do algoritmo Welsh-Powell, utilizando a ordem decrescente dos graus dos vértices.

**4. Identificação de componentes conexas**

Identifica os conjuntos de vértices conectados por caminhos, permitindo analisar a conectividade da rede.

## Resultados

A execução das funcionalidades sobre o conjunto de dados apresentou os seguintes resultados:

- 80 medicamentos e 220 interações.
- Soma dos graus dos vértices: 440.
- Grau médio: 5,5.
- Uma componente conexa formada pelos 80 vértices.
- Coloração gulosa utilizando cinco cores.
- Identificação de interações leves, moderadas e graves entre medicamentos selecionados.

Os resultados descrevem as relações registradas no conjunto de dados utilizado. A ausência de uma interação no grafo não comprova segurança clínica, e a coloração não constitui uma recomendação de uso conjunto de medicamentos.

## Testes automatizados

O arquivo `testes_robustez_parte3.py` contém 15 testes automatizados para verificar:

- Leitura de arquivos válidos e inválidos.
- Validação da estrutura do arquivo.
- Identificação de arestas duplicadas, laços e pesos inválidos.
- Tratamento de vértices inexistentes.
- Gravação e releitura dos dados.
- Análise de combinações de medicamentos.
- Cálculo dos graus dos vértices.
- Validação da coloração.
- Identificação de componentes conexas.
- Consistência após remoção de vértices.

Na execução realizada com o conjunto de dados do projeto, os 15 testes foram aprovados.

## Visualização

O arquivo `visualizar_grafo.py` utiliza as bibliotecas NetworkX e Matplotlib para gerar:

- `figura_grafo_completo.png`: representação dos 80 medicamentos e das 220 interações, com arestas diferenciadas por gravidade.
- `figura_subgrafo_0_7_79.png`: representação do subgrafo induzido pelos medicamentos Dexamethasone, Levofloxacin e Ciprofloxacin.

## Arquivos do projeto

- `main_parte3.py`: programa principal atualizado da Parte 3.
- `testes_robustez_parte3.py`: testes automatizados.
- `visualizar_grafo.py`: geração das representações gráficas.
- `grafo.txt`: conjunto de dados utilizado na aplicação.
- `main.py`: código da etapa anterior do projeto.
- `projetoTG_parte2_templateRelatorio.pdf`: relatório da Parte 2.

## Como executar

**Requisito:** Python 3.

Mantenha `main_parte3.py` e `grafo.txt` na mesma pasta.

Para executar a aplicação principal:

```bash
python main_parte3.py
```

No menu, selecione a opção `a` para carregar os dados antes de executar as análises.

Para executar os testes automatizados:

```bash
python testes_robustez_parte3.py
```

Para gerar as figuras, instale as bibliotecas necessárias:

```bash
python -m pip install networkx matplotlib
```

Depois, execute:

```bash
python visualizar_grafo.py
```

## Autora

**Ilca Mária Pereira da Luz**  
RA: 10444474

## Observação

Este projeto tem finalidade acadêmica. As análises não substituem avaliações clínicas ou orientações de profissionais de saúde.
