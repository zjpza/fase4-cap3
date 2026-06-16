
<img src="../assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Administração Paulista" border="0" width=30% height=30%>

# AI Project Document - Fase 4 - CAP 3 - FIAP

## Grupo

- Henrique Sanches Silva — RM 570527
- João Pedro Zavanela Andreu — RM 570231
- Kayck Gabriel Evangelista da Silva — RM 572331
- Luis Henrique Laurentino Boschi — RM 571352
- Patrick Borges de Melo — RM 574030

## Sumário

[1. Introdução](#c1)

[2. Visão Geral do Projeto](#c2)

[3. Desenvolvimento do Projeto](#c3)

[4. Resultados e Avaliações](#c4)

[5. Conclusões e Trabalhos Futuros](#c5)

[6. Referências](#c6)

[Anexos](#c7)

<br>

# <a name="c1"></a>1. Introdução

## 1.1. Escopo do Projeto

### 1.1.1. Contexto da Inteligência Artificial

A Inteligência Artificial aplicada ao agronegócio tem crescido mundialmente, impulsionando soluções de precisão para classificação de grãos, monitoramento de safras e controle de qualidade. Em cooperativas agrícolas de pequeno porte, a classificação de variedades de trigo ainda é realizada manualmente por especialistas, o que torna o processo lento, subjetivo e sujeito a erros humanos. Modelos de aprendizado de máquina supervisionado oferecem alternativa acessível e escalável para automatizar essa tarefa a partir de medições físicas simples dos grãos.

### 1.1.2. Descrição da Solução Desenvolvida

O projeto desenvolve um pipeline de classificação supervisionada para identificar variedades de grãos de trigo (Kama, Rosa e Canadian) a partir de sete atributos geométricos do dataset Seeds (UCI Machine Learning Repository). A solução segue a metodologia CRISP-DM e inclui análise exploratória, pré-processamento, treinamento comparativo de cinco algoritmos, otimização de hiperparâmetros e interpretação dos resultados. Toda a modelagem é reproduzível via notebooks Jupyter.

# <a name="c2"></a>2. Visão Geral do Projeto

## 2.1. Objetivos do Projeto

- Analisar e pré-processar o dataset Seeds para modelagem.
- Implementar e comparar cinco algoritmos de classificação.
- Otimizar os modelos com Grid Search e avaliar melhorias.
- Interpretar os resultados e extrair insights aplicáveis ao contexto agrícola.

## 2.2. Público-Alvo

Cooperativas agrícolas de pequeno porte, técnicos de laboratório de sementes e profissionais de controle de qualidade que precisam classificar grãos de trigo de forma rápida e automatizada.

## 2.3. Metodologia

Foi adotada a metodologia CRISP-DM, dividida em cinco etapas:

1. Análise e pré-processamento: estatísticas descritivas, visualizações, tratamento de ausentes e padronização.
2. Modelagem comparativa: KNN, SVM, Random Forest, Naive Bayes e Regressão Logística.
3. Otimização: Grid Search para ajuste de hiperparâmetros.
4. Interpretação: comparação de desempenho, importância de features e conclusões agrícolas.
5. Entrega: documentação do projeto e revisão dos notebooks.

# <a name="c3"></a>3. Desenvolvimento do Projeto

## 3.1. Tecnologias Utilizadas

- Python 3.10+
- Pandas e NumPy (manipulação de dados)
- Scikit-learn (modelos, métricas e busca de hiperparâmetros)
- Matplotlib e Seaborn (visualização)
- Jupyter Notebook
- Git e GitHub

## 3.2. Modelagem e Algoritmos

Foram escolhidos algoritmos clássicos de classificação supervisionada:

- KNN: simples, interpretável e adequado a datasets pequenos.
- SVM: eficiente em espaços de características de alta dimensionalidade.
- Random Forest: ensemble robusto que fornece importância das features.
- Naive Bayes: baseline rápido e fácil de interpretar.
- Regressão Logística: baseline linear com boa performance multiclasse.

A implementação ocorreu no notebook `02_classificacao.ipynb`. A otimização foi feita no notebook `03_otimizacao.ipynb` com GridSearchCV e validação cruzada de 5 folds.

## 3.3. Treinamento e Teste

- Dataset: 210 amostras, 3 classes balanceadas (70 cada).
- Divisão: 70% treino (147 amostras) e 30% teste (63 amostras), estratificada.
- Pré-processamento: padronização com StandardScaler.
- Métricas: acurácia, precisão, recall e F1-score.

Resultados no conjunto de teste:

| Modelo | Acurácia Base | Acurácia Otimizada |
|---|---|---|
| KNN | 0.8889 | 0.9048 |
| SVM | 0.8889 | 0.8889 |
| Random Forest | 0.8413 | 0.8413 |
| Logistic Regression | 0.9048 | 0.8889 |
| Naive Bayes | 0.8413 | 0.8413 |

# <a name="c4"></a>4. Resultados e Avaliações

## 4.1. Análise dos Resultados

KNN otimizado alcançou a melhor acurácia no teste (0.9048). SVM e LogReg mantiveram desempenho elevado (~0.89). Random Forest e Naive Bayes apresentaram acurácia ligeiramente inferior (~0.84). A otimização não trouxe ganhos expressivos para SVM, RF e NB, sugerindo que os hiperparâmetros padrão já eram adequados ao dataset pequeno e bem comportado. A Random Forest indicou que `area`, `kernel_length` e `perimeter` são as features mais discriminativas.

## 4.2. Feedback dos Usuários

Não houve teste com usuários finais nesta etapa. A validação foi realizada exclusivamente via métricas estatísticas no conjunto de teste.

# <a name="c5"></a>5. Conclusões e Trabalhos Futuros

A solução atingiu o objetivo de demonstrar a viabilidade da classificação automatizada de grãos de trigo com aprendizado de máquina. KNN otimizado mostrou-se a melhor opção de custo-benefício para esse cenário.

Pontos fortes:
- Pipeline reproduzível e bem documentado.
- Alta acurácia com modelos simples.
- Insights claros sobre quais medidas físicas diferenciam as variedades.

Pontos a melhorar:
- Testar o modelo com dados de novas safras e regiões.
- Incluir mais amostras para aumentar a generalização.
- Desenvolver uma interface ou API para uso prático nas cooperativas.

# <a name="c6"></a>6. Referências

- UCI Machine Learning Repository. Seeds Dataset. Disponível em: https://archive.ics.uci.edu/dataset/236/seeds
- Charytanowicz et al. Complete Gradient Clustering Algorithm for Features Analysis of X-Ray Images. Information Technologies in Biomedicine, 2010.
- Scikit-learn documentation. https://scikit-learn.org/stable/

# <a name="c7"></a>Anexos

Os notebooks e scripts do projeto estão disponíveis em:

- `src/notebooks/01_exploracao.ipynb`
- `src/notebooks/02_classificacao.ipynb`
- `src/notebooks/03_otimizacao.ipynb`
- `src/notebooks/04_interpretacao.ipynb`
- `src/data/download_seeds.py`
- `src/data/preprocess.py`
