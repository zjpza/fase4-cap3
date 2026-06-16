# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href= "https://www.fiap.com.br/"><img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Administração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

## Fase 4 — CAP 3
## Classificação de Grãos de Trigo com Machine Learning (Seeds Dataset)

## Nome do grupo

Grupo 5 — Classificação de Grãos de Trigo

## 👨‍🎓 Integrantes: 
- <a href="https://github.com/HenriqueSanchesSilva">Henrique Sanches Silva</a> — RM 570527
- <a href="https://github.com/zjpza">João Pedro Zavanela Andreu</a> — RM 570231
- <a href="https://github.com/Kayckxz">Kayck Gabriel Evangelista da Silva</a> — RM 572331
- <a href="https://github.com/lhboschi">Luis Henrique Laurentino Boschi</a> — RM 571352
- <a href="https://github.com/Trickmelo">Patrick Borges de Melo</a> — RM 574030

## 👩‍🏫 Professores:
### Tutor(a) 
- Sabrina Otoni
### Coordenador(a)
- André Godoi

## 📜 Descrição

Este projeto aplica a metodologia CRISP-DM para desenvolver um modelo de aprendizado de máquina supervisionado capaz de classificar automaticamente variedades de grãos de trigo com base em suas características físicas. O objetivo é substituir a classificação manual — realizada por especialistas em cooperativas agrícolas de pequeno porte — por uma solução automatizada, rápida e precisa.

O conjunto de dados utilizado é o **Seeds Dataset (UCI Machine Learning Repository)**, contendo 210 amostras de grãos de trigo pertencentes a três variedades (Kama, Rosa e Canadian), descritas por sete atributos físicos: área, perímetro, compacidade, comprimento do núcleo, largura do núcleo, coeficiente de assimetria e comprimento do sulco do núcleo.

A solução percorre todo o ciclo de ciência de dados: análise exploratória dos dados, pré-processamento, implementação e comparação de múltiplos algoritmos de classificação (KNN, SVM, Random Forest, Naive Bayes, Regressão Logística), otimização de hiperparâmetros via Grid Search e Randomized Search, e interpretação dos resultados para extração de insights relevantes ao contexto agrícola.

O projeto foi desenvolvido em notebooks Jupyter (.ipynb) com Python, Pandas, Scikit-learn, Matplotlib e Seaborn. Inclui estatísticas descritivas, validação cruzada, Grid Search, Randomized Search, matrizes de confusão, análise estatística entre modelos e relatórios de métricas comparativas.

## 📁 Estrutura de pastas

- <b>.github</b>: arquivos de configuração específicos do GitHub.
- <b>assets</b>: imagens, logos e screenshots dos notebooks.
- <b>config</b>: arquivos de configuração do projeto.
- <b>document</b>: documentos do projeto, incluindo o AI Project Document.
- <b>scripts</b>: scripts auxiliares para tarefas específicas.
- <b>src</b>: código fonte do projeto.
  - <b>src/data</b>: dataset Seeds (raw e processed), scripts de download e pré-processamento.
  - <b>src/notebooks</b>: notebooks Jupyter com EDA, modelos, otimização e interpretação.
  - <b>src/models</b>: modelos de ML serializados (.pkl) gerados pelos notebooks.
- <b>README.md</b>: guia geral do projeto.

## 🔧 Como executar o código

### Pré-requisitos
- Python 3.10+
- pip

### Passo a passo

1. Clone o repositório:
```bash
git clone https://github.com/zjpza/fase4-cap3.git
cd fase4-cap3
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Baixe o dataset Seeds (se ainda não estiver em `src/data/raw/`):
```bash
python src/data/download_seeds.py
```

4. Execute o pré-processamento para gerar os dados de treino e teste:
```bash
python src/data/preprocess.py
```

5. Execute os notebooks na ordem:
```bash
jupyter notebook src/notebooks/
```

> Os notebooks 02 e 03 usam pipelines com escalonamento interno. O script `preprocess.py` apenas persiste a divisão treino/teste padronizada para reprodutibilidade; o escalonamento também é reaplicado dentro dos pipelines.

## 🗃 Histórico de lançamentos

* 1.0.0 - 26/05/2026
    * Fase 4 CAP 3 — Classificação de Grãos de Trigo com ML: EDA, modelos comparativos (KNN, SVM, RF, Naive Bayes, LogReg), otimização de hiperparâmetros via Grid Search e Randomized Search, validação cruzada, teste estatístico e interpretação de resultados.
* 0.1.0 - 15/06/2026
    * Início do projeto e estruturação do repositório.

## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/zjpza/fase4-cap3">FIAP Fase 4 CAP 3 — Classificação de Grãos</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>
