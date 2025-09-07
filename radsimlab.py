import streamlit as st
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time
from datetime import datetime

# Configuração da página
st.set_page_config(
    page_title="RadSimLab Pro",
    page_icon="☢️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personalizado
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #1E88E5;
        text-align: center;
        margin-bottom: 2rem;
    }
    .result-box {
        background-color: #e8f5e9;
        padding: 15px;
        border-radius: 10px;
        margin-top: 15px;
        border-left: 5px solid #4CAF50;
    }
    .warning-box {
        background-color: #ffebee;
        padding: 15px;
        border-radius: 10px;
        margin-top: 15px;
        border-left: 5px solid #F44336;
    }
    .info-box {
        background-color: #e3f2fd;
        padding: 15px;
        border-radius: 10px;
        margin-top: 15px;
        border-left: 5px solid #2196F3;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
    }
</style>
""", unsafe_allow_html=True)

# Título principal
st.markdown('<h1 class="main-header">🔬 RadSimLab Pro – Simulador Radiológico Avançado</h1>', unsafe_allow_html=True)

# Sidebar com informações
with st.sidebar:
    st.title("RadSimLab Pro")
    st.markdown("---")
    st.markdown("### 📊 Navegação")
    
    # Menu de módulos
    modulos = {
        "Datação Radiométrica": "datacao_radiometrica",
        "Blindagem Radiológica": "blindagem",
        "Radioterapia": "radioterapia",
        "Distribuição de Dose": "dose",
        "Aplicações Clínicas": "clinico",
        "Aplicações Ambientais": "ambiental",
        "Efeito Compton": "compton",
        "Produção de Pares": "pares",
        "Exposição Ocupacional": "ocupacional",
        "Cenários Históricos": "historico",
        "Decaimento Radioativo": "decaimento",
        "Modo Explicativo": "explicativo",
        "Quiz Interativo": "quiz",
        "Exportar Dados": "exportar",
        "Comparar Simulações": "comparar"
    }
    
    modulo = st.selectbox("Selecione o módulo", list(modulos.keys()))
    
    st.markdown("---")
    st.markdown("### ℹ️ Sobre")
    st.info("""
    RadSimLab Pro é uma ferramenta educacional para simulações
    em física radiológica. Desenvolvido para estudantes e
    profissionais da área.
    """)

# Funções dos módulos
def modulo_datacao_radiometrica():
    st.header("⏳ Datação Radiométrica")
    metodo = st.radio("Selecione o método:", ["Carbono-14", "Potássio-Argônio", "Urânio-Chumbo", "Rubídio-Estrôncio"], horizontal=True)
    
    if metodo == "Carbono-14":
        modulo_carbono14()
    elif metodo == "Potássio-Argônio":
        modulo_potassio_argonio()
    elif metodo == "Urânio-Chumbo":
        modulo_uranio_chumbo()
    elif metodo == "Rubídio-Estrôncio":
        modulo_rubidio_estroncio()

def modulo_carbono14():
    st.markdown("### 🧪 Datação por Carbono-14")
    
    col1, col2 = st.columns(2)
    
    with col1:
        f = st.slider("Fração atual de C-14", min_value=0.001, max_value=0.999, value=0.5, step=0.001, 
                     help="Razão entre C-14 atual e C-14 inicial")
        l = st.number_input("Constante de decaimento λ (anos⁻¹)", min_value=0.000001, value=0.000121, 
                           format="%.6f", help="Valor padrão: 0.000121 anos⁻¹ (meia-vida de 5730 anos)")
    
    if st.button("🔄 Calcular Datação por C-14", use_container_width=True):
        if f <= 0 or l <= 0:
            st.error("Os valores devem ser positivos!")
            return
            
        with st.spinner("Calculando..."):
            time.sleep(0.5)
            idade = -math.log(f) / l
            
            st.markdown("---")
            st.markdown("### 📊 Resultados")
            st.markdown(f'<div class="result-box"><h4>🧪 Idade estimada: <span style="color:#d32f2f">{idade:,.2f} anos</span></h4></div>', unsafe_allow_html=True)
            
            meia_vida = math.log(2) / l
            st.info(f"Meia-vida utilizada: {meia_vida:,.2f} anos")
            
            st.markdown("**📐 Equação utilizada:** `t = -ln(f) / λ`")
            
            # Gráfico com Matplotlib
            tempos = np.linspace(0, idade * 1.5, 100)
            fracoes = np.exp(-l * tempos)
            
            fig, ax = plt.subplots(figsize=(10, 6))
            ax.plot(tempos, fracoes, 'b-', linewidth=3, label='f(t) = e^(–λt)')
            ax.plot(idade, f, 'ro', markersize=10, label=f'Idade estimada: {idade:.0f} anos')
            ax.set_xlabel("Tempo (anos)")
            ax.set_ylabel("Fração de C-14")
            ax.set_title("Decaimento do Carbono-14")
            ax.legend()
            ax.grid(True)
            
            st.pyplot(fig)
            
            # Tabela de dados
            df = pd.DataFrame({"Tempo (anos)": tempos, "Fração de C-14": fracoes})
            st.dataframe(df.head(10), use_container_width=True)
            
            # Opções de download
            col1, col2 = st.columns(2)
            with col1:
                st.download_button("📥 Baixar CSV", data=df.to_csv(index=False), 
                                  file_name="carbono14.csv", mime="text/csv",
                                  use_container_width=True)
            with col2:
                st.download_button("📥 Baixar TXT", data=df.to_string(index=False), 
                                  file_name="carbono14.txt", mime="text/plain",
                                  use_container_width=True)

def modulo_potassio_argonio():
    st.markdown("### 🔋 Datação por Potássio-Argônio")
    
    col1, col2 = st.columns(2)
    
    with col1:
        R = st.number_input("Razão Ar/K medida", min_value=0.01, value=0.5, step=0.01,
                           help="Razão entre Argônio-40 e Potássio-40")
        l = st.number_input("Constante de decaimento λ (anos⁻¹)", min_value=0.000001, 
                           value=0.000125, format="%.6f",
                           help="Valor padrão: 0.000125 anos⁻¹")
    
    if st.button("🔄 Calcular Datação por K-Ar", use_container_width=True):
        if R <= 0 or l <= 0:
            st.error("Os valores devem ser positivos!")
            return
            
        idade = (1 / l) * math.log(1 + R)
        
        st.markdown("---")
        st.markdown("### 📊 Resultados")
        st.markdown(f'<div class="result-box"><h4>🔋 Idade estimada: <span style="color:#d32f2f">{idade:,.2f} anos</span></h4></div>', unsafe_allow_html=True)
        st.markdown("**📐 Equação utilizada:** `t = (1 / λ) · ln(1 + R)`")
        
        # Gráfico
        tempos = np.linspace(0, idade * 1.5, 100)
        razoes = np.exp(l * tempos) - 1
        
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(tempos, razoes, 'g-', linewidth=3, label='R(t) = e^(λt) – 1')
        ax.plot(idade, R, 'ro', markersize=10, label=f'Idade estimada: {idade:.0f} anos')
        ax.set_xlabel("Tempo (anos)")
        ax.set_ylabel("Razão Ar/K")
        ax.set_title("Acúmulo de Argônio-40")
        ax.legend()
        ax.grid(True)
        
        st.pyplot(fig)
        
        # Tabela de dados
        df = pd.DataFrame({"Tempo (anos)": tempos, "Razão Ar/K": razoes})
        st.download_button("📥 Baixar CSV", data=df.to_csv(index=False), 
                          file_name="potassio_argonio.csv", mime="text/csv",
                          use_container_width=True)

def modulo_uranio_chumbo():
    st.markdown("### ☢️ Datação por Urânio-Chumbo")
    
    col1, col2 = st.columns(2)
    
    with col1:
        R = st.number_input("Razão Pb/U medida", min_value=0.01, value=0.5, step=0.01,
                           help="Razão entre Chumbo-206 e Urânio-238")
        l = st.number_input("Constante de decaimento λ (anos⁻¹)", min_value=0.000001, 
                           value=0.000155, format="%.6f",
                           help="Valor padrão: 0.000155 anos⁻¹")
    
    if st.button("🔄 Calcular Datação por U-Pb", use_container_width=True):
        if R <= 0 or l <= 0:
            st.error("Os valores devem ser positivos!")
            return
            
        idade = (1 / l) * math.log(R + 1)
        
        st.markdown("---")
        st.markdown("### 📊 Resultados")
        st.markdown(f'<div class="result-box"><h4>☢️ Idade estimada: <span style="color:#d32f2f">{idade:,.2f} anos</span></h4></div>', unsafe_allow_html=True)
        st.markdown("**📐 Equação utilizada:** `t = (1 / λ) · ln(R + 1)`")
        
        # Gráfico
        tempos = np.linspace(0, idade * 1.5, 100)
        razoes = np.exp(l * tempos) - 1
        
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(tempos, razoes, 'orange', linewidth=3, label='R(t) = e^(λt) – 1')
        ax.plot(idade, R, 'ro', markersize=10, label=f'Idade estimada: {idade:.0f} anos')
        ax.set_xlabel("Tempo (anos)")
        ax.set_ylabel("Razão Pb/U")
        ax.set_title("Acúmulo de Chumbo-206")
        ax.legend()
        ax.grid(True)
        
        st.pyplot(fig)
        
        # Tabela de dados
        df = pd.DataFrame({"Tempo (anos)": tempos, "Razão Pb/U": razoes})
        st.download_button("📥 Baixar CSV", data=df.to_csv(index=False), 
                          file_name="uranio_chumbo.csv", mime="text/csv",
                          use_container_width=True)

def modulo_rubidio_estroncio():
    st.markdown("### 🔬 Datação por Rubídio-Estrôncio")
    
    col1, col2 = st.columns(2)
    
    with col1:
        R = st.number_input("Razão Sr/Rb medida", min_value=0.01, value=0.1, step=0.01,
                           help="Razão entre Estrôncio-87 e Rubídio-87")
        l = st.number_input("Constante de decaimento λ (anos⁻¹)", min_value=0.000001, 
                           value=0.0000142, format="%.8f",
                           help="Valor padrão: 1.42 × 10⁻⁵ anos⁻¹")
    
    if st.button("🔄 Calcular Datação por Rb-Sr", use_container_width=True):
        if R <= 0 or l <= 0:
            st.error("Os valores devem ser positivos!")
            return
            
        idade = (1 / l) * math.log(1 + R)
        
        st.markdown("---")
        st.markdown("### 📊 Resultados")
        st.markdown(f'<div class="result-box"><h4>🔬 Idade estimada: <span style="color:#d32f2f">{idade:,.2f} anos</span></h4></div>', unsafe_allow_html=True)
        st.markdown("**📐 Equação utilizada:** `t = (1 / λ) · ln(1 + R)`")
        
        # Gráfico
        tempos = np.linspace(0, idade * 1.5, 100)
        razoes = np.exp(l * tempos) - 1
        
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(tempos, razoes, 'purple', linewidth=3, label='R(t) = e^(λt) – 1')
        ax.plot(idade, R, 'ro', markersize=10, label=f'Idade estimada: {idade:.0f} anos')
        ax.set_xlabel("Tempo (anos)")
        ax.set_ylabel("Razão Sr/Rb")
        ax.set_title("Acúmulo de Estrôncio-87")
        ax.legend()
        ax.grid(True)
        
        st.pyplot(fig)
        
        # Tabela de dados
        df = pd.DataFrame({"Tempo (anos)": tempos, "Razão Sr/Rb": razoes})
        st.download_button("📥 Baixar CSV", data=df.to_csv(index=False), 
                          file_name="rubidio_estroncio.csv", mime="text/csv",
                          use_container_width=True)

def modulo_blindagem():
    st.header("🧱 Cálculo de Blindagem Radiológica")
    
    materials = {
        "Chumbo": 0.77,
        "Concreto": 0.15,
        "Água": 0.07,
        "Aço": 0.43,
        "Tungstênio": 1.20,
        "Urânio": 1.50
    }
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        material = st.selectbox("Material", options=list(materials.keys()))
        mu = materials[material]
        st.info(f"Coeficiente de atenuação (μ): {mu} cm⁻¹")
        
    with col2:
        I0 = st.number_input("Dose inicial (µSv/h)", min_value=0.01, value=100.0, step=10.0)
        
    with col3:
        I = st.number_input("Dose desejada (µSv/h)", min_value=0.01, value=10.0, step=1.0)
    
    if st.button("🧱 Calcular Blindagem", use_container_width=True):
        if I0 <= 0 or I <= 0 or mu <= 0:
            st.error("Os valores devem ser positivos!")
            return
            
        if I >= I0:
            st.error("A dose desejada deve ser menor que a dose inicial!")
            return
            
        x = (1 / mu) * math.log(I0 / I)
        
        st.markdown("---")
        st.markdown("### 📊 Resultados")
        st.markdown(f'<div class="result-box"><h4>🧱 Espessura mínima de {material}: <span style="color:#d32f2f">{x:.2f} cm</span></h4></div>', unsafe_allow_html=True)
        st.markdown("**📐 Equação utilizada:** `x = (1 / μ) · ln(I₀ / I)`")
        
        # Gráfico com Matplotlib
        espessuras = np.linspace(0, x * 1.5, 100)
        doses = I0 * np.exp(-mu * espessuras)
        
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(espessuras, doses, 'b-', linewidth=3, label=f'Dose com blindagem de {material}')
        ax.plot(x, I, 'ro', markersize=10, label='Espessura mínima')
        ax.axhline(y=I, color='r', linestyle='--', label='Dose desejada')
        ax.set_xlabel("Espessura (cm)")
        ax.set_ylabel("Dose (µSv/h)")
        ax.set_title(f"Atenuação da dose com blindagem de {material}")
        ax.legend()
        ax.grid(True)
        
        st.pyplot(fig)
        
        # Comparação entre materiais
        st.markdown("### 📊 Comparação entre Materiais")
        comparacao = []
        for mat, coef in materials.items():
            esp = (1 / coef) * math.log(I0 / I) if I0 > I else 0
            comparacao.append({"Material": mat, "Coeficiente (cm⁻¹)": coef, "Espessura (cm)": esp})
        
        df_comp = pd.DataFrame(comparacao)
        st.dataframe(df_comp, use_container_width=True)
        
        # Resultado para download
        resultado = f"Material: {material}\nDose inicial: {I0} µSv/h\nDose desejada: {I} µSv/h\nμ: {mu} cm⁻¹\nEspessura mínima: {x:.2f} cm"
        st.download_button("📥 Baixar resultado (.txt)", data=resultado, 
                          file_name="blindagem.txt", mime="text/plain",
                          use_container_width=True)

def modulo_radioterapia():
    st.header("📅 Planejamento Radioterápico")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        D = st.number_input("Dose prescrita (Gy)", min_value=0.1, value=60.0, step=5.0)
    
    with col2:
        R = st.number_input("Taxa de dose (Gy/min)", min_value=0.01, value=2.0, step=0.1)
    
    with col3:
        N = st.number_input("Número de sessões", min_value=1, value=30, step=1)
    
    if st.button("💉 Calcular Radioterapia", use_container_width=True):
        if D <= 0 or R <= 0 or N <= 0:
            st.error("Os valores devem ser positivos!")
            return
            
        dps = D / N
        tps = dps / R
        
        st.markdown("---")
        st.markdown("### 📊 Resultados")
        st.markdown(f'<div class="result-box"><h4>💉 Dose por sessão: <span style="color:#d32f2f">{dps:.2f} Gy</span></h4></div>', unsafe_allow_html=True)
        st.markdown(f'<div class="info-box"><h4>⏱️ Tempo por sessão: <span style="color:#1976D2">{tps:.2f} min</span></h4></div>', unsafe_allow_html=True)
        
        # Gráfico da distribuição de sessões
        sessoes = list(range(1, N+1))
        doses_sessoes = [dps] * N
        
        fig, ax = plt.subplots(figsize=(10, 4))
        ax.bar(sessoes, doses_sessoes, color='skyblue', edgecolor='navy')
        ax.set_xlabel("Sessão")
        ax.set_ylabel("Dose (Gy)")
        ax.set_title("Distribuição de Dose por Sessão")
        ax.grid(True, axis='y')
        
        st.pyplot(fig)
        
        # Resultado para download
        resultado = f"Dose total: {D} Gy\nTaxa de dose: {R} Gy/min\nSessões: {N}\nDose por sessão: {dps:.2f} Gy\nTempo por sessão: {tps:.2f} min"
        st.download_button("📥 Baixar plano (.txt)", data=resultado, 
                          file_name="radioterapia.txt", mime="text/plain",
                          use_container_width=True)

def modulo_dose():
    st.header("📊 Distribuição de Dose em Tecido")
    
    col1, col2 = st.columns(2)
    
    with col1:
        D0 = st.number_input("Dose na superfície (Gy)", min_value=0.1, value=10.0, step=1.0)
        mu = st.number_input("Coef. de atenuação (cm⁻¹)", min_value=0.01, value=0.2, step=0.01)
    
    with col2:
        max_depth = st.number_input("Profundidade máxima (cm)", min_value=1, value=10, step=1)
        pontos = st.slider("Número de pontos", min_value=10, max_value=100, value=50)
    
    if st.button("📊 Calcular Distribuição", use_container_width=True):
        if D0 <= 0 or mu <= 0 or max_depth <= 0:
            st.error("Os valores devem ser positivos!")
            return
            
        profundidades = np.linspace(0, max_depth, pontos)
        doses = [D0 * math.exp(-mu * x) for x in profundidades]
        
        st.markdown("---")
        st.markdown("### 📊 Resultados")
        
        # Tabela de valores
        df = pd.DataFrame({"Profundidade (cm)": profundidades, "Dose (Gy)": doses})
        st.dataframe(df, use_container_width=True)
        
        st.markdown("**📐 Equação:** `D(x) = D₀ · e^(–μx)`")
        
        # Gráfico
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(profundidades, doses, 'purple', marker='o', linewidth=2, markersize=4)
        ax.set_xlabel("Profundidade (cm)")
        ax.set_ylabel("Dose (Gy)")
        ax.set_title("Distribuição de Dose em Tecido")
        ax.grid(True)
        
        st.pyplot(fig)
        
        # Opções de download
        col1, col2 = st.columns(2)
        with col1:
            st.download_button("📥 Baixar CSV", data=df.to_csv(index=False), 
                              file_name="distribuicao_dose.csv", mime="text/csv",
                              use_container_width=True)
        with col2:
            st.download_button("📥 Baixar TXT", data=df.to_string(index=False), 
                              file_name="distribuicao_dose.txt", mime="text/plain",
                              use_container_width=True)

def modulo_clinico():
    st.header("🧬 Distribuição de Tc-99m em Órgãos")
    
    col1, col2 = st.columns(2)
    
    with col1:
        D = st.number_input("Dose administrada (MBq)", min_value=0.1, value=100.0, step=10.0)
        F = st.slider("Fração fixa (%)", min_value=0.1, max_value=100.0, value=20.0, step=0.1)
    
    with col2:
        H = st.number_input("Meia-vida (h)", min_value=0.1, value=6.0, step=0.1)
        T = st.number_input("Tempo após administração (h)", min_value=0.0, value=2.0, step=0.1)
    
    if st.button("🧬 Calcular Tc-99m", use_container_width=True):
        if D <= 0 or F <= 0 or H <= 0 or T < 0:
            st.error("Os valores devem ser positivos!")
            return
            
        lambda_ = math.log(2) / H
        A = D * (F / 100) * math.exp(-lambda_ * T)
        
        st.markdown("---")
        st.markdown("### 📊 Resultados")
        st.markdown(f'<div class="result-box"><h4>🧬 Atividade no órgão: <span style="color:#d32f2f">{A:.2f} MBq</span></h4></div>', unsafe_allow_html=True)
        st.markdown("**📐 Equação:** `A = D · F · e^(–λt)`")
        
        # Gráfico
        tempos = np.linspace(0, H * 3, 100)
        atividades = D * (F / 100) * np.exp(-lambda_ * tempos)
        
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(tempos, atividades, 'green', linewidth=3, label='A(t) = D · F · e^(–λt)')
        ax.axvline(T, color='red', linestyle='--', label=f'Tempo atual: {T:.1f} h')
        ax.set_xlabel("Tempo (h)")
        ax.set_ylabel("Atividade (MBq)")
        ax.set_title("Decaimento de Tc-99m no órgão")
        ax.legend()
        ax.grid(True)
        
        st.pyplot(fig)
        
        # Tabela de dados
        df = pd.DataFrame({"Tempo (h)": tempos, "Atividade (MBq)": atividades})
        st.download_button("📥 Baixar CSV", data=df.to_csv(index=False), 
                          file_name="tc99m.csv", mime="text/csv",
                          use_container_width=True)

def modulo_ambiental():
    st.header("🌱 Exposição Ambiental à Radiação")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Solo")
        taxa_solo = st.number_input("Taxa no solo (µSv/h)", min_value=0.0, value=1.0, step=0.1)
        tempo_solo = st.number_input("Tempo no solo (h)", min_value=0.0, value=5.0, step=0.5)
    
    with col2:
        st.subheader("Ar")
        taxa_ar = st.number_input("Taxa no ar (µSv/h)", min_value=0.0, value=0.5, step=0.1)
        tempo_ar = st.number_input("Tempo no ar (h)", min_value=0.0, value=3.0, step=0.5)
    
    if st.button("🌱 Calcular Exposição Ambiental", use_container_width=True):
        if taxa_solo < 0 or tempo_solo < 0 or taxa_ar < 0 or tempo_ar < 0:
            st.error("Os valores não podem ser negativos!")
            return
            
        dose_solo = taxa_solo * tempo_solo
        dose_ar = taxa_ar * tempo_ar
        total = dose_solo + dose_ar
        
        st.markdown("---")
        st.markdown("### 📊 Resultados")
        st.markdown(f'<div class="result-box"><h4>🌱 Dose no solo: <span style="color:#d32f2f">{dose_solo:.2f} µSv</span></h4></div>', unsafe_allow_html=True)
        st.markdown(f'<div class="info-box"><h4>🌬️ Dose no ar: <span style="color:#1976D2">{dose_ar:.2f} µSv</span></h4></div>', unsafe_allow_html=True)
        st.markdown(f'<div class="result-box"><h4>📊 Dose total: <span style="color:#d32f2f">{total:.2f} µSv</span></h4></div>', unsafe_allow_html=True)
        
        # Gráfico de barras
        categorias = ['Solo', 'Ar', 'Total']
        valores = [dose_solo, dose_ar, total]
        cores = ['#4CAF50', '#2196F3', '#FF9800']
        
        fig, ax = plt.subplots(figsize=(8, 5))
        bars = ax.bar(categorias, valores, color=cores, edgecolor='black')
        ax.set_ylabel("Dose (µSv)")
        ax.set_title("Exposição Ambiental à Radiação")
        
        # Adicionar valores nas barras
        for bar, valor in zip(bars, valores):
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height + max(valores)*0.01,
                    f'{valor:.2f}', ha='center', va='bottom')
        
        st.pyplot(fig)
        
        # Resultado para download
        resultado = f"Dose solo: {dose_solo:.2f} µSv\nDose ar: {dose_ar:.2f} µSv\nTotal: {total:.2f} µSv"
        st.download_button("📥 Baixar resultado (.txt)", data=resultado, 
                          file_name="ambiental.txt", mime="text/plain",
                          use_container_width=True)

def modulo_compton():
    st.header("🔄 Espalhamento Compton")
    
    col1, col2 = st.columns(2)
    
    with col1:
        E = st.number_input("Energia do fóton (MeV)", min_value=0.01, value=1.0, step=0.1)
    
    with col2:
        angulo = st.slider("Ângulo de espalhamento (°)", min_value=0.0, max_value=180.0, value=90.0, step=1.0)
    
    if st.button("🔄 Calcular Compton", use_container_width=True):
        if E <= 0:
            st.error("A energia deve ser positiva!")
            return
            
        mec2 = 0.511
        theta_rad = math.radians(angulo)
        Efinal = E / (1 + (E / mec2) * (1 - math.cos(theta_rad)))
        transferida = E - Efinal
        
        st.markdown("---")
        st.markdown("### 📊 Resultados")
        st.markdown(f'<div class="result-box"><h4>🔄 Energia espalhada: <span style="color:#d32f2f">{Efinal:.3f} MeV</span></h4></div>', unsafe_allow_html=True)
        st.markdown(f'<div class="info-box"><h4>⚡ Energia transferida: <span style="color:#1976D2">{transferida:.3f} MeV</span></h4></div>', unsafe_allow_html=True)
        st.markdown("**📐 Equação:** `E' = E / [1 + (E / 0.511)(1 – cosθ)]`")
        
        # Gráfico da variação com o ângulo
        angulos = np.linspace(0, 180, 100)
        theta_rads = np.radians(angulos)
        E_finals = E / (1 + (E / mec2) * (1 - np.cos(theta_rads)))
        
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(angulos, E_finals, 'blue', linewidth=3)
        ax.axvline(angulo, color='red', linestyle='--', label=f'Ângulo selecionado: {angulo}°')
        ax.set_xlabel("Ângulo de espalhamento (°)")
        ax.set_ylabel("Energia espalhada (MeV)")
        ax.set_title("Variação da Energia Espalhada com o Ângulo")
        ax.legend()
        ax.grid(True)
        
        st.pyplot(fig)
        
        # Resultado para download
        resultado = f"Energia inicial: {E} MeV\nÂngulo: {angulo}°\nEnergia espalhada: {Efinal:.3f} MeV\nEnergia transferida: {transferida:.3f} MeV"
        st.download_button("📥 Baixar resultado (.txt)", data=resultado, 
                          file_name="compton.txt", mime="text/plain",
                          use_container_width=True)

def modulo_pares():
    st.header("⚡ Produção de Pares")
    
    E = st.number_input("Energia do fóton (MeV)", min_value=0.0, value=2.0, step=0.1)
    
    if st.button("⚡ Calcular Pares", use_container_width=True):
        if E <= 0:
            st.error("A energia deve ser positiva!")
            return
            
        if E <= 1.022:
            st.markdown("---")
            st.markdown("### ❌ Resultado")
            st.markdown('<div class="warning-box"><h4>❌ Energia insuficiente para produção de pares</h4></div>', unsafe_allow_html=True)
            st.markdown("**📐 Limite mínimo:** `E > 1.022 MeV`")
        else:
            Ecin = E - 1.022
            
            st.markdown("---")
            st.markdown("### 📊 Resultados")
            st.markdown(f'<div class="result-box"><h4>⚡ Energia cinética total: <span style="color:#d32f2f">{Ecin:.3f} MeV</span></h4></div>', unsafe_allow_html=True)
            st.markdown("**📐 Equação:** `Eₖ = E – 1.022`")
            
            # Gráfico de energia
            componentes = ['Energia do fóton', 'Energia de repouso (2mₑc²)', 'Energia cinética']
            valores = [E, 1.022, Ecin]
            cores = ['#2196F3', '#F44336', '#4CAF50']
            
            fig, ax = plt.subplots(figsize=(8, 5))
            bars = ax.bar(componentes, valores, color=cores, edgecolor='black')
            ax.set_ylabel("Energia (MeV)")
            ax.set_title("Distribuição de Energia na Produção de Pares")
            
            # Adicionar valores nas barras
            for bar, valor in zip(bars, valores):
                height = bar.get_height()
                ax.text(bar.get_x() + bar.get_width()/2., height + max(valores)*0.01,
                        f'{valor:.3f}', ha='center', va='bottom')
            
            st.pyplot(fig)
            
            # Resultado para download
            resultado = f"Energia do fóton: {E} MeV\nEnergia cinética total: {Ecin:.3f} MeV"
            st.download_button("📥 Baixar resultado (.txt)", data=resultado, 
                              file_name="pares.txt", mime="text/plain",
                              use_container_width=True)

def modulo_ocupacional():
    st.header("🧑‍⚕️ Exposição Ocupacional")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        taxa = st.number_input("Taxa diária (µSv/dia)", min_value=0.0, value=5.0, step=0.5)
    
    with col2:
        dias = st.number_input("Dias por ano", min_value=1, value=250, step=5)
    
    with col3:
        fator = st.slider("Fator de proteção (0-100%)", min_value=0.0, max_value=100.0, value=20.0, step=1.0)
    
    if st.button("🧑‍⚕️ Calcular Ocupacional", use_container_width=True):
        if taxa < 0 or dias < 0 or fator < 0:
            st.error("Os valores não podem ser negativos!")
            return
            
        dose = taxa * dias * (1 - fator/100)
        
        st.markdown("---")
        st.markdown("### 📊 Resultados")
        st.markdown(f'<div class="result-box"><h4>🧑‍⚕️ Dose anual estimada: <span style="color:#d32f2f">{dose:.2f} µSv</span></h4></div>', unsafe_allow_html=True)
        
        # Comparação com limites anuais
        limite_publico = 1000  # µSv/ano
        limite_trabalhador = 20000  # µSv/ano
        
        st.markdown("### 📋 Comparação com Limites Anuais")
        col1, col2 = st.columns(2)
        
        with col1:
            percentual_publico = (dose / limite_publico) * 100
            st.metric("Limite para público", f"{limite_publico} µSv", f"{percentual_publico:.1f}%")
        
        with col2:
            percentual_trabalhador = (dose / limite_trabalhador) * 100
            st.metric("Limite para trabalhadores", f"{limite_trabalhador} µSv", f"{percentual_trabalhador:.1f}%")
        
        # Resultado para download
        resultado = f"Taxa diária: {taxa} µSv\nDias/ano: {dias}\nFator proteção: {fator}%\nDose anual: {dose:.2f} µSv\n% do limite público: {percentual_publico:.1f}%\n% do limite trabalhador: {percentual_trabalhador:.1f}%"
        st.download_button("📥 Baixar resultado (.txt)", data=resultado, 
                          file_name="ocupacional.txt", mime="text/plain",
                          use_container_width=True)

def modulo_historico():
    st.header("🕰️ Cenários Históricos")
    
    evento = st.selectbox("Escolha o evento", ["Chernobyl", "Goiânia", "Fukushima", "Three Mile Island"])
    
    dados = {
        "Chernobyl": {
            "ano": "1986",
            "descricao": "Liberação de 5.2 milhões de curies. Zona de exclusão de 30 km.",
            "dose": "Até 20.000 mSv para liquidadores",
            "impacto": "Evacuação de 116.000 pessoas, aumento de câncer de tireoide"
        },
        "Goiânia": {
            "ano": "1987",
            "descricao": "Acidente com Césio-137. 249 contaminados, 4 mortes.",
            "dose": "Até 7 Gy em alguns casos",
            "impacto": "Maior acidente radiológico do mundo fora de usinas nucleares"
        },
        "Fukushima": {
            "ano": "2011",
            "descricao": "Vazamento após tsunami. Evacuação em massa.",
            "dose": "Até 678 mSv para trabalhadores",
            "impacto": "Evacuação de 154.000 pessoas, impacto na pesca local"
        },
        "Three Mile Island": {
            "ano": "1979",
            "descricao": "Fusão parcial do núcleo do reator. Pequena liberação de gases nobres.",
            "dose": "Média de 0.01 mSv para população",
            "impacto": "Mudanças significativas na regulamentação nuclear"
        }
    }
    
    st.markdown("---")
    st.markdown(f"### {evento} ({dados[evento]['ano']})")
    st.markdown(f"**Descrição:** {dados[evento]['descricao']}")
    st.markdown(f"**Doses estimadas:** {dados[evento]['dose']}")
    st.markdown(f"**Impacto:** {dados[evento]['impacto']}")
    
    # Adicionar uma imagem relacionada (apenas para os eventos mais conhecidos)
    if evento == "Chernobyl":
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/5/5a/Chernobyl_NPP_Site_2019-6278.jpg/800px-Chernobyl_NPP_Site_2019-6278.jpg", 
                 caption="Usina Nuclear de Chernobyl em 2019", use_column_width=True)
    elif evento == "Fukushima":
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/8/8e/Fukushima_I_NPP_photo_2011.03.16_02.jpg/800px-Fukushima_I_NPP_photo_2011.03.16_02.jpg", 
                 caption="Usina Nuclear de Fukushima após o tsunami", use_column_width=True)

def modulo_decaimento():
    st.header("📉 Simulação de Decaimento Radioativo")
    
    col1, col2 = st.columns(2)
    
    with col1:
        N0 = st.number_input("Quantidade inicial (Bq)", min_value=1.0, value=1000.0, step=100.0)
        meia_vida = st.number_input("Meia-vida (anos)", min_value=0.01, value=5730.0, step=100.0)
    
    with col2:
        tempo = st.number_input("Tempo decorrido (anos)", min_value=0.0, value=10000.0, step=100.0)
        pontos = st.slider("Número de pontos no gráfico", min_value=10, max_value=200, value=100)
    
    if st.button("📉 Calcular Decaimento", use_container_width=True):
        if N0 <= 0 or meia_vida <= 0 or tempo < 0:
            st.error("Os valores devem ser positivos!")
            return
            
        lambda_val = math.log(2) / meia_vida
        N = N0 * math.exp(-lambda_val * tempo)
        fração_restante = N / N0
        
        st.markdown("---")
        st.markdown("### 📊 Resultados")
        st.markdown(f'<div class="result-box"><h4>📉 Quantidade restante: <span style="color:#d32f2f">{N:,.2f} Bq</span></h4></div>', unsafe_allow_html=True)
        st.markdown(f'<div class="info-box"><h4>📊 Fração restante: <span style="color:#1976D2">{fração_restante:.4f}</span></h4></div>', unsafe_allow_html=True)
        st.markdown("**📐 Equação:** `N = N₀ · e^(-λt)`")
        
        # Gráfico
        tempos = np.linspace(0, meia_vida * 5, pontos)
        quantidades = N0 * np.exp(-lambda_val * tempos)
        
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(tempos, quantidades, 'red', linewidth=3, label='N(t) = N₀ · e^(-λt)')
        ax.plot(tempo, N, 'bo', markersize=10, label=f'Valor no tempo especificado: {N:.2f} Bq')
        
        # Adicionar linhas de meia-vida
        for i in range(1, 6):
            t_meia_vida = meia_vida * i
            n_meia_vida = N0 * (0.5 ** i)
            ax.axvline(x=t_meia_vida, color='green', linestyle='--', alpha=0.7)
            ax.axhline(y=n_meia_vida, color='green', linestyle='--', alpha=0.7)
            ax.text(t_meia_vida, N0*1.05, f'{i}T½', ha='center', va='bottom', color='green')
        
        ax.set_xlabel("Tempo (anos)")
        ax.set_ylabel("Quantidade (Bq)")
        ax.set_title("Decaimento Radioativo")
        ax.legend()
        ax.grid(True)
        
        st.pyplot(fig)
        
        # Tabela de dados
        df = pd.DataFrame({"Tempo (anos)": tempos, "Quantidade (Bq)": quantidades})
        st.download_button("📥 Baixar CSV", data=df.to_csv(index=False), 
                          file_name="decaimento.csv", mime="text/csv",
                          use_container_width=True)

def modulo_explicativo():
    st.header("📘 Modo Explicativo")
    
    tema = st.selectbox("Escolha o tema", ["Carbono-14", "Blindagem", "Compton", "Produção de Pares", "Decaimento Radioativo"])
    
    explicacoes = {
        "Carbono-14": """
        **Datação por Carbono-14**
        
        O Carbono-14 é um isótopo radioativo do carbono com meia-vida de aproximadamente 5730 anos. 
        É produzido na atmosfera pela interação de nêutrons cósmicos com nitrogênio-14.
        
        **Aplicações:**
        - Datação de materiais orgânicos até 50.000 anos
        - Arqueologia e paleontologia
        - Estudos climáticos
        
        **Equação:** `t = (1/λ) · ln(N₀/N)`
        Onde λ é a constante de decaimento (0.000121 anos⁻¹)
        """,
        
        "Blindagem": """
        **Blindagem Radiológica**
        
        A blindagem é utilizada para reduzir a intensidade da radiação através da absorção ou espalhamento.
        
        **Materiais comuns:**
        - Chumbo (alto Z, alta densidade)
        - Concreto (para neutrons e raios gama)
        - Água (para moderar nêutrons)
        
        **Lei da Atenuação:** `I = I₀ · e^(-μx)`
        Onde μ é o coeficiente de atenuação linear e x é a espessura do material.
        """,
        
        "Compton": """
        **Efeito Compton**
        
        O espalhamento Compton é a interação de fótons com elétrons livres ou fracamente ligados, 
        resultando em transferência de energia para o elétron e mudança de direção do fóton.
        
        **Características:**
        - Dominante para energias intermediárias (0.1-10 MeV)
        - Depende do ângulo de espalhamento
        - Produz radiação secundária
        
        **Equação:** `E' = E / [1 + (E/mₑc²)(1 - cosθ)]`
        """,
        
        "Produção de Pares": """
        **Produção de Pares**
        
        A produção de pares ocorre quando um fóton de alta energia interage com o campo 
        eletromagnético de um núcleo, convertendo-se em um par elétron-pósitron.
        
        **Características:**
        - Requer energia mínima de 1.022 MeV (2mₑc²)
        - Probabilidade aumenta com a energia do fóton
        - Importante para energias acima de 5 MeV
        
        **Equação:** `Eₖ = E - 2mₑc²`
        """,
        
        "Decaimento Radioativo": """
        **Decaimento Radioativo**
        
        Processo pelo qual núcleos instáveis emitem radiação para atingir estabilidade.
        
        **Tipos de decaimento:**
        - Alpha (α): emissão de núcleos de hélio
        - Beta (β): conversão de nêutrons em prótons ou vice-versa
        - Gama (γ): emissão de fótons de alta energia
        
        **Lei do decaimento:** `N(t) = N₀ · e^(-λt)`
        Onde λ é a constante de decaimento, relacionada à meia-vida por `λ = ln(2)/T½`
        """
    }
    
    st.markdown("---")
    st.markdown(explicacoes[tema])

def modulo_quiz():
    st.header("❓ Quiz Interativo")
    
    st.info("Teste seus conhecimentos em física radiológica!")
    
    # Perguntas e respostas
    perguntas = [
        {
            "pergunta": "Qual é a meia-vida do Carbono-14?",
            "opcoes": ["5730 anos", "1620 anos", "7560 anos", "1200 anos"],
            "resposta": 0
        },
        {
            "pergunta": "Qual material oferece melhor proteção contra radiação gama?",
            "opcoes": ["Chumbo", "Concreto", "Água", "Alumínio"],
            "resposta": 0
        },
        {
            "pergunta": "Qual é a energia mínima necessária para produção de pares?",
            "opcoes": ["1.022 MeV", "0.511 MeV", "2.044 MeV", "0.256 MeV"],
            "resposta": 0
        }
    ]
    
    respostas = []
    for i, pergunta in enumerate(perguntas):
        st.markdown(f"**{i+1}. {pergunta['pergunta']}**")
        resposta = st.radio(f"Opções para pergunta {i+1}:", pergunta["opcoes"], key=f"q{i}")
        respostas.append(resposta)
    
    if st.button("✅ Verificar Respostas", use_container_width=True):
        acertos = 0
        resultados = []
        
        for i, pergunta in enumerate(perguntas):
            if respostas[i] == pergunta["opcoes"][pergunta["resposta"]]:
                acertos += 1
                resultados.append(f"Pergunta {i+1}: ✅ Correto")
            else:
                resultados.append(f"Pergunta {i+1}: ❌ Incorreto (Resposta correta: {pergunta['opcoes'][pergunta['resposta']]})")
        
        st.markdown("---")
        st.markdown("### 📊 Resultado do Quiz")
        st.markdown(f'<div class="result-box"><h4>🎯 Pontuação: <span style="color:#d32f2f">{acertos}/{len(perguntas)}</span></h4></div>', unsafe_allow_html=True)
        
        for resultado in resultados:
            st.write(resultado)
        
        # Resultado para download
        resultado_texto = f"Resultado do Quiz: {acertos}/{len(perguntas)}\n\n"
        for i, resultado in enumerate(resultados):
            resultado_texto += f"{resultado}\n"
        
        st.download_button("📥 Baixar resultado (.txt)", data=resultado_texto, 
                          file_name="quiz_resultado.txt", mime="text/plain",
                          use_container_width=True)

def modulo_exportar():
    st.header("📤 Exportar Dados")
    
    st.info("Cole seus dados abaixo para exportar em diferentes formatos")
    
    texto = st.text_area("Insira os dados para exportar (um valor por linha ou separados por vírgula/vírgula e espaço)")
    
    if texto:
        # Processar diferentes formatos de entrada
        linhas = texto.strip().split("\n")
        dados_processados = []
        
        for linha in linhas:
            # Tentar separar por vírgula
            if "," in linha:
                valores = [v.strip() for v in linha.split(",")]
                dados_processados.extend(valores)
            else:
                dados_processados.append(linha.strip())
        
        # Remover entradas vazias
        dados_processados = [d for d in dados_processados if d]
        
        st.markdown("---")
        st.markdown("### 📄 Dados Processados")
        
        # Mostrar preview
        preview = "\n".join(dados_processados[:10])
        if len(dados_processados) > 10:
            preview += "\n..."
        
        st.text(preview)
        st.write(f"Total de itens: {len(dados_processados)}")
        
        # Opções de exportação
        col1, col2 = st.columns(2)
        
        with col1:
            # Exportar como TXT
            st.download_button("📥 Baixar TXT", data="\n".join(dados_processados), 
                              file_name="dados_exportados.txt", mime="text/plain",
                              use_container_width=True)
        
        with col2:
            # Exportar como CSV
            csv_data = "Valor\n" + "\n".join(dados_processados)
            st.download_button("📥 Baixar CSV", data=csv_data, 
                              file_name="dados_exportados.csv", mime="text/csv",
                              use_container_width=True)

def modulo_comparar():
    st.header("📈 Comparar Simulações")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Simulação A")
        A = st.text_input("Valores separados por vírgula", key="simA")
    
    with col2:
        st.subheader("Simulação B")
        B = st.text_input("Valores separados por vírgula", key="simB")
    
    if st.button("📊 Comparar Simulações", use_container_width=True):
        try:
            # Processar dados
            listaA = [float(x.strip()) for x in A.split(",") if x.strip()]
            listaB = [float(x.strip()) for x in B.split(",") if x.strip()]
            
            if not listaA or not listaB:
                st.error("Ambas as simulações precisam ter dados!")
                return
                
            # Calcular estatísticas
            mA = np.mean(listaA)
            mB = np.mean(listaB)
            stdA = np.std(listaA)
            stdB = np.std(listaB)
            diff = mA - mB
            diff_percent = (diff / ((mA + mB) / 2)) * 100 if (mA + mB) > 0 else 0
            
            st.markdown("---")
            st.markdown("### 📊 Resultados da Comparação")
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.metric("Média A", f"{mA:.2f}", f"±{stdA:.2f}")
            
            with col2:
                st.metric("Média B", f"{mB:.2f}", f"±{stdB:.2f}")
            
            st.metric("Diferença", f"{diff:.2f}", f"{diff_percent:.1f}%")
            
            # Gráfico de comparação
            fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
            
            # Boxplot
            ax1.boxplot([listaA, listaB], labels=['Simulação A', 'Simulação B'])
            ax1.set_title("Distribuição dos Dados")
            ax1.grid(True, axis='y')
            
            # Gráfico de barras com desvio padrão
            medios = [mA, mB]
            erros = [stdA, stdB]
            ax2.bar(['Simulação A', 'Simulação B'], medios, yerr=erros, 
                   capsize=10, color=['skyblue', 'lightgreen'], edgecolor='navy')
            ax2.set_title("Médias com Desvio Padrão")
            ax2.grid(True, axis='y')
            
            plt.tight_layout()
            st.pyplot(fig)
            
            # Tabela de dados
            max_len = max(len(listaA), len(listaB))
            df_data = {
                "Simulação A": listaA + [None] * (max_len - len(listaA)),
                "Simulação B": listaB + [None] * (max_len - len(listaB))
            }
            df = pd.DataFrame(df_data)
            st.dataframe(df, use_container_width=True)
            
            # Opções de download
            st.download_button("📥 Baixar CSV", data=df.to_csv(index=False), 
                              file_name="comparacao_simulacoes.csv", mime="text/csv",
                              use_container_width=True)
            
        except ValueError:
            st.error("❌ Dados inválidos. Use números separados por vírgula.")

# Mapeamento de funções
modulo_funcoes = {
    "datacao_radiometrica": modulo_datacao_radiometrica,
    "blindagem": modulo_blindagem,
    "radioterapia": modulo_radioterapia,
    "dose": modulo_dose,
    "clinico": modulo_clinico,
    "ambiental": modulo_ambiental,
    "compton": modulo_compton,
    "pares": modulo_pares,
    "ocupacional": modulo_ocupacional,
    "historico": modulo_historico,
    "decaimento": modulo_decaimento,
    "explicativo": modulo_explicativo,
    "quiz": modulo_quiz,
    "exportar": modulo_exportar,
    "comparar": modulo_comparar
}

# Executa o módulo selecionado
if modulo in modulos:
    modulo_funcoes[modulos[modulo]]()
else:
    st.error("Módulo não encontrado!")
