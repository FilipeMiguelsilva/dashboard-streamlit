# dashboard.py
import streamlit as st
import pandas as pd
from datetime import datetime

# ========== CONFIGURAÇÃO ==========
st.set_page_config(
    page_title="Minha Transição Tech",
    page_icon="🚀",
    layout="centered"
)

# ========== CABEÇALHO ==========
st.title("🎯 Minha Jornada para TI")
st.write("De Analista POD para Analista de Dados")
st.write(f"*Data: {datetime.now().strftime('%d/%m/%Y %H:%M')}*")

# ========== SEÇÃO 1: MEU PERFIL ==========
st.header("👤 Meu Perfil Atual")

col1, col2 = st.columns(2)

with col1:
    st.subheader(" Situação Atual")
    st.write("**Cargo:** Analista POD III")
    st.write("**Salário:** R$ -")
    st.write("**Local:** Vinhedo-SP")
    st.write("**Experiência:** Conhecimento em processos industriais")

with col2:
    st.subheader("🎯 Objetivo")
    st.write("**Transição:** Para área de TI")
    st.write("**Salário mínimo:** R$ -")
    st.write("**Prazo:** 6-12 meses")
    st.write("**Estratégia:** Projetos práticos + Experiência atual")

# ========== SEÇÃO 2: MEU PLANO ==========
st.header("📅 Plano de Ação - Próximos 30 Dias")

plano = pd.DataFrame({
    "Semana": ["Esta Semana", "Semana 2", "Semana 3", "Semana 4"],
    "Foco Principal": [
        "Primeiro dashboard em Python",
        "Automação de planilha Excel",
        "Dashboard de eficiência de produção", 
        "LinkedIn + primeiras candidaturas"
    ],
    "Tempo/Dia": ["1h", "1h", "1h", "30min"],
    "Status": ["🟢 Finalizado", "⚪", "⚪", "⚪"]
})


st.dataframe(plano, use_container_width=True, hide_index=True)



# ========== SEÇÃO 3: HABILIDADES ==========
st.header("🛠️ Minhas Habilidades")

habilidades = {
    "Python Básico": 40,
    "Análise de Processos": 80,
    "Streamlit": 30,
    "Conhecimento Industrial": 90,
    "LinkedIn": 50
}

for habilidade, nivel in habilidades.items():
    st.write(f"**{habilidade}**")
    st.progress(nivel/100)

# ========== SEÇÃO 4: PRÓXIMA AÇÃO ==========
st.header("🚀 Próximo Passo Imediato")

acao = st.selectbox(
    "O que vou fazer depois deste dashboard:",
    [
        "Atualizar LinkedIn com este projeto",
        "Estudar Python por 30 minutos",
        "Buscar 3 vagas de Analista de Processos Jr.",
        "Pensar em um projeto de automação para meu trabalho"
    ]
)

if st.button("🏁 Definir como meta"):
    st.success(f"✅ Meta definida: {acao}")
    st.balloons()
    
    # Salvar em arquivo simples
    with open("minha_meta.txt", "w", encoding="utf-8") as f:
        f.write(f"Meta: {acao}\n")
        f.write(f"Data: {datetime.now().strftime('%d/%m/%Y %H:%M')}")
    
    st.info("Meta salva em 'minha_meta.txt' na mesma pasta")

# ========== SEÇÃO 5: VAGAS SUGERIDAS ==========
with st.expander("💼 Vagas que posso buscar em Campinas"):
    st.write("""
    **1. Analista de Processos Jr.**
    - Salário: R$ 4.500 - R$ 5.500
    - Requisitos: Excel, análise de dados, processos industriais
    - Seu diferencial: Já trabalha com isso!
    
    **2. Assistente de TI Industrial**
    - Salário: R$ 4.000 - R$ 5.000
    - Requisitos: Suporte, conhecimento de produção
    - Seu diferencial: Conhece o chão de fábrica
    
    **3. Analista de Dados Jr.**
    - Salário: R$ 4.000 - R$ 6.000
    - Requisitos: Python básico, SQL, análise
    - Seu diferencial: Projetos práticos em Python
    """)

# ========== RODAPÉ ==========
st.divider()
st.caption("Dashboard desenvolvido por [Seu Nome] | Campinas-SP | Último semestre ADS")

# ========== MENSAGEM FINAL ==========
st.success("""
🎉 **PARABÉNS!** Você já tem:
1. ✅ Python instalado
2. ✅ Streamlit funcionando  
3. ✅ Primeiro dashboard criado
4. ✅ Plano de ação definido

**Próximo:** Compartilhar este progresso!
""")
