import streamlit as st
import pandas as pd
import plotly.express as px

# Carrega os dados
df = pd.read_csv("SEEG.csv")

# Ajusta o DataFrame (ajuste conforme seu formato real)
df_transposed = df.set_index('Ano').T.reset_index()
df_transposed.rename(columns={'index': 'Setor'}, inplace=True)

# Título
st.title("Evolução das Emissões de Gases de Efeito Estufa no Brasil")

# Gráfico interativo
fig = px.line(
    df,
    x='Ano',
    y=['Mudança de Uso da Terra e Floresta', 'Agropecuária', 'Energia', 'Resíduos', 'Processos Industriais'],
    labels={'value': 'Emissões (MtCO₂e)', 'variable': 'Setor'},
    title='Emissões por Setor (1990–2023)'
)

st.plotly_chart(fig, use_container_width=True)
