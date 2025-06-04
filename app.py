
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Códigos de Cura", layout="wide")
st.title("🔮 Consulta de Códigos de Cura")
st.markdown("Consulte códigos canalizados do Arcanjo Rafael e da Mãe Divina. Use palavras-chave ou números para buscar.")

@st.cache_data
def load_data():
    return pd.read_csv("codigos_de_cura_completos.csv", encoding="utf-8")

df = load_data()

# Campo de busca
busca = st.text_input("🔍 Digite um código ou palavra-chave:")

# Resultado da busca com realce
if busca:
    busca_lower = busca.lower()
    resultados = df[df.apply(lambda row: busca_lower in row["Código"].lower() or busca_lower in row["Utilização"].lower(), axis=1)]
    st.markdown(f"**{len(resultados)} resultados encontrados** para: `{busca}`")
else:
    resultados = df
    st.markdown(f"**{len(resultados)} códigos disponíveis**")

# Exibir tabela com largura total
st.dataframe(resultados, use_container_width=True)

# Download
csv = resultados.to_csv(index=False).encode("utf-8")
st.download_button("📥 Baixar resultados filtrados", csv, "resultados_codigos_de_cura.csv", "text/csv")
