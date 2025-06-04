
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Códigos de Cura", layout="wide")
st.title("Consulta de Códigos de Cura")
st.markdown("Busque por termos nos códigos e descrições da base oficial de Códigos de Cura.")

# Carregar CSV interno
@st.cache_data
def load_data():
    return pd.read_csv("codigos_de_cura_completos.csv")

df = load_data()

# Campo de busca
busca = st.text_input("🔍 Buscar por código ou utilização (termo livre):")

# Resultado da busca
if busca:
    resultados = df[df.apply(lambda row: busca.lower() in row["Código"].lower() or busca.lower() in row["Utilização"].lower(), axis=1)]
else:
    resultados = df

st.write(f"🔎 Resultados encontrados: {len(resultados)}")
st.dataframe(resultados, use_container_width=True)

# Botão para download
csv = resultados.to_csv(index=False).encode("utf-8")
st.download_button("📥 Baixar resultados como CSV", csv, "resultados_filtrados.csv", "text/csv")
