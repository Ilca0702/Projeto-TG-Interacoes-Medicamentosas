
# Projeto de Teoria dos Grafos — Interações Medicamentosas

**Universidade Presbiteriana Mackenzie**  
**Curso:** Ciência da Computação  
**Disciplina:** Teoria dos Grafos  
**Professor:** Dr. Ivan Carlos Alcântara de Oliveira  
**Autora:** Ilca Mária Pereira da Luz  
**RA:** 10444474

---

## 🎥 VÍDEO DE APRESENTAÇÃO DO PROJETO

### ▶️ [CLIQUE AQUI PARA ASSISTIR À APRESENTAÇÃO NO YOUTUBE](https://www.youtube.com/watch?v=HcQO-a2EdBE)

O vídeo apresenta o problema estudado, a origem e o tratamento dos dados, a modelagem por meio da Teoria dos Grafos, a implementação em Python, a demonstração das funcionalidades, os resultados obtidos e os testes realizados.

---

## 1. Descrição do projeto

Este projeto foi desenvolvido na disciplina de Teoria dos Grafos com o objetivo de representar e analisar interações entre medicamentos utilizando conceitos e algoritmos estudados ao longo do curso.

O problema abordado está relacionado ao uso simultâneo de medicamentos, que pode ocasionar interações com diferentes níveis de gravidade.

Para organizar e analisar essas relações, foi desenvolvido um sistema computacional em Python, utilizando um **grafo não orientado e ponderado**.

Nesse modelo:

- **Vértices:** representam os medicamentos.
- **Arestas:** representam as interações medicamentosas registradas.
- **Pesos:** representam os níveis de gravidade das interações.

A aplicação permite investigar combinações de medicamentos, analisar conexões e aplicar diferentes técnicas da Teoria dos Grafos.

## 2. Origem e organização dos dados

Os dados foram obtidos da **DDInter (Drug-Drug Interaction Database)**, uma base científica de informações sobre interações medicamentosas.

Foi utilizado um arquivo CSV relacionado à categoria *Alimentary Tract and Metabolism* (Trato Alimentar e Metabolismo).

A partir dos registros disponíveis, foi organizado um subconjunto de dados adequado ao escopo acadêmico do projeto.

O conjunto utilizado contém:

| Informação | Quantidade |
|---|---:|
| Medicamentos (vértices) | 80 |
| Interações (arestas) | 220 |
| Interações leves | 18 |
| Interações moderadas | 141 |
| Interações graves | 61 |

As classificações de gravidade foram convertidas em pesos numéricos:

- **Peso 1:** interação leve.
- **Peso 2:** interação moderada.
- **Peso 3:** interação grave.

Os dados estão armazenados no arquivo `grafo.txt`.

A planilha `rastreabilidade_projeto_grafos_parte3.xlsx` permite relacionar os medicamentos e as interações utilizados aos registros da base original.

## 3. Modelagem utilizando Teoria dos Grafos

A rede foi representada por um **grafo simples, não orientado e ponderado**, implementado por meio de listas de adjacências.

A estrutura permite identificar as conexões entre medicamentos e aplicar algoritmos para estudar propriedades do grafo.

Foram utilizados conceitos como:

- Vértices e arestas.
- Grafos ponderados e não orientados.
- Listas de adjacências.
- Graus dos vértices.
- Subgrafos induzidos.
- Conexidade e componentes conexas.
- Coloração de grafos.

## 4. Implementação

A aplicação foi desenvolvida em **Python**, com uma classe própria denominada `Grafo`.

### Funcionalidades básicas

O programa permite:

- Ler e gravar os dados do grafo.
- Inserir e remover vértices.
- Inserir e remover arestas.
- Exibir o conteúdo do arquivo.
- Mostrar as listas de adjacências.
- Verificar a conexidade.
- Validar entradas e tratar erros.

### Funcionalidades desenvolvidas na Parte 3

**1. Análise de combinações de medicamentos**

Permite selecionar medicamentos pelos identificadores e construir o subgrafo induzido, identificando as interações registradas e seus níveis de gravidade.

**2. Análise dos graus dos vértices**

Calcula o número de conexões de cada medicamento e identifica aqueles que possuem mais interações registradas no conjunto analisado.

**3. Coloração de grafos**

Utiliza uma estratégia gulosa baseada no algoritmo Welsh-Powell, considerando os vértices em ordem decrescente de grau.

**4. Identificação de componentes conexas**

Determina os conjuntos de vértices conectados por caminhos, permitindo analisar a conectividade da rede.

