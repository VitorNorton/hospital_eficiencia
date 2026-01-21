# 🏥 Relatório de Eficiência Hospitalar

Este é um projeto em Python desenvolvido para analisar indicadores de desempenho hospitalar, como taxas de mortalidade e ocupação, utilizando bibliotecas de ciência de dados e machine learning para gerar relatórios visuais no terminal e gráficos estatísticos.

## 🚀 Funcionalidades

- **Análise de Dados:** Cálculo automático de Taxa de Mortalidade e Ocupação Hospitalar.
- **Interface no Terminal:** Relatórios formatados e coloridos utilizando a biblioteca `rich`.
- **Visualização de Dados:** Geração de gráficos de dispersão (Leitos vs. Óbitos) e Mapas de Calor de ocupação.
- **Predição:** Modelo de Regressão Linear para prever óbitos com base no número de leitos e atendimentos.

## 🛠️ Tecnologias Utilizadas

- **Python 3**
- **Pandas**: Manipulação e análise de dados.
- **Matplotlib & Seaborn**: Geração de gráficos estatísticos.
- **Scikit-Learn**: Implementação do modelo de regressão linear.
- **Rich**: Formatação avançada de tabelas e painéis no terminal.

## 📦 Como Instalar e Rodar

1.  **Clone o repositório:**

    ```bash
    git clone [https://github.com/seu-usuario/hospital-eficiencia.git](https://github.com/seu-usuario/hospital-eficiencia.git)
    cd hospital-eficiencia
    ```

2.  **Instale as dependências:**

    ```bash
    pip install -r requirements.txt
    ```

3.  **Certifique-se de que o arquivo `hospital_eficiencia.csv` está na pasta.**

4.  **Execute o script:**
    ```bash
    python "Eficiência Hospitalar.py"
    ```

## 📊 Exemplo de Saída

O projeto gera dois arquivos de imagem automaticamente:

1. `grafico_dispersao_hospital.png`
2. `mapa_calor_ocupacao.png`

Além disso, o terminal exibe uma tabela detalhada com os indicadores de cada hospital cadastrado.

## 📝 Estrutura do Projeto

- `Eficiência Hospitalar.py`: Script principal do sistema.
- `hospital_eficiencia.csv`: Base de dados utilizada para a análise.
- `requirements.txt`: Lista de dependências para fácil instalação.
