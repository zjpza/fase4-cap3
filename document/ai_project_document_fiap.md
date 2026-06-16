
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

1. **Entendimento do negócio**: identificação da necessidade de automação da classificação de grãos em cooperativas de pequeno porte, reduzindo subjetividade e tempo de processo.
2. **Análise e pré-processamento**: estatísticas descritivas, histogramas, boxplots, scatterplots, matriz de correlação, verificação de valores ausentes e padronização com `StandardScaler`.
3. **Modelagem comparativa**: cinco algoritmos (KNN, SVM, Random Forest, Naive Bayes e Regressão Logística) avaliados com validação cruzada de 5 folds estratificados no treino e, após seleção, no conjunto de teste independente.
4. **Otimização**: `GridSearchCV` para KNN e Regressão Logística; `RandomizedSearchCV` para SVM e Random Forest, todos sobre pipelines com escalonamento interno para evitar data leakage.
5. **Interpretação e entrega**: comparação estatística dos modelos, análise de feature importance, matrizes de confusão e consolidação dos achados no AI Project Document.

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

- Dataset: 210 amostras, 3 classes balanceadas (70 amostras cada).
- Divisão: 70% treino (147 amostras) e 30% teste (63 amostras), estratificada, com `random_state=42`.
- Pré-processamento: padronização com `StandardScaler` aplicada **apenas aos dados de treino** e replicada ao teste; os notebooks 02 e 03 usam pipelines com escalonamento interno para evitar data leakage.
- Métricas: acurácia, precisão, recall e F1-score (média ponderada).
- Validação: 5-fold cross-validation estratificada no treino para seleção de modelos; teste reservado para avaliação final.

Resultados de validação cruzada no treino (média ± desvio):

| Modelo | Acurácia CV |
|---|---|
| Logistic Regression | 0.9453 ± 0.0466 |
| SVM | 0.9391 ± 0.0494 |
| Naive Bayes | 0.9320 ± 0.0218 |
| Random Forest | 0.9317 ± 0.0431 |
| KNN | 0.9115 ± 0.0461 |

Resultados no conjunto de teste:

| Modelo | Acurácia Base | Acurácia Otimizada |
|---|---|---|
| Logistic Regression | 0.9048 | 0.9048 |
| SVM | 0.8889 | 0.8889 |
| KNN | 0.8889 | 0.8730 |
| Random Forest | 0.8413 | 0.8413 |
| Naive Bayes | 0.8413 | 0.8413 |

A análise estatística (teste t pareado, 10 folds) entre Logistic Regression e SVM não indicou diferença significativa (p > 0.05), mostrando que ambos são igualmente adequados ao problema.

# <a name="c4"></a>4. Resultados e Avaliações

## 4.1. Análise dos Resultados

A Regressão Logística otimizada alcançou a melhor acurácia no conjunto de teste (0.9048), seguida por SVM (0.8889). Random Forest e Naive Bayes apresentaram desempenho ligeiramente inferior (~0.84), possivelmente porque assumem independência ou sofrem com a alta correlação entre medidas de tamanho (área, perímetro, comprimento do núcleo). A otimização não trouxe melhorias expressivas em relação aos modelos base, indicando que os hiperparâmetros padrão já são adequados para esse dataset pequeno e bem balanceado.

A Random Forest apontou `groove_length` (0.30), `perimeter` (0.20) e `area` (0.20) como as features mais importantes. O comprimento do sulco do núcleo é particularmente relevante porque reflete a morfologia interna do grão, difícil de avaliar visualmente em triagem manual, o que reforça o valor da abordagem automatizada.

A análise de confusão do melhor modelo revela que a maioria dos erros ocorre entre Kama e Canadian, variedades com características morfológicas mais próximas. Em uma implementação real, esses casos fronteiriços devem ser encaminhados para revisão humana.

## 4.2. Limitações

- Dataset pequeno (210 amostras) e de origem única (Polônia), limitando a generalização para variedades brasileiras.
- Ausência de teste com usuários finais ou dados de novas safras.
- Modelo não inclui estimativa de incerteza (probabilidades) na predição, importante para triagem com revisão humana.

## 4.3. Feedback dos Usuários

Não houve teste com usuários finais nesta etapa. A validação foi realizada exclusivamente via métricas estatísticas no conjunto de teste e teste t pareado entre os melhores modelos.

# <a name="c5"></a>5. Conclusões e Trabalhos Futuros

A solução atingiu o objetivo de demonstrar a viabilidade da classificação automatizada de grãos de trigo com aprendizado de máquina. A Regressão Logística otimizada apresentou o melhor desempenho no teste (0.9048), empatada com seu modelo base, enquanto SVM obteve resultado estatisticamente equivalente. Isso indica que o problema pode ser bem modelado por fronteiras de decisão lineares no espaço padronizado, favorecendo modelos simples e interpretáveis.

Pontos fortes:
- Pipeline reproduzível, com versionamento de dependências e notebooks executáveis.
- Uso de validação cruzada no treino e teste independente, minimizando overfitting e data leakage.
- Comparação estatística entre modelos e interpretação de features alinhada aos resultados reais.

Pontos a melhorar:
- Coletar dados de variedades brasileiras e de múltiplas safras para aumentar a generalização.
- Adicionar calibração de probabilidades e threshold de confiança para encaminhar amostras duvidosas à revisão humana.
- Implementar uma API ou interface simples para integração em laboratórios de sementes.
- Realizar testes com usuários finais para validar usabilidade e impacto operacional.

# <a name="c6"></a>6. Referências

- UCI Machine Learning Repository. Seeds Dataset. Disponível em: https://archive.ics.uci.edu/dataset/236/seeds
- Charytanowicz et al. Complete Gradient Clustering Algorithm for Features Analysis of X-Ray Images. Information Technologies in Biomedicine, 2010.
- Scikit-learn documentation. https://scikit-learn.org/stable/
- Python Software Foundation. Python 3.10. https://docs.python.org/3.10/
- Hunter, J. Matplotlib: A 2D graphics environment. Computing in Science & Engineering, 2007.
- Waskom, M. seaborn: statistical data visualization. Journal of Open Source Software, 2021.

# <a name="c7"></a>Anexos

Os notebooks e scripts do projeto estão disponíveis em:

- `src/notebooks/01_exploracao.ipynb`
- `src/notebooks/02_classificacao.ipynb`
- `src/notebooks/03_otimizacao.ipynb`
- `src/notebooks/04_interpretacao.ipynb`
- `src/data/download_seeds.py`
- `src/data/preprocess.py`