## 5. Resultados obtidos

A execução do programa apresentou os seguintes resultados:

| Indicador | Resultado |
|---|---:|
| Total de vértices | 80 |
| Total de arestas | 220 |
| Soma dos graus | 440 |
| Grau médio | 5,5 |
| Componentes conexas | 1 |
| Cores utilizadas na coloração gulosa | 5 |

A rede analisada apresentou uma única componente conexa, formada pelos 80 medicamentos.

A coloração gulosa utilizou cinco cores, respeitando a restrição de atribuir cores diferentes a vértices adjacentes.

Os resultados descrevem as relações registradas no conjunto de dados utilizado e não constituem recomendações clínicas.

## 6. Testes de robustez

O arquivo `testes_robustez_parte3.py` contém **15 testes automatizados**, desenvolvidos para verificar o funcionamento e a consistência da aplicação.

Entre as verificações realizadas estão:

- Leitura de arquivos válidos e inválidos.
- Validação da estrutura dos dados.
- Detecção de arestas duplicadas e laços.
- Identificação de pesos inválidos.
- Tratamento de vértices inexistentes.
- Gravação e releitura dos dados.
- Análise de combinações de medicamentos.
- Cálculo dos graus.
- Validação da coloração.
- Identificação de componentes conexas.
- Consistência após a remoção de vértices.

**Resultado: os 15 testes foram aprovados na execução realizada.**

## 7. Visualização dos grafos

O arquivo `visualizar_grafo.py` utiliza as bibliotecas **NetworkX** e **Matplotlib** para gerar representações visuais dos dados.

As figuras produzidas são:

- `figura_grafo_completo.png`: representa os 80 medicamentos e as 220 interações, com arestas diferenciadas por gravidade.
- `figura_subgrafo_0_7_79.png`: representa o subgrafo induzido pelos medicamentos dexametasona, levofloxacino e ciprofloxacino.

As bibliotecas são utilizadas para visualização, enquanto a estrutura principal do grafo e suas funcionalidades são implementadas na classe própria do projeto.

## 8. Objetivos de Desenvolvimento Sustentável

O projeto está relacionado a dois Objetivos de Desenvolvimento Sustentável (ODS) da Organização das Nações Unidas.

**ODS 3 — Saúde e Bem-Estar**

Relaciona-se ao estudo e à organização de informações sobre interações medicamentosas e seus diferentes níveis de gravidade.

**ODS 9 — Indústria, Inovação e Infraestrutura**

Relaciona-se ao desenvolvimento de uma aplicação computacional que utiliza estruturas de dados e algoritmos para organizar e analisar informações.

## 9. Arquivos do projeto

| Arquivo | Descrição |
|---|---|
| `main_parte3.py` | Programa principal da Parte 3 |
| `testes_robustez_parte3.py` | Testes automatizados |
| `visualizar_grafo.py` | Geração das figuras |
| `grafo.txt` | Dados dos 80 medicamentos e das 220 interações |
| `main.py` | Código da etapa anterior |
| `rastreabilidade_projeto_grafos_parte3.xlsx` | Planilha de rastreabilidade dos dados |
| `projetoTG_parte2_templateRelatorio.pdf` | Relatório da Parte 2 |
| `projetoTG_parte3_templateRelatório.pdf` | Relatório final da Parte 3 |

## 10. Como executar

**Requisito:** Python 3.

Mantenha `main_parte3.py` e `grafo.txt` na mesma pasta.

### Executar o programa principal

```bash
python3 main_parte3.py
```

No menu, selecione a opção `a` para carregar os dados do arquivo antes de realizar as análises.

### Executar os testes automatizados

```bash
python3 testes_robustez_parte3.py
```

### Gerar as representações gráficas

Instale as bibliotecas necessárias:

```bash
python3 -m pip install networkx matplotlib
```

Depois, execute:

```bash
python3 visualizar_grafo.py
```

## 11. Considerações finais

O projeto demonstra a aplicação prática de conceitos da Teoria dos Grafos na organização e análise de uma rede de interações medicamentosas.

A implementação permitiu explorar subgrafos induzidos, graus dos vértices, conectividade, componentes conexas e coloração, além de verificar a consistência do programa por meio de testes automatizados.

O trabalho possui finalidade exclusivamente acadêmica. A ausência de uma interação no conjunto analisado não comprova segurança clínica, e os resultados não substituem avaliações ou orientações de profissionais de saúde.


## Observação

Este projeto tem finalidade acadêmica. As análises não substituem avaliações clínicas ou orientações de profissionais de saúde.
