
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Códigos de Cura", layout="wide")
st.title("Consulta de Códigos de Cura")
st.markdown("Suba o arquivo CSV ou use a versão de demonstração para buscar códigos e descrições de cura.")

uploaded_file = st.file_uploader("📤 Envie seu CSV (opcional)", type=["csv"])

@st.cache_data
def load_data():
    return pd.read_csv("codigos_de_cura_completos.csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
else:
    df = load_data()

busca = st.text_input("🔍 Buscar por código ou utilização (termo livre):")

if busca:
    resultados = df[df.apply(lambda row: busca.lower() in row["Código"].lower() or busca.lower() in row["Utilização"].lower(), axis=1)]
else:
    resultados = df

st.write(f"🔎 Resultados encontrados: {len(resultados)}")
st.dataframe(resultados, use_container_width=True)

csv = resultados.to_csv(index=False).encode("utf-8")
st.download_button("📥 Baixar resultados como CSV", csv, "resultados_filtrados.csv", "text/csv")
