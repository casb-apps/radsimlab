import streamlit as st
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import time
from datetime import datetime
import base64

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
        font-size: 3rem;
        color: #1E88E5;
        text-align: center;
        margin-bottom: 2rem;
    }
    .module-card {
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        background-color: #f0f2f6;
    }
    .result-box {
        background-color: #e8f5e9;
        padding: 15px;
        border-radius: 10px;
        margin-top: 15px;
    }
    .warning-box {
        background-color: #ffebee;
        padding: 15px;
        border-radius: 10px;
        margin-top: 15px;
    }
</style>
""", unsafe_allow_html=True)

# Título principal
st.markdown('<h1 class="main-header">🔬 RadSimLab Pro – Simulador Radiológico Avançado</h1>', unsafe_allow_html=True)

# Sidebar com informações
with st.sidebar:
    st.image("https://img.icons8.com/dusk/64/000000/radioactive.png", width=80)
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
    
    st.markdown("---")
    st.markdown("### 🎨 Tema")
    tema = st.radio("Selecionar tema", ["Claro", "Escuro"], index=0)
    
    if tema == "Escuro":
        st.markdown("""
        <style>
            .stApp {
                background-color: #1E1E1E;
                color: #FFFFFF;
            }
        </style>
        """, unsafe_allow_html=True)

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
            time.sleep(0.5)  # Simulação de processamento
            idade = -math.log(f) / l
            
            st.markdown("---")
            st.markdown("### 📊 Resultados")
            st.markdown(f'<div class="result-box"><h4>🧪 Idade estimada: <span style="color:#d32f2f">{idade:,.2f} anos</span></h4></div>', unsafe_allow_html=True)
            
            # Cálculo da meia-vida para verificação
            meia_vida = math.log(2) / l
            st.info(f"Meia-vida utilizada: {meia_vida:,.2f} anos")
            
            st.markdown("**📐 Equação utilizada:** `t = -ln(f) / λ`")
            
            # Gráfico interativo com Plotly
            tempos = np.linspace(0, idade * 1.5, 100)
            fracoes = np.exp(-l * tempos)
            
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=tempos, y=fracoes, mode='lines', name='f(t) = e^(–λt)',
                                    line=dict(color='royalblue', width=3)))
            fig.add_trace(go.Scatter(x=[idade], y=[f], mode='markers', name='Idade estimada',
                                    marker=dict(color='red', size=10)))
            
            fig.update_layout(
                title="Decaimento do Carbono-14",
                xaxis_title="Tempo (anos)",
                yaxis_title="Fração de C-14",
                hovermode="x unified",
                showlegend=True
            )
            
            st.plotly_chart(fig, use_container_width=True)
            
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
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=tempos, y=razoes, mode='lines', name='R(t) = e^(λt) – 1',
                                line=dict(color='green', width=3)))
        fig.add_trace(go.Scatter(x=[idade], y=[R], mode='markers', name='Idade estimada',
                                marker=dict(color='red', size=10)))
        
        fig.update_layout(
            title="Acúmulo de Argônio-40",
            xaxis_title="Tempo (anos)",
            yaxis_title="Razão Ar/K",
            hovermode="x unified"
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
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
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=tempos, y=razoes, mode='lines', name='R(t) = e^(λt) – 1',
                                line=dict(color='orange', width=3)))
        fig.add_trace(go.Scatter(x=[idade], y=[R], mode='markers', name='Idade estimada',
                                marker=dict(color='red', size=10)))
        
        fig.update_layout(
            title="Acúmulo de Chumbo-206",
            xaxis_title="Tempo (anos)",
            yaxis_title="Razão Pb/U",
            hovermode="x unified"
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
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
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=tempos, y=razoes, mode='lines', name='R(t) = e^(λt) – 1',
                                line=dict(color='purple', width=3)))
        fig.add_trace(go.Scatter(x=[idade], y=[R], mode='markers', name='Idade estimada',
                                marker=dict(color='red', size=10)))
        
        fig.update_layout(
            title="Acúmulo de Estrôncio-87",
            xaxis_title="Tempo (anos)",
            yaxis_title="Razão Sr/Rb",
            hovermode="x unified"
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
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
        
        # Gráfico
        espessuras = np.linspace(0, x * 1.5, 100)
        doses = I0 * np.exp(-mu * espessuras)
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=espessuras, y=doses, mode='lines', name=f'Dose com blindagem de {material}',
                                line=dict(color='blue', width=3)))
        fig.add_trace(go.Scatter(x=[x], y=[I], mode='markers', name='Espessura mínima',
                                marker=dict(color='red', size=10)))
        fig.add_hline(y=I, line_dash="dash", line_color="red", annotation_text="Dose desejada")
        
        fig.update_layout(
            title=f"Atenuação da dose com blindagem de {material}",
            xaxis_title="Espessura (cm)",
            yaxis_title="Dose (µSv/h)",
            hovermode="x unified"
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
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

# Adicione aqui as outras funções dos módulos (elas permanecem semelhantes às originais, mas podem ser melhoradas)

# ... (outras funções de módulo)

def modulo_decaimento():
    st.header("📉 Simulação de Decaimento Radioativo")
    
    col1, col2 = st.columns(2)
    
    with col1:
        N0 = st.number_input("Quantidade inicial (Bq)", min_value=1.0, value=1000.0)
        meia_vida = st.number_input("Meia-vida (anos)", min_value=0.01, value=5730.0)
        tempo = st.number_input("Tempo decorrido (anos)", min_value=0.0, value=10000.0)
    
    if st.button("📉 Calcular Decaimento", use_container_width=True):
        lambda_val = math.log(2) / meia_vida
        N = N0 * math.exp(-lambda_val * tempo)
        fração_restante = N / N0
        
        st.markdown("---")
        st.markdown("### 📊 Resultados")
        st.markdown(f'<div class="result-box"><h4>📉 Quantidade restante: <span style="color:#d32f2f">{N:,.2f} Bq</span></h4></div>', unsafe_allow_html=True)
        st.markdown(f'<div class="result-box"><h4>📊 Fração restante: <span style="color:#d32f2f">{fração_restante:.4f}</span></h4></div>', unsafe_allow_html=True)
        st.markdown("**📐 Equação utilizada:** `N = N₀ · e^(-λt)`")
        
        # Gráfico
        tempos = np.linspace(0, meia_vida * 5, 100)
        quantidades = N0 * np.exp(-lambda_val * tempos)
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=tempos, y=quantidades, mode='lines', name='N(t) = N₀ · e^(-λt)',
                                line=dict(color='red', width=3)))
        fig.add_trace(go.Scatter(x=[tempo], y=[N], mode='markers', name='Valor no tempo especificado',
                                marker=dict(color='blue', size=10)))
        
        # Adicionar linhas de meia-vida
        for i in range(1, 6):
            t_meia_vida = meia_vida * i
            n_meia_vida = N0 * (0.5 ** i)
            fig.add_vline(x=t_meia_vida, line_dash="dash", line_color="green", 
                         annotation_text=f"{i} meia-vida", annotation_position="top right")
            fig.add_hline(y=n_meia_vida, line_dash="dash", line_color="green")
        
        fig.update_layout(
            title="Decaimento Radioativo",
            xaxis_title="Tempo (anos)",
            yaxis_title="Quantidade (Bq)",
            hovermode="x unified"
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        # Tabela de dados
        df = pd.DataFrame({"Tempo (anos)": tempos, "Quantidade (Bq)": quantidades})
        st.download_button("📥 Baixar CSV", data=df.to_csv(index=False), 
                          file_name="decaimento.csv", mime="text/csv",
                          use_container_width=True)

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
modulo_funcoes[modulos[modulo]]()
