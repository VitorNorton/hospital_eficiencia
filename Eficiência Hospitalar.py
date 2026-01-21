import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import warnings
warnings.filterwarnings('ignore', category=UserWarning)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

console = Console()

# Leitura dos Dados 
df = pd.read_csv('hospital_eficiencia.csv')

console.print(Panel("[bold cyan]Relatório de Eficiência Hospitalar[/bold cyan]", border_style="green"))

# Cálculos 
console.print(Panel("[bold]Análise[/bold]", border_style="blue"))

df['taxa_mortalidade'] = (df['obitos'] / df['atendimentos']).round(4)
df['ocupacao'] = (df['atendimentos'] / df['leitos']).round(2)

hospital_maior_mortalidade = df.loc[df['taxa_mortalidade'].idxmax()]
hospital_maior_ocupacao = df.loc[df['ocupacao'].idxmax()]

# Tabela 
tabela = Table(title="Indicadores Hospitalares")
tabela.add_column("Hospital", style="cyan")
tabela.add_column("Leitos", justify="right")
tabela.add_column("Atendimentos", justify="right")
tabela.add_column("Óbitos", justify="right")
tabela.add_column("Taxa Mortalidade", style="magenta")
tabela.add_column("Ocupação", style="yellow")

for _, row in df.iterrows():
    tabela.add_row(
        row['hospital'],
        str(row['leitos']),
        str(row['atendimentos']),
        str(row['obitos']),
        f"{row['taxa_mortalidade']*100:.2f}%",
        str(row['ocupacao'])
    )

console.print(tabela)
console.print(Text(f"🏥 Maior taxa de mortalidade: Hospital {hospital_maior_mortalidade['hospital']} ({hospital_maior_mortalidade['taxa_mortalidade']*100:.2f}%)"))
console.print(Text(f"📊 Maior taxa de ocupação: Hospital {hospital_maior_ocupacao['hospital']} ({hospital_maior_ocupacao['ocupacao']} atendimentos/leito)"))

# Graficos 
console.print(Panel("[bold]Visualizações de Dados[/bold]", border_style="blue"))
console.print("📈 Gerando gráficos...")

# Gráfico de dispersão - Leitos vs Óbitos
plt.figure(figsize=(8,5))
sns.scatterplot(x='leitos', y='obitos', data=df, hue='hospital', s=100)
plt.title('Relação entre Leitos e Mortalidade')
plt.xlabel('Número de Leitos')
plt.ylabel('Óbitos Registrados')
plt.grid(True)
plt.savefig('grafico_dispersao_hospital.png')

# Mapa de calor - Ocupação Hospitalar
plt.figure(figsize=(4,3))
sns.heatmap(df[['ocupacao']].set_index(df['hospital']), annot=True, cmap='Reds', cbar=True)
plt.title('Mapa de Calor - Ocupação Hospitalar')
plt.savefig('mapa_calor_ocupacao.png')

# Previsão 
console.print(Panel("[bold]Previsão[/bold]", border_style="blue"))

X = df[['leitos', 'atendimentos']]
y = df['obitos']
modelo = LinearRegression()
modelo.fit(X, y)

novo_hospital = pd.DataFrame([[100, 500]], columns=['leitos', 'atendimentos'])
predicao = modelo.predict(novo_hospital)[0]

console.print(f"🔮 Previsão de óbitos para hospital com 100 leitos e 500 atendimentos: [bold red]{predicao:.1f}[/bold red]")

console.print("\n[bold cyan]✅ Relatório concluído! Gráficos e resultados gerados com sucesso.[/bold cyan]")
