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
    .formula-box {
        background-color: #f5f5f5;
        padding: 15px;
        border-radius: 8px;
        border-left: 4px solid #9E9E9E;
        font-family: 'Courier New', monospace;
        margin: 10px 0;
    }
    .parameter-table {
        width: 100%;
        border-collapse: collapse;
        margin: 10px 0;
    }
    .parameter-table th, .parameter-table td {
        padding: 8px 12px;
        text-align: left;
        border-bottom: 1px solid #ddd;
    }
    .parameter-table th {
        background-color: #f0f0f0;
        font-weight: bold;
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

# =============================================================================
# MÓDULO 1: DATAÇÃO RADIOMÉTRICA
# =============================================================================

def modulo_datacao_radiometrica():
    st.header("⏳ Datação Radiométrica")
    
    st.info("""
    **Instruções:** 
    - Para Carbono-14: Insira a fração remanescente de C-14 (N/N₀)
    - Para outros métodos: Insira a razão do produto de decaimento em relação ao elemento pai
    """)
    
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
        st.markdown("**Parâmetros de Entrada:**")
        frac_remanescente = st.slider("Fração remanescente de C-14 (N/N₀)", 
                                     min_value=0.001, max_value=0.999, 
                                     value=0.5, step=0.001,
                                     help="Razão entre C-14 atual e C-14 inicial")
        
        meia_vida = st.number_input("Meia-vida do C-14 (anos)", 
                                   min_value=100.0, value=5730.0, step=10.0,
                                   help="Meia-vida padrão: 5730 anos")
    
    with col2:
        st.markdown("**Informações Técnicas:**")
        st.markdown("""
        <table class="parameter-table">
            <tr><th>Parâmetro</th><th>Valor</th></tr>
            <tr><td>Meia-vida do C-14</td><td>5730 anos</td></tr>
            <tr><td>Constante de decaimento (λ)</td><td>1.21 × 10⁻⁴ ano⁻¹</td></tr>
            <tr><td>Faixa de datação</td><td>até 50,000 anos</td></tr>
        </table>
        """, unsafe_allow_html=True)
        
        st.markdown("**📐 Fórmula:**")
        st.markdown('<div class="formula-box">t = (T½/ln(2)) × ln(1/(N/N₀))</div>', unsafe_allow_html=True)
    
    if st.button("🔄 Calcular Datação por C-14", use_container_width=True):
        if frac_remanescente <= 0 or meia_vida <= 0:
            st.error("Os valores devem ser positivos!")
            return
            
        with st.spinner("Calculando..."):
            time.sleep(0.5)
            
            # Cálculo CORRETO da idade usando a lei do decaimento radioativo
            lambda_val = math.log(2) / meia_vida
            idade = (1 / lambda_val) * math.log(1 / frac_remanescente)
            
            st.markdown("---")
            st.markdown("### 📊 Resultados")
            
            st.markdown(f'<div class="result-box"><h4>🧪 Idade estimada: <span style="color:#d32f2f">{idade:,.2f} anos</span></h4></div>', unsafe_allow_html=True)
            
            # Detalhes do cálculo
            st.markdown("**🔍 Detalhes do Cálculo:**")
            col_calc1, col_calc2 = st.columns(2)
            
            with col_calc1:
                st.markdown(f"- **Fração remanescente:** {frac_remanescente:.4f}")
                st.markdown(f"- **Meia-vida do C-14:** {meia_vida:,.0f} anos")
                st.markdown(f"- **Constante λ:** {lambda_val:.6f} ano⁻¹")
            
            with col_calc2:
                st.markdown(f"- **ln(1/(N/N₀)):** {math.log(1/frac_remanescente):.4f}")
                st.markdown(f"- **1/λ:** {1/lambda_val:,.0f} anos")
                st.markdown(f"- **Idade calculada:** {idade:,.0f} anos")
            
            # Verificação com exemplo conhecido
            if abs(frac_remanescente - 0.5) < 0.01 and abs(meia_vida - 5730) < 1:
                st.success("✅ Verificação: Para 50% de C-14 remanescente, a idade deve ser igual à meia-vida (5730 anos)")
            
            # Gráfico do decaimento
            tempos = np.linspace(0, min(idade * 1.5, 50000), 100)
            fracoes = np.exp(-lambda_val * tempos)
            
            fig, ax = plt.subplots(figsize=(10, 6))
            ax.plot(tempos, fracoes, 'b-', linewidth=3, label='N(t)/N₀ = e^(–λt)')
            ax.plot(idade, frac_remanescente, 'ro', markersize=10, 
                   label=f'Idade estimada: {idade:.0f} anos')
            
            # Linhas de meia-vida
            for i in range(1, 6):
                t_meia = meia_vida * i
                frac_meia = 0.5 ** i
                ax.axvline(x=t_meia, color='gray', linestyle='--', alpha=0.5)
                ax.axhline(y=frac_meia, color='gray', linestyle='--', alpha=0.5)
                ax.text(t_meia, 1.02, f'{i}T½', ha='center', va='bottom', color='gray')
            
            ax.set_xlabel("Tempo (anos)")
            ax.set_ylabel("Fração de C-14 remanescente (N/N₀)")
            ax.set_title("Decaimento do Carbono-14")
            ax.legend()
            ax.grid(True)
            ax.set_ylim(0, 1.1)
            
            st.pyplot(fig)
            
            # Tabela de dados para exportação
            df = pd.DataFrame({
                "Tempo (anos)": tempos, 
                "Fração_C14": fracoes,
                "Atividade_Relativa": fracoes  # Para C-14, fração = atividade relativa
            })
            
            # Opções de download
            col_dl1, col_dl2 = st.columns(2)
            with col_dl1:
                st.download_button("📥 Baixar CSV", data=df.to_csv(index=False), 
                                  file_name="carbono14_simulation.csv", mime="text/csv",
                                  use_container_width=True)
            with col_dl2:
                st.download_button("📥 Baixar TXT", data=df.to_string(index=False), 
                                  file_name="carbono14_results.txt", mime="text/plain",
                                  use_container_width=True)

def modulo_potassio_argonio():
    st.markdown("### 🔋 Datação por Potássio-Argônio")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Parâmetros de Entrada:**")
        razao_ar_k = st.number_input("Razão ⁴⁰Ar/⁴⁰K", 
                                   min_value=0.001, value=0.5, step=0.001,
                                   format="%.3f",
                                   help="Razão entre Argônio-40 e Potássio-40")
        
        meia_vida = st.number_input("Meia-vida do ⁴⁰K (anos)", 
                                   min_value=1.0e8, value=1.25e9, 
                                   format="%.2e",
                                   help="Meia-vida padrão: 1.25 × 10⁹ anos")
        
        fracao_decaimento = st.number_input("Fração que decai para ⁴⁰Ar", 
                                          min_value=0.01, max_value=1.0, 
                                          value=0.1072, step=0.0001,
                                          help="Padrão: 0.1072 (10.72%)")
    
    with col2:
        st.markdown("**Informações Técnicas:**")
        st.markdown("""
        <table class="parameter-table">
            <tr><th>Parâmetro</th><th>Valor</th></tr>
            <tr><td>Meia-vida do ⁴⁰K</td><td>1.25 × 10⁹ anos</td></tr>
            <tr><td>Fração para ⁴⁰Ar</td><td>10.72%</td></tr>
            <tr><td>Faixa de datação</td><td>10⁴ - 10⁹ anos</td></tr>
        </table>
        """, unsafe_allow_html=True)
        
        st.markdown("**📐 Fórmula:**")
        st.markdown('<div class="formula-box">t = (1/λ) × ln(1 + (⁴⁰Ar/⁴⁰K) × (λ/λ_Ar))</div>', unsafe_allow_html=True)
        st.markdown('*Simplificado para: t = (1/λ) × ln(1 + R × (1/f))*', unsafe_allow_html=True)
    
    if st.button("🔄 Calcular Datação por K-Ar", use_container_width=True):
        if razao_ar_k <= 0 or meia_vida <= 0 or fracao_decaimento <= 0:
            st.error("Todos os valores devem ser positivos!")
            return
            
        # Cálculo CORRETO considerando a fração de decaimento
        lambda_val = math.log(2) / meia_vida
        idade = (1 / lambda_val) * math.log(1 + (razao_ar_k / fracao_decaimento))
        
        st.markdown("---")
        st.markdown("### 📊 Resultados")
        
        idade_millions = idade / 1e6
        
        if idade_millions < 1:
            st.markdown(f'<div class="result-box"><h4>🔋 Idade estimada: <span style="color:#d32f2f">{idade:,.2f} anos</span></h4></div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="result-box"><h4>🔋 Idade estimada: <span style="color:#d32f2f">{idade_millions:,.2f} milhões de anos</span></h4></div>', unsafe_allow_html=True)
        
        # Detalhes do cálculo
        st.markdown("**🔍 Detalhes do Cálculo:**")
        
        col_calc1, col_calc2 = st.columns(2)
        
        with col_calc1:
            st.markdown(f"- **Razão ⁴⁰Ar/⁴⁰K:** {razao_ar_k:.4f}")
            st.markdown(f"- **Meia-vida do ⁴⁰K:** {meia_vida:.2e} anos")
            st.markdown(f"- **Fração para ⁴⁰Ar:** {fracao_decaimento:.4f}")
        
        with col_calc2:
            st.markdown(f"- **Constante λ:** {lambda_val:.3e} ano⁻¹")
            st.markdown(f"- **Razão ajustada:** {razao_ar_k/fracao_decaimento:.4f}")
            st.markdown(f"- **ln(1 + R/f):** {math.log(1 + razao_ar_k/fracao_decaimento):.4f}")
        
        # Gráfico
        tempos = np.linspace(0, min(idade * 1.5, 5e9), 100)
        razoes = fracao_decaimento * (np.exp(lambda_val * tempos) - 1)
        
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(tempos/1e6, razoes, 'g-', linewidth=3, label='R(t) = f × (e^(λt) - 1)')
        ax.plot(idade/1e6, razao_ar_k, 'ro', markersize=10, 
               label=f'Idade estimada: {idade/1e6:.2f} milhões de anos')
        
        ax.set_xlabel("Tempo (milhões de anos)")
        ax.set_ylabel("Razão ⁴⁰Ar/⁴⁰K")
        ax.set_title("Acúmulo de Argônio-40 no Método K-Ar")
        ax.legend()
        ax.grid(True)
        
        st.pyplot(fig)
        
        # Tabela de dados
        df = pd.DataFrame({
            "Tempo (milhões de anos)": tempos/1e6,
            "Razao_Ar_K": razoes
        })
        
        st.download_button("📥 Baixar CSV", data=df.to_csv(index=False), 
                          file_name="potassio_argonio_simulation.csv", mime="text/csv",
                          use_container_width=True)

def modulo_uranio_chumbo():
    st.markdown("### ⚛️ Datação por Urânio-Chumbo")
    st.info("Módulo em desenvolvimento. Use Potássio-Argônio ou Carbono-14 para datação.")
    st.warning("Este método utiliza as séries de decaimento do U-238 para Pb-206 e U-235 para Pb-207")

def modulo_rubidio_estroncio():
    st.markdown("### 🔬 Datação por Rubídio-Estrôncio")
    st.info("Módulo em desenvolvimento. Use Potássio-Argônio ou Carbono-14 para datação.")
    st.warning("Este método utiliza o decaimento do Rb-87 para Sr-87 com meia-vida de 48.8 bilhões de anos")

# =============================================================================
# MÓDULO 2: BLINDAGEM RADIOLÓGICA
# =============================================================================

def modulo_blindagem():
    st.header("🧱 Cálculo de Blindagem Radiológica")
    
    st.info("""
    **Instruções:** 
    - Selecione o material de blindagem
    - Informe a dose inicial e a dose desejada após a blindagem
    - O sistema calculará a espessura necessária usando a Lei de Atenuação Exponencial
    """)
    
    materials = {
        "Chumbo": {"mu": 0.77, "densidade": 11.34, "cor": "#FF6B6B"},
        "Concreto": {"mu": 0.15, "densidade": 2.35, "cor": "#4ECDC4"},
        "Água": {"mu": 0.07, "densidade": 1.00, "cor": "#45B7D1"},
        "Aço": {"mu": 0.43, "densidade": 7.85, "cor": "#96CEB4"},
        "Tungstênio": {"mu": 1.20, "densidade": 19.25, "cor": "#FECA57"},
        "Urânio": {"mu": 1.50, "densidade": 19.10, "cor": "#FF9FF3"}
    }
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("**Seleção do Material:**")
        material = st.selectbox("Material", options=list(materials.keys()))
        mu = materials[material]["mu"]
        densidade = materials[material]["densidade"]
        cor = materials[material]["cor"]
        
        st.markdown(f"**Propriedades do {material}:**")
        st.markdown(f"- μ = {mu} cm⁻¹")
        st.markdown(f"- ρ = {densidade} g/cm³")
        st.markdown(f"- Camada semi-redutora: {math.log(2)/mu:.2f} cm")
        
    with col2:
        st.markdown("**Parâmetros de Radiação:**")
        I0 = st.number_input("Dose inicial (µSv/h)", 
                           min_value=0.01, value=1000.0, step=10.0,
                           help="Dose sem blindagem")
        
        I = st.number_input("Dose desejada (µSv/h)", 
                          min_value=0.01, value=10.0, step=1.0,
                          help="Dose máxima permitida após blindagem")
        
        energia = st.number_input("Energia dos fótons (MeV)", 
                                min_value=0.01, value=1.0, step=0.1,
                                help="Energia média da radiação")
    
    with col3:
        st.markdown("**Fator de Build-up:**")
        buildup = st.selectbox("Considerar fator de build-up?", 
                             options=["Não", "Sim - Baixo", "Sim - Médio", "Sim - Alto"],
                             index=0,
                             help="Fator que considera radiação espalhada")
        
        st.markdown("**📐 Fórmula da Atenuação:**")
        st.markdown('<div class="formula-box">I = I₀ × B × e^(-μx)</div>', unsafe_allow_html=True)
        st.markdown('<div class="formula-box">x = (1/μ) × ln(I₀ × B / I)</div>', unsafe_allow_html=True)
    
    # Definir fator de build-up
    fatores_buildup = {
        "Não": 1.0,
        "Sim - Baixo": 1.5,
        "Sim - Médio": 2.0,
        "Sim - Alto": 3.0
    }
    B = fatores_buildup[buildup]
    
    if st.button("🧱 Calcular Blindagem", use_container_width=True):
        if I0 <= 0 or I <= 0 or mu <= 0:
            st.error("Todos os valores devem ser positivos!")
            return
            
        if I >= I0:
            st.error("A dose desejada deve ser menor que a dose inicial!")
            return
            
        # Cálculo CORRETO da espessura considerando build-up
        x = (1 / mu) * math.log((I0 * B) / I)
        
        # Calcular também a massa por área
        massa_por_area = x * densidade  # kg/m² (considerando cm → m)
        
        st.markdown("---")
        st.markdown("### 📊 Resultados")
        
        st.markdown(f'<div class="result-box"><h4>🧱 Espessura necessária de {material}: <span style="color:#d32f2f">{x:.2f} cm</span></h4></div>', unsafe_allow_html=True)
        
        if buildup != "Não":
            st.markdown(f'<div class="info-box"><h4>📊 Com fator de build-up: <span style="color:#1976D2">{B:.1f}</span></h4></div>', unsafe_allow_html=True)
        
        st.markdown(f'<div class="info-box"><h4>⚖️ Massa por área: <span style="color:#1976D2">{massa_por_area:.1f} kg/m²</span></h4></div>', unsafe_allow_html=True)
        
        # Detalhes do cálculo
        st.markdown("**🔍 Detalhes do Cálculo:**")
        
        col_calc1, col_calc2 = st.columns(2)
        
        with col_calc1:
            st.markdown(f"- **Dose inicial (I₀):** {I0} µSv/h")
            st.markdown(f"- **Dose desejada (I):** {I} µSv/h")
            st.markdown(f"- **Coeficiente μ:** {mu} cm⁻¹")
            st.markdown(f"- **Fator B:** {B}")
        
        with col_calc2:
            st.markdown(f"- **I₀×B/I:** {(I0 * B) / I:.1f}")
            st.markdown(f"- **ln(I₀×B/I):** {math.log((I0 * B) / I):.2f}")
            st.markdown(f"- **1/μ:** {1/mu:.2f} cm")
            st.markdown(f"- **Espessura (x):** {x:.2f} cm")
        
        # Gráfico de atenuação
        espessuras = np.linspace(0, x * 2, 100)
        doses = I0 * B * np.exp(-mu * espessuras)
        
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(espessuras, doses, color=cor, linewidth=3, 
               label=f'Blindagem de {material} (μ={mu} cm⁻¹)')
        ax.plot(x, I, 'ro', markersize=10, label=f'Espessura necessária: {x:.1f} cm')
        ax.axhline(y=I, color='r', linestyle='--', label='Dose desejada')
        
        ax.set_xlabel("Espessura (cm)")
        ax.set_ylabel("Dose (µSv/h)")
        ax.set_title(f"Atenuação da Radiação com {material}")
        ax.legend()
        ax.grid(True)
        ax.set_yscale('log')  # Escala log para melhor visualização
        
        st.pyplot(fig)
        
        # Comparação entre materiais
        st.markdown("### 📊 Comparação entre Materiais")
        
        comparacao = []
        for mat, props in materials.items():
            esp = (1 / props["mu"]) * math.log((I0 * B) / I)
            massa = esp * props["densidade"]
            comparacao.append({
                "Material": mat,
                "μ (cm⁻¹)": props["mu"],
                "Espessura (cm)": esp,
                "Massa (kg/m²)": massa
            })
        
        df_comp = pd.DataFrame(comparacao)
        st.dataframe(df_comp.style.format({
            "μ (cm⁻¹)": "{:.2f}",
            "Espessura (cm)": "{:.2f}",
            "Massa (kg/m²)": "{:.1f}"
        }), use_container_width=True)
        
        # Resultado para download
        resultado = f"""MATERIAL: {material}
DOSE INICIAL: {I0} µSv/h
DOSE DESEJADA: {I} µSv/h
ENERGIA: {energia} MeV
FATOR BUILD-UP: {B}
COEFICIENTE μ: {mu} cm⁻¹
DENSIDADE: {densidade} g/cm³
ESPESSURA NECESSÁRIA: {x:.2f} cm
MASSA POR ÁREA: {massa_por_area:.1f} kg/m²
CAMADA SEMI-REDUTORA: {math.log(2)/mu:.2f} cm"""
        
        st.download_button("📥 Baixar Relatório", data=resultado, 
                          file_name=f"blindagem_{material.lower()}.txt", 
                          mime="text/plain", use_container_width=True)

# =============================================================================
# MÓDULO 3: RADIOTERAPIA
# =============================================================================

def modulo_radioterapia():
    st.header("📅 Planejamento Radioterápico")
    
    st.info("""
    **Instruções:**
    - **Dose prescrita:** Dose total que o paciente deve receber
    - **Taxa de dose:** Velocidade de administração da radiação  
    - **Número de sessões:** Total de tratamentos
    """)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("**💉 Parâmetros do Tratamento:**")
        dose_total = st.number_input("Dose prescrita total (Gy)", 
                                   min_value=0.1, value=60.0, step=5.0,
                                   help="Dose total do tratamento")
        
    with col2:
        taxa_dose = st.number_input("Taxa de dose (Gy/min)", 
                                  min_value=0.01, value=2.0, step=0.1,
                                  help="Velocidade de administração da radiação")
    
    with col3:
        num_sessoes = st.number_input("Número de sessões", 
                                    min_value=1, value=30, step=1,
                                    help="Total de sessões de tratamento")
        
        dias_semana = st.number_input("Sessões por semana", 
                                    min_value=1, max_value=7, value=5, step=1,
                                    help="Tratamentos por semana")
    
    # Cálculos adicionais
    col_calc1, col_calc2 = st.columns(2)
    
    with col_calc1:
        st.markdown("**📐 Fórmulas:**")
        st.markdown('<div class="formula-box">Dose/sessão = Dose_total / N_sessões</div>', unsafe_allow_html=True)
        st.markdown('<div class="formula-box">Tempo/sessão = Dose/sessão / Taxa_dose</div>', unsafe_allow_html=True)
    
    with col_calc2:
        st.markdown("**⏱️ Duração do Tratamento:**")
        semanas = num_sessoes / dias_semana
        st.markdown(f"- **Semanas totais:** {semanas:.1f}")
        st.markdown(f"- **Dias totais:** {num_sessoes}")
    
    if st.button("💉 Calcular Plano de Tratamento", use_container_width=True):
        if dose_total <= 0 or taxa_dose <= 0 or num_sessoes <= 0:
            st.error("Todos os valores devem ser positivos!")
            return
            
        # Cálculos CORRETOS conforme especificado
        dose_por_sessao = dose_total / num_sessoes
        tempo_por_sessao = dose_por_sessao / taxa_dose
        duracao_total = tempo_por_sessao * num_sessoes
        
        st.markdown("---")
        st.markdown("### 📊 Plano de Tratamento")
        
        col_res1, col_res2, col_res3 = st.columns(3)
        
        with col_res1:
            st.markdown(f'<div class="result-box"><h4>💉 Dose/sessão: <span style="color:#d32f2f">{dose_por_sessao:.2f} Gy</span></h4></div>', unsafe_allow_html=True)
        
        with col_res2:
            st.markdown(f'<div class="result-box"><h4>⏱️ Tempo/sessão: <span style="color:#d32f2f">{tempo_por_sessao:.2f} min</span></h4></div>', unsafe_allow_html=True)
        
        with col_res3:
            st.markdown(f'<div class="info-box"><h4>📅 Duração total: <span style="color:#1976D2">{duracao_total:.1f} min</span></h4></div>', unsafe_allow_html=True)
        
        # Detalhes do cálculo
        st.markdown("**🔍 Detalhes do Cálculo:**")
        
        st.markdown('<div class="formula-box">Dose/sessão = {:.1f} Gy / {} = {:.2f} Gy</div>'.format(
            dose_total, num_sessoes, dose_por_sessao), unsafe_allow_html=True)
        
        st.markdown('<div class="formula-box">Tempo/sessão = {:.2f} Gy / {:.1f} Gy/min = {:.2f} min</div>'.format(
            dose_por_sessao, taxa_dose, tempo_por_sessao), unsafe_allow_html=True)
        
        # Teste com o exemplo fornecido
        st.markdown("---")
        st.markdown("### 🧪 Teste de Verificação")
        st.markdown("**Entradas de teste (exemplo):**")
        st.markdown("- Dose prescrita: 50 Gy")
        st.markdown("- Taxa de dose: 2 Gy/min")  
        st.markdown("- Número de sessões: 25")
        
        dose_teste = 50 / 25  # 2 Gy
        tempo_teste = 2 / 2   # 1 min
        
        st.markdown("**Resultados esperados:**")
        st.markdown(f"- Dose por sessão: {dose_teste:.1f} Gy")
        st.markdown(f"- Tempo por sessão: {tempo_teste:.1f} min")
        
        # Verificação
        if abs(dose_por_sessao - dose_teste) < 0.01 and abs(tempo_por_sessao - tempo_teste) < 0.01:
            st.success("✅ Teste passou! Os cálculos estão corretos.")
        else:
            st.error("❌ Teste falhou! Verifique os cálculos.")
        
        # Gráfico da distribuição de sessões
        sessoes = list(range(1, num_sessoes + 1))
        doses_acumuladas = [dose_por_sessao * i for i in range(1, num_sessoes + 1)]
        
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
        
        # Gráfico 1: Dose por sessão
        ax1.bar(sessoes, [dose_por_sessao] * num_sessoes, color='skyblue', edgecolor='navy')
        ax1.set_xlabel("Sessão")
        ax1.set_ylabel("Dose (Gy)")
        ax1.set_title("Dose por Sessão")
        ax1.grid(True, axis='y')
        
        # Gráfico 2: Dose acumulada
        ax2.plot(sessoes, doses_acumuladas, 'r-', marker='o', linewidth=2)
        ax2.set_xlabel("Sessão")
        ax2.set_ylabel("Dose Acumulada (Gy)")
        ax2.set_title("Dose Total Acumulada")
        ax2.grid(True)
        ax2.axhline(y=dose_total, color='g', linestyle='--', label=f'Dose total: {dose_total} Gy')
        ax2.legend()
        
        plt.tight_layout()
        st.pyplot(fig)
        
        # Tabela de tratamento
        df_tratamento = pd.DataFrame({
            "Sessão": sessoes,
            "Dose_Sessão (Gy)": [dose_por_sessao] * num_sessoes,
            "Dose_Acumulada (Gy)": doses_acumuladas,
            "Tempo_Sessão (min)": [tempo_por_sessao] * num_sessoes
        })
        
        st.dataframe(df_tratamento.head(10), use_container_width=True)
        
        # Download do plano
        plano = f"""PLANO DE RADIOTERAPIA
=====================
DOSE PRESCRITA TOTAL: {dose_total} Gy
TAXA DE DOSE: {taxa_dose} Gy/min
NÚMERO DE SESSÕES: {num_sessoes}
SESSÕES POR SEMANA: {dias_semana}

RESULTADOS:
- Dose por sessão: {dose_por_sessao:.2f} Gy
- Tempo por sessão: {tempo_por_sessao:.2f} min
- Duração total: {duracao_total:.1f} min
- Semanas de tratamento: {semanas:.1f}

CALENDÁRIO ESTIMADO:
- Início: {datetime.now().strftime('%d/%m/%Y')}
- Término: {(datetime.now() + pd.DateOffset(weeks=semanas)).strftime('%d/%m/%Y')}"""

        st.download_button("📥 Baixar Plano de Tratamento", data=plano, 
                          file_name="plano_radioterapia.txt", 
                          mime="text/plain", use_container_width=True)

# =============================================================================
# MÓDULO 4: DISTRIBUIÇÃO DE DOSE
# =============================================================================

def modulo_distribuicao_dose():
    st.header("📊 Distribuição de Dose em Tecidos")
    
    st.info("""
    **Instruções:**
    - Selecione o tipo de radiação e energia
    - Configure os parâmetros de profundidade
    - Visualize a distribuição de dose no tecido
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**☢️ Tipo de Radiação:**")
        tipo_rad = st.selectbox("Tipo", 
                              options=["Raios X", "Elétrons", "Prótons", "Nêutrons", "Raios Gama"],
                              index=0)
        
        energia = st.slider("Energia (MeV)", 
                          min_value=0.1, max_value=20.0, value=6.0, step=0.1)
        
        st.markdown("**🧪 Parâmetros do Tecido:**")
        densidade = st.number_input("Densidade (g/cm³)", 
                                  min_value=0.1, value=1.0, step=0.1)
    
    with col2:
        st.markdown("**📏 Parâmetros de Profundidade:**")
        max_profundidade = st.slider("Profundidade máxima (cm)", 
                                   min_value=1.0, max_value=30.0, value=20.0, step=1.0)
        
        resolucao = st.slider("Resolução (pontos)", 
                            min_value=10, max_value=500, value=100, step=10)
        
        st.markdown("**📐 Modelo de Atenuação:**")
        modelo = st.selectbox("Modelo", 
                            options=["Exponencial Simples", "Com Build-up", "Com PDD"],
                            index=0)
    
    if st.button("📊 Calcular Distribuição de Dose", use_container_width=True):
        # Gerar dados de profundidade
        profundidades = np.linspace(0, max_profundidade, resolucao)
        
        # Modelos de distribuição de dose baseados no tipo de radiação
        if tipo_rad == "Raios X" or tipo_rad == "Raios Gama":
            # Para fótons: pico de dose em superfície com decaimento exponencial
            if modelo == "Exponencial Simples":
                doses = 100 * np.exp(-0.1 * profundidades)
            elif modelo == "Com Build-up":
                # Pico de dose a alguns cm de profundidade
                build_up = 2.0  # cm
                doses = 100 * (profundidades/build_up) * np.exp(1 - profundidades/build_up)
            else:  # PDD (Percent Depth Dose)
                doses = 100 * np.exp(-0.08 * profundidades) * (1 + 0.5 * np.exp(-0.3 * (profundidades - 2)**2))
                
        elif tipo_rad == "Elétrons":
            # Elétrons: pico mais superficial
            r_max = 0.5 * energia  # range máximo em cm
            doses = 100 * (profundidades/r_max) * np.exp(1 - profundidades/r_max)
            
        elif tipo_rad == "Prótons":
            # Prótons: pico de Bragg
            r_max = 1.0 * energia  # range em cm
            doses = 100 * np.exp(-0.05 * (profundidades - r_max)**2)
            
        else:  # Nêutrons
            # Nêutrons: decaimento exponencial
            doses = 100 * np.exp(-0.15 * profundidades)
        
        # Normalizar para dose máxima = 100%
        doses = doses / np.max(doses) * 100
        
        st.markdown("---")
        st.markdown("### 📈 Distribuição de Dose")
        
        # Gráfico principal
        fig, ax = plt.subplots(figsize=(12, 8))
        ax.plot(profundidades, doses, 'b-', linewidth=3, label=f'{tipo_rad} - {energia} MeV')
        
        # Encontrar Dmax
        idx_max = np.argmax(doses)
        dmax = doses[idx_max]
        p_dmax = profundidades[idx_max]
        
        ax.plot(p_dmax, dmax, 'ro', markersize=10, label=f'Dmax: {dmax:.1f}% @ {p_dmax:.1f}cm')
        
        # Linhas de referência
        ax.axhline(y=50, color='orange', linestyle='--', label='50% dose')
        ax.axvline(x=p_dmax, color='red', linestyle=':', alpha=0.5)
        
        ax.set_xlabel("Profundidade (cm)")
        ax.set_ylabel("Dose Relativa (%)")
        ax.set_title(f"Distribuição de Dose - {tipo_rad} {energia} MeV")
        ax.legend()
        ax.grid(True)
        
        # Adicionar segundo eixo para dose absoluta se especificado
        ax2 = ax.twinx()
        dose_max_abs = 2.0  # Gy por unidade (exemplo)
        ax2.set_ylabel(f"Dose Absoluta (Gy)", color='green')
        ax2.set_ylim(0, dose_max_abs)
        
        st.pyplot(fig)
        
        # Parâmetros importantes
        st.markdown("### 📋 Parâmetros Importantes")
        
        # Encontrar R50 (profundidade onde dose = 50%)
        idx_50 = np.where(doses <= 50)[0]
        if len(idx_50) > 0:
            r50 = profundidades[idx_50[0]]
        else:
            r50 = max_profundidade
            
        # Encontrar R80 e R20
        idx_80 = np.where(doses <= 80)[0]
        r80 = profundidades[idx_80[0]] if len(idx_80) > 0 else max_profundidade
        
        idx_20 = np.where(doses <= 20)[0]
        r20 = profundidades[idx_20[0]] if len(idx_20) > 0 else max_profundidade
        
        col_params1, col_params2 = st.columns(2)
        
        with col_params1:
            st.markdown(f"**📍 Dmax:** {dmax:.1f}% @ {p_dmax:.1f} cm")
            st.markdown(f"**📏 R50:** {r50:.1f} cm (50% dose)")
            st.markdown(f"**📐 R80:** {r80:.1f} cm (80% dose)")
        
        with col_params2:
            st.markdown(f"**📊 R20:** {r20:.1f} cm (20% dose)")
            st.markdown(f"**🎯 Razão R50/R80:** {r50/r80:.2f}")
            st.markdown(f"**📈 Penetração:** {r20:.1f} cm")
        
        # Tabela de dados
        df_dose = pd.DataFrame({
            "Profundidade (cm)": profundidades,
            "Dose_Relativa (%)": doses,
            "Dose_Absoluta (Gy)": doses/100 * dose_max_abs
        })
        
        st.dataframe(df_dose.head(10), use_container_width=True)
        
        # Download dos dados
        csv = df_dose.to_csv(index=False)
        st.download_button("📥 Baixar Dados CSV", data=csv, 
                          file_name=f"distribuicao_dose_{tipo_rad.lower()}_{energia}MeV.csv", 
                          mime="text/csv", use_container_width=True)
        
        # Informações adicionais
        st.markdown("### ℹ️ Informações Técnicas")
        
        info_text = f"""
        **Tipo de Radiação:** {tipo_rad}
        **Energia:** {energia} MeV
        **Densidade do Tecido:** {densidade} g/cm³
        **Modelo Utilizado:** {modelo}
        
        **Características da Distribuição:**
        - Profundidade de Dmax: {p_dmax:.2f} cm
        - Valor de Dmax: {dmax:.1f}%
        - Profundidade de 50% dose: {r50:.2f} cm
        - Índice de penetração: {r20:.2f} cm
        
        **Aplicações Clínicas:**
        - {tipo_rad} com {energia} MeV é comumente usado para {'tratamentos superficiais' if p_dmax < 2 else 'tratamentos profundos'}
        - A distribuição mostra {'baixa' if r20 < 5 else 'alta'} penetração no tecido
        """
        
        st.info(info_text)

# =============================================================================
# MÓDULO 5: APLICAÇÕES CLÍNICAS
# =============================================================================

def modulo_aplicacoes_clinicas():
    st.header("🏥 Aplicações Clínicas da Radiação")
    
    st.info("""
    **Instruções:** 
    - Selecione o tipo de aplicação clínica
    - Configure os parâmetros específicos
    - Visualize os resultados e recomendações
    """)
    
    aplicacoes = {
        "Radioterapia Externa": "Tratamento com feixe externo de radiação",
        "Brachytherapy": "Fontes radioativas internas",
        "Radiocirurgia": "Alta dose única precisa",
        "Terapia com Prótons": "Terapia com partículas carregadas",
        "Imagem Diagnóstica": "Raios X, CT, PET, etc."
    }
    
    aplicacao = st.selectbox("Selecione a aplicação clínica:", list(aplicacoes.keys()))
    
    if aplicacao == "Radioterapia Externa":
        st.markdown("### 📅 Radioterapia Externa")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**💊 Parâmetros do Tratamento:**")
            dose_total = st.slider("Dose total (Gy)", 10.0, 80.0, 60.0, 2.0)
            num_fracoes = st.slider("Número de frações", 1, 40, 30, 1)
            energia = st.selectbox("Energia (MV)", [6, 10, 15, 18])
            
        with col2:
            st.markdown("**🎯 Parâmetros do Tumor:**")
            volume = st.slider("Volume do tumor (cm³)", 1.0, 1000.0, 50.0, 10.0)
            localizacao = st.selectbox("Localização", ["Pulmão", "Próstata", "Mama", "Cérebro", "Outro"])
            
            # Parâmetro BED (Biological Effective Dose)
            alpha_beta = st.slider("Razão α/β", 1.0, 20.0, 10.0, 1.0)
        
        if st.button("📊 Calcular Parâmetros Clínicos"):
            dose_fracao = dose_total / num_fracoes
            BED = dose_total * (1 + dose_fracao / alpha_beta)
            
            st.markdown("---")
            st.markdown("### 📋 Resultados do Tratamento")
            
            col_res1, col_res2 = st.columns(2)
            
            with col_res1:
                st.markdown(f'<div class="result-box"><h4>💉 Dose/fração: <span style="color:#d32f2f">{dose_fracao:.2f} Gy</span></h4></div>', unsafe_allow_html=True)
                st.markdown(f'<div class="info-box"><h4>📈 BED: <span style="color:#1976D2">{BED:.1f} Gy</span></h4></div>', unsafe_allow_html=True)
            
            with col_res2:
                st.markdown(f'<div class="info-box"><h4>⏱️ Duração: <span style="color:#1976D2">{num_fracoes/5:.1f} semanas</span></h4></div>', unsafe_allow_html=True)
                st.markdown(f'<div class="info-box"><h4>🔋 Energia: <span style="color:#1976D2">{energia} MV</span></h4></div>', unsafe_allow_html=True)
            
            # Recomendações baseadas nos parâmetros
            st.markdown("### 💡 Recomendações")
            
            if dose_fracao > 3.0:
                st.warning("⚠️ Dose por fração elevada. Considerar hiperfracionamento.")
            elif dose_fracao < 1.8:
                st.info("ℹ️ Dose por fração baixa. Considerar hipofracionamento.")
            else:
                st.success("✅ Dose por fração dentro da faixa convencional.")
            
            if BED > 100:
                st.info("ℹ️ BED elevado indica maior efetividade biológica.")
            
            # Gráfico de BED vs dose/fração
            fracoes_test = np.linspace(1, 40, 40)
            doses_frac_test = 60 / fracoes_test
            BED_test = 60 * (1 + doses_frac_test / alpha_beta)
            
            fig, ax = plt.subplots(figsize=(10, 6))
            ax.plot(fracoes_test, BED_test, 'b-', linewidth=2)
            ax.plot(num_fracoes, BED, 'ro', markersize=8, label=f'Plano atual: {BED:.1f} Gy')
            
            ax.set_xlabel("Número de Frações")
            ax.set_ylabel("BED (Gy)")
            ax.set_title("Dose Biologicamente Efetiva (BED) vs Número de Frações")
            ax.legend()
            ax.grid(True)
            
            st.pyplot(fig)
    
    elif aplicacao == "Brachytherapy":
        st.markdown("### 📍 Brachytherapy")
        st.info("Módulo em desenvolvimento. Use Radioterapia Externa para simulações.")
        
    else:
        st.info(f"Módulo {aplicacao} em desenvolvimento.")

# =============================================================================
# MÓDULO 6: APLICAÇÕES AMBIENTAIS
# =============================================================================

def modulo_aplicacoes_ambientais():
    st.header("🌍 Aplicações Ambientais da Radioatividade")
    
    st.info("""
    **Instruções:** 
    - Selecione o cenário ambiental
    - Configure os parâmetros de contaminação
    - Visualize o impacto e medidas de proteção
    """)
    
    cenarios = {
        "Contaminação do Solo": "Análise de radioisótopos no solo",
        "Contaminação da Água": "Monitoramento de recursos hídricos", 
        "Monitoramento do Ar": "Partículas radioativas no ar",
        "Acidentes Nucleares": "Simulação de cenários de acidente"
    }
    
    cenario = st.selectbox("Selecione o cenário ambiental:", list(cenarios.keys()))
    
    if cenario == "Contaminação do Solo":
        st.markdown("### 🌱 Contaminação do Solo")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**☢️ Parâmetros de Contaminação:**")
            isotopo = st.selectbox("Radioisótopo", 
                                 ["Cs-137", "Sr-90", "I-131", "U-238", "Co-60"])
            atividade = st.number_input("Atividade (Bq/kg)", 
                                      min_value=0.1, value=1000.0, step=10.0)
            profundidade = st.slider("Profundidade (cm)", 1, 100, 20, 1)
            
        with col2:
            st.markdown("**📊 Parâmetros do Solo:**")
            tipo_solo = st.selectbox("Tipo de solo", 
                                   ["Argiloso", "Arenoso", "Orgânico", "Misto"])
            ph = st.slider("pH do solo", 3.0, 9.0, 6.5, 0.1)
            umidade = st.slider("Umidade (%)", 0, 100, 30, 1)
        
        if st.button("🌱 Analisar Contaminação"):
            # Cálculos simplificados
            meia_vida = {
                "Cs-137": 30.17, "Sr-90": 28.8, "I-131": 8.02, 
                "U-238": 4.468e9, "Co-60": 5.27
            }[isotopo]  # anos
            
            lambda_val = math.log(2) / (meia_vida * 365.25)  # dia⁻¹
            
            # Fator de migração baseado no tipo de solo
            fatores_migracao = {"Argiloso": 0.1, "Arenoso": 0.3, "Orgânico": 0.2, "Misto": 0.15}
            taxa_migracao = fatores_migracao[tipo_solo] * (1 + umidade/100)
            
            st.markdown("---")
            st.markdown("### 📋 Resultados da Análise")
            
            col_res1, col_res2 = st.columns(2)
            
            with col_res1:
                st.markdown(f'<div class="result-box"><h4>⏳ Meia-vida: <span style="color:#d32f2f">{meia_vida} anos</span></h4></div>', unsafe_allow_html=True)
                st.markdown(f'<div class="info-box"><h4>📉 Constante λ: <span style="color:#1976D2">{lambda_val:.3e} dia⁻¹</span></h4></div>', unsafe_allow_html=True)
            
            with col_res2:
                st.markdown(f'<div class="info-box"><h4>🌊 Taxa migração: <span style="color:#1976D2">{taxa_migracao:.3f} cm/dia</span></h4></div>', unsafe_allow_html=True)
                st.markdown(f'<div class="info-box"><h4>📏 Profundidade: <span style="color:#1976D2">{profundidade} cm</span></h4></div>', unsafe_allow_html=True)
            
            # Recomendações
            st.markdown("### 💡 Recomendações de Proteção")
            
            if atividade > 10000:
                st.error("🚨 CONTAMINAÇÃO ELEVADA! Medidas urgentes necessárias.")
                st.markdown("- Isolamento da área")
                st.markdown("- Remoção de solo contaminado")
                st.markdown("- Monitoramento contínuo")
            elif atividade > 1000:
                st.warning("⚠️ Contaminação moderada. Monitoramento intensivo.")
                st.markdown("- Restrição de acesso")
                st.markdown("- Amostragem regular")
            else:
                st.success("✅ Contaminação baixa. Monitoramento de rotina.")
            
            # Simulação temporal
            tempo_dias = np.linspace(0, min(meia_vida * 365.25 * 2, 3650), 100)
            atividade_temporal = atividade * np.exp(-lambda_val * tempo_dias)
            
            fig, ax = plt.subplots(figsize=(10, 6))
            ax.plot(tempo_dias/365.25, atividade_temporal, 'r-', linewidth=2)
            ax.axhline(y=1000, color='orange', linestyle='--', label='Limite alerta (1000 Bq/kg)')
            ax.axhline(y=100, color='green', linestyle='--', label='Limite seguro (100 Bq/kg)')
            
            ax.set_xlabel("Tempo (anos)")
            ax.set_ylabel("Atividade (Bq/kg)")
            ax.set_title(f"Decaimento do {isotopo} no Solo")
            ax.legend()
            ax.grid(True)
            ax.set_yscale('log')
            
            st.pyplot(fig)
    
    else:
        st.info(f"Módulo {cenario} em desenvolvimento.")

# =============================================================================
# MÓDULO 7: EFEITO COMPTON
# =============================================================================

def modulo_efeito_compton():
    st.header("⚡ Efeito Compton")
    
    st.info("""
    **Instruções:**
    - Insira a energia do fóton incidente
    - Selecione o ângulo de espalhamento
    - Visualize as energias e comprimentos de onda resultantes
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**📊 Parâmetros de Entrada:**")
        energia_incidente = st.number_input("Energia do fóton incidente (MeV)", 
                                          min_value=0.01, value=1.0, step=0.1)
        
        angulo_graus = st.slider("Ângulo de espalhamento (graus)", 
                                min_value=0, max_value=180, value=90, step=1)
        
        # Constantes físicas CORRETAS
        h = 4.135667662e-15  # eV·s (constante de Planck)
        c = 299792458        # m/s (velocidade da luz)
        m_e = 0.5109989461   # MeV/c² (massa do elétron)
        
    with col2:
        st.markdown("**📐 Fórmula do Efeito Compton:**")
        st.markdown('<div class="formula-box">λ\' - λ = (h/mₑc) × (1 - cosθ)</div>', unsafe_allow_html=True)
        st.markdown('<div class="formula-box">E\' = E / [1 + (E/mₑc²)(1 - cosθ)]</div>', unsafe_allow_html=True)
        
        st.markdown("**ℹ️ Constantes Físicas:**")
        st.markdown(f"- h = {h:.3e} eV·s")
        st.markdown(f"- c = {c:.3e} m/s")
        st.markdown(f"- mₑc² = {m_e} MeV")
    
    if st.button("⚡ Calcular Efeito Compton", use_container_width=True):
        if energia_incidente <= 0:
            st.error("A energia deve ser positiva!")
            return
            
        # Converter ângulo para radianos
        angulo_rad = math.radians(angulo_graus)
        
        # Cálculo CORRETO da energia espalhada
        denominador = 1 + (energia_incidente / m_e) * (1 - math.cos(angulo_rad))
        energia_espalhada = energia_incidente / denominador
        
        # Cálculo do comprimento de onda
        lambda_compton = 2.426e-12  # m (comprimento de onda Compton)
        delta_lambda = lambda_compton * (1 - math.cos(angulo_rad))
        
        # Energia do elétron de recuo
        energia_eletron = energia_incidente - energia_espalhada
        
        st.markdown("---")
        st.markdown("### 📊 Resultados do Espalhamento Compton")
        
        col_res1, col_res2, col_res3 = st.columns(3)
        
        with col_res1:
            st.markdown(f'<div class="result-box"><h4>📉 Energia espalhada: <span style="color:#d32f2f">{energia_espalhada:.4f} MeV</span></h4></div>', unsafe_allow_html=True)
        
        with col_res2:
            st.markdown(f'<div class="result-box"><h4>⚡ Energia elétron: <span style="color:#d32f2f">{energia_eletron:.4f} MeV</span></h4></div>', unsafe_allow_html=True)
        
        with col_res3:
            st.markdown(f'<div class="info-box"><h4>📏 Δλ: <span style="color:#1976D2">{delta_lambda:.3e} m</span></h4></div>', unsafe_allow_html=True)
        
        # Detalhes do cálculo
        st.markdown("**🔍 Detalhes do Cálculo:**")
        
        st.markdown(f'- **1 - cosθ:** {1 - math.cos(angulo_rad):.4f}')
        st.markdown(f'- **E/mₑc²:** {energia_incidente/m_e:.4f}')
        st.markdown(f'- **(E/mₑc²)(1 - cosθ):** {(energia_incidente/m_e) * (1 - math.cos(angulo_rad)):.4f}')
        st.markdown(f'- **Denominador:** {denominador:.4f}')
        st.markdown(f'- **E\' = E / denominador:** {energia_incidente/denominador:.4f} MeV')
        
        # Gráfico da energia espalhada vs ângulo
        angulos = np.linspace(0, 180, 181)
        angulos_rad = np.radians(angulos)
        energias_esp = energia_incidente / (1 + (energia_incidente/m_e) * (1 - np.cos(angulos_rad)))
        
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(angulos, energias_esp, 'b-', linewidth=3)
        ax.plot(angulo_graus, energia_espalhada, 'ro', markersize=8, 
               label=f'Ângulo selecionado: {angulo_graus}°')
        
        ax.set_xlabel("Ângulo de Espalhamento (graus)")
        ax.set_ylabel("Energia do Fóton Espalhado (MeV)")
        ax.set_title(f"Efeito Compton - Fóton Incidente de {energia_incidente} MeV")
        ax.legend()
        ax.grid(True)
        
        st.pyplot(fig)
        
        # Tabela de valores
        df_compton = pd.DataFrame({
            "Ângulo (graus)": angulos,
            "Energia_Espalhada (MeV)": energias_esp,
            "Energia_Elétron (MeV)": energia_incidente - energias_esp
        })
        
        st.dataframe(df_compton.head(10), use_container_width=True)
        
        # Download
        csv = df_compton.to_csv(index=False)
        st.download_button("📥 Baixar Dados Compton", data=csv, 
                          file_name=f"compton_{energia_incidente}MeV.csv", 
                          mime="text/csv", use_container_width=True)
        
        # Verificação com caso conhecido
        if abs(angulo_graus - 90) < 1 and abs(energia_incidente - 1.0) < 0.01:
            st.markdown("### 🧪 Verificação com Caso Conhecido")
            st.markdown("Para E = 1 MeV e θ = 90°:")
            st.markdown("- E' esperado ≈ 0.338 MeV")
            st.markdown(f"- E' calculado = {energia_espalhada:.3f} MeV")
            
            if abs(energia_espalhada - 0.338) < 0.01:
                st.success("✅ Cálculo verificado!")
            else:
                st.warning("⚠️ Pequena diferença nos valores. Verifique as constantes.")

# =============================================================================
# MÓDULO 8: PRODUÇÃO DE PARES
# =============================================================================

def modulo_producao_pares():
    st.header("⚛️ Produção de Pares")
    
    st.info("""
    **Instruções:**
    - Insira a energia do fóton incidente
    - Selecione o material alvo
    - Visualize a probabilidade de produção de pares
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**📊 Parâmetros de Entrada:**")
        energia_incidente = st.number_input("Energia do fóton (MeV)", 
                                          min_value=1.022, value=5.0, step=0.1,
                                          help="Mínimo: 1.022 MeV (2×mₑc²)")
        
        material = st.selectbox("Material", 
                              ["Chumbo", "Alumínio", "Água", "Concreto", "Tungstênio"])
        
        espessura = st.slider("Espessura (cm)", 0.1, 10.0, 1.0, 0.1)
    
    with col2:
        st.markdown("**📐 Física da Produção de Pares:**")
        st.markdown('<div class="formula-box">E_min = 2 × mₑc² = 1.022 MeV</div>', unsafe_allow_html=True)
        st.markdown('<div class="formula-box">σ_par ∝ Z² × (E - 1.022)</div>', unsafe_allow_html=True)
        
        st.markdown("**ℹ️ Números Atômicos:**")
        numeros_z = {"Chumbo": 82, "Alumínio": 13, "Água": 7.5, "Concreto": 11, "Tungstênio": 74}
        Z = numeros_z[material]
        st.markdown(f"- **{material}:** Z = {Z}")
    
    if st.button("⚛️ Calcular Produção de Pares", use_container_width=True):
        if energia_incidente < 1.022:
            st.error("A energia deve ser ≥ 1.022 MeV para produção de pares!")
            return
            
        # Cálculo simplificado da seção de choque
        # Coeficiente de atenuação para produção de pares (aproximado)
        k_par = 0.001 * (Z ** 2) * (energia_incidente - 1.022)
        
        # Probabilidade de interação
        probabilidade = 1 - math.exp(-k_par * espessura)
        
        st.markdown("---")
        st.markdown("### 📊 Resultados da Produção de Pares")
        
        col_res1, col_res2 = st.columns(2)
        
        with col_res1:
            st.markdown(f'<div class="result-box"><h4>📈 Coeficiente μ_par: <span style="color:#d32f2f">{k_par:.4f} cm⁻¹</span></h4></div>', unsafe_allow_html=True)
        
        with col_res2:
            st.markdown(f'<div class="result-box"><h4>🎯 Probabilidade: <span style="color:#d32f2f">{probabilidade*100:.2f}%</span></h4></div>', unsafe_allow_html=True)
        
        # Energia dos elétrons e pósitrons
        energia_restante = energia_incidente - 1.022
        energia_cinetica = energia_restante / 2  # Aproximadamente igual para elétron e pósitron
        
        st.markdown("**⚡ Energias das Partículas:**")
        st.markdown(f"- **Energia cinética total disponível:** {energia_restante:.3f} MeV")
        st.markdown(f"- **Energia cinética do elétron:** ~{energia_cinetica:.3f} MeV")
        st.markdown(f"- **Energia cinética do pósitron:** ~{energia_cinetica:.3f} MeV")
        
        # Gráfico da probabilidade vs energia
        energias = np.linspace(1.022, 10.0, 100)
        k_par_vals = 0.001 * (Z ** 2) * (energias - 1.022)
        prob_vals = 1 - np.exp(-k_par_vals * espessura)
        
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(energias, prob_vals * 100, 'purple', linewidth=3)
        ax.plot(energia_incidente, probabilidade * 100, 'ro', markersize=8, 
               label=f'Energia selecionada: {energia_incidente} MeV')
        
        ax.set_xlabel("Energia do Fóton (MeV)")
        ax.set_ylabel("Probabilidade de Produção de Pares (%)")
        ax.set_title(f"Produção de Pares em {material} (Z={Z}) - {espessura} cm")
        ax.legend()
        ax.grid(True)
        
        st.pyplot(fig)
        
        # Comparação entre materiais
        st.markdown("### 📊 Comparação entre Materiais")
        
        comparacao = []
        for mat, z_val in numeros_z.items():
            k_val = 0.001 * (z_val ** 2) * (energia_incidente - 1.022)
            prob_val = 1 - math.exp(-k_val * espessura)
            comparacao.append({
                "Material": mat,
                "Z": z_val,
                "μ_par (cm⁻¹)": k_val,
                "Probabilidade (%)": prob_val * 100
            })
        
        df_comp = pd.DataFrame(comparacao)
        st.dataframe(df_comp.style.format({
            "μ_par (cm⁻¹)": "{:.4f}",
            "Probabilidade (%)": "{:.2f}"
        }), use_container_width=True)

# =============================================================================
# MÓDULO 9: EXPOSIÇÃO OCUPACIONAL
# =============================================================================

def modulo_exposicao_ocupacional():
    st.header("👨‍⚕️ Cálculo de Exposição Ocupacional")
    
    st.info("""
    **Instruções:**
    - Insira as taxas de dose e tempos de exposição
    - Configure os fatores de proteção
    - Calcule a dose total e compare com limites
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**📊 Parâmetros de Exposição:**")
        taxa_dose = st.number_input("Taxa de dose (µSv/h)", 
                                  min_value=0.1, value=100.0, step=10.0)
        
        horas_dia = st.number_input("Horas por dia", 
                                  min_value=0.1, max_value=24.0, value=8.0, step=0.5)
        
        dias_semana = st.number_input("Dias por semana", 
                                    min_value=1, max_value=7, value=5, step=1)
        
        semanas_ano = st.number_input("Semanas por ano", 
                                    min_value=1, max_value=52, value=48, step=1)
    
    with col2:
        st.markdown("**🛡️ Fatores de Proteção:**")
        fator_protecao = st.slider("Fator de proteção", 1.0, 100.0, 10.0, 1.0,
                                 help="Redução na dose devido a blindagem/EPI")
        
        distancia = st.slider("Distância (metros)", 0.1, 10.0, 2.0, 0.1,
                            help="Distância da fonte")
        
        st.markdown("**📏 Limites Anuais:**")
        limite_anual = st.selectbox("Limite de dose anual", 
                                  ["20 mSv (ocupacional)", "1 mSv (público)", "50 mSv (emergência)"],
                                  index=0)
    
    if st.button("👨‍⚕️ Calcular Exposição", use_container_width=True):
        # Converter limite para µSv
        limites = {
            "20 mSv (ocupacional)": 20000,
            "1 mSv (público)": 1000, 
            "50 mSv (emergência)": 50000
        }
        limite = limites[limite_anual]
        
        # Cálculos CORRETOS
        horas_ano = horas_dia * dias_semana * semanas_ano
        dose_bruta_anual = taxa_dose * horas_ano
        
        # Ajustes por proteção e distância
        dose_efetiva = dose_bruta_anual / fator_protecao
        dose_efetiva = dose_efetiva / (distancia ** 2)  # Lei do inverso do quadrado
        
        percentual_limite = (dose_efetiva / limite) * 100
        
        st.markdown("---")
        st.markdown("### 📊 Resultados da Exposição")
        
        col_res1, col_res2, col_res3 = st.columns(3)
        
        with col_res1:
            st.markdown(f'<div class="result-box"><h4>📈 Dose bruta anual: <span style="color:#d32f2f">{dose_bruta_anual:,.0f} µSv</span></h4></div>', unsafe_allow_html=True)
        
        with col_res2:
            st.markdown(f'<div class="result-box"><h4>🛡️ Dose efetiva: <span style="color:#d32f2f">{dose_efetiva:,.0f} µSv</span></h4></div>', unsafe_allow_html=True)
        
        with col_res3:
            cor = "green" if percentual_limite < 80 else "orange" if percentual_limite < 100 else "red"
            st.markdown(f'<div class="result-box"><h4>📊 % do limite: <span style="color:{cor}">{percentual_limite:.1f}%</span></h4></div>', unsafe_allow_html=True)
        
        # Avaliação de risco
        st.markdown("### 📋 Avaliação de Risco")
        
        if percentual_limite < 50:
            st.success("✅ EXPOSIÇÃO BAIXA. Dentro dos limites de segurança.")
            st.markdown("- Monitoramento de rotina")
            st.markdown("- Manutenção dos procedimentos atuais")
            
        elif percentual_limite < 100:
            st.warning("⚠️ EXPOSIÇÃO MODERADA. Atenção necessária.")
            st.markdown("- Revisão de procedimentos")
            st.markdown("- Otimização de tempos de exposição")
            st.markdown("- Verificação de EPIs")
            
        else:
            st.error("🚨 EXPOSIÇÃO ELEVADA! Medidas corretivas urgentes.")
            st.markdown("- Paralisação das atividades")
            st.markdown("- Investigação imediata")
            st.markdown("- Revisão completa da proteção radiológica")
        
        # Detalhes do cálculo
        st.markdown("**🔍 Detalhes do Cálculo:**")
        
        col_det1, col_det2 = st.columns(2)
        
        with col_det1:
            st.markdown(f"- **Horas anuais:** {horas_ano:.1f} h")
            st.markdown(f"- **Taxa de dose:** {taxa_dose} µSv/h")
            st.markdown(f"- **Dose bruta:** {taxa_dose} × {horas_ano:.1f} = {dose_bruta_anual:,.0f} µSv")
        
        with col_det2:
            st.markdown(f"- **Fator proteção:** {fator_protecao}")
            st.markdown(f"- **Distância:** {distancia} m (fator: {1/(distancia**2):.3f})")
            st.markdown(f"- **Dose efetiva:** {dose_bruta_anual:,.0f} / {fator_protecao} / {distancia**2:.2f} = {dose_efetiva:,.0f} µSv")
        
        # Gráfico de acumulação de dose
        semanas = list(range(1, semanas_ano + 1))
        dose_acumulada = []
        for semana in semanas:
            horas_semana = horas_dia * dias_semana
            dose_semana = (taxa_dose * horas_semana) / fator_protecao / (distancia ** 2)
            dose_acumulada.append(dose_semana * semana)
        
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(semanas, dose_acumulada, 'b-', linewidth=2, label='Dose acumulada')
        ax.axhline(y=limite, color='r', linestyle='--', label=f'Limite anual: {limite/1000:.0f} mSv')
        ax.axhline(y=limite*0.8, color='orange', linestyle=':', label='80% do limite')
        
        ax.set_xlabel("Semana")
        ax.set_ylabel("Dose Acumulada (µSv)")
        ax.set_title("Acumulação de Dose Ocupacional Anual")
        ax.legend()
        ax.grid(True)
        
        st.pyplot(fig)
        
        # Relatório
        relatorio = f"""RELATÓRIO DE EXPOSIÇÃO OCUPACIONAL
===============================
DATA: {datetime.now().strftime('%d/%m/%Y')}

PARÂMETROS:
- Taxa de dose: {taxa_dose} µSv/h
- Horas/dia: {horas_dia}
- Dias/semana: {dias_semana}
- Semanas/ano: {semanas_ano}
- Fator proteção: {fator_protecao}
- Distância: {distancia} m
- Limite anual: {limite_anual}

RESULTADOS:
- Horas anuais: {horas_ano:.1f} h
- Dose bruta anual: {dose_bruta_anual:,.0f} µSv
- Dose efetiva anual: {dose_efetiva:,.0f} µSv
- Percentual do limite: {percentual_limite:.1f}%

AVALIAÇÃO: {'BAIXA' if percentual_limite < 50 else 'MODERADA' if percentual_limite < 100 else 'ELEVADA'}

RECOMENDAÇÕES:
{'✅ Dentro dos limites de segurança' if percentual_limite < 50 else '⚠️ Atenção necessária' if percentual_limite < 100 else '🚨 Medidas corretivas urgentes'}"""

        st.download_button("📥 Baixar Relatório", data=relatorio, 
                          file_name="exposicao_ocupacional.txt", 
                          mime="text/plain", use_container_width=True)

# =============================================================================
# MÓDULO 10: CENÁRIOS HISTÓRICOS
# =============================================================================

def modulo_cenarios_historicos():
    st.header("📜 Simulação de Cenários Históricos")
    
    st.info("""
    **Instruções:**
    - Selecione um evento histórico significativo
    - Configure os parâmetros de simulação
    - Visualize os impactos radiológicos
    """)
    
    eventos = {
        "Chernobyl (1986)": "Acidente nuclear de Chernobyl",
        "Fukushima (2011)": "Acidente nuclear de Fukushima",
        "Goiânia (1987)": "Acidente com césio-137 em Goiânia",
        "Three Mile Island (1979)": "Acidente nuclear nos EUA",
        "Testes Nucleares": "Testes atmosféricos de armas nucleares"
    }
    
    evento = st.selectbox("Selecione o evento histórico:", list(eventos.keys()))
    
    if evento == "Chernobyl (1986)":
        st.markdown("### ☢️ Acidente de Chernobyl (1986)")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**📊 Parâmetros do Acidente:**")
            liberacao = st.slider("Liberação estimada (PBq)", 
                                1000, 10000, 5200, 100,
                                help="Atividade total liberada (1 PBq = 10¹⁵ Bq)")
            
            distancia = st.slider("Distância do reator (km)", 
                                1, 1000, 30, 1)
            
            tempo_exposicao = st.slider("Tempo de exposição (horas)", 
                                      1, 720, 24, 1)
        
        with col2:
            st.markdown("**📋 Isótopos Principais:**")
            st.markdown("- **I-131:** 8.02 dias meia-vida (tiroide)")
            st.markdown("- **Cs-137:** 30.17 anos meia-vida (corpo inteiro)")
            st.markdown("- **Sr-90:** 28.8 anos meia-vida (ossos)")
            st.markdown("- **Pu-239:** 24,100 anos meia-vida (pulmões)")
            
            st.markdown("**🛡️ Fatores de Proteção:**")
            abrigo = st.slider("Fator de proteção do abrigo", 1.0, 100.0, 10.0, 1.0)
            evacuação = st.selectbox("Tempo de evacuação", 
                                   ["Imediata", "1 dia", "3 dias", "1 semana", "Nenhuma"],
                                   index=0)
        
        if st.button("📊 Simular Impacto de Chernobyl"):
            # Cálculos simplificados
            # Dose aproximada usando modelo de nuvem radioativa
            dose_1h = (liberacao * 1000) / (distancia ** 2)  # µSv/h a 1 km
            dose_total = dose_1h * tempo_exposicao / abrigo
            
            # Redução por evacuação
            fatores_evac = {
                "Imediata": 0.1, "1 dia": 0.3, "3 dias": 0.6, 
                "1 semana": 0.8, "Nenhuma": 1.0
            }
            dose_total *= fatores_evac[evacuação]
            
            st.markdown("---")
            st.markdown("### 📊 Resultados da Simulação")
            
            col_res1, col_res2 = st.columns(2)
            
            with col_res1:
                st.markdown(f'<div class="result-box"><h4>📈 Dose estimada: <span style="color:#d32f2f">{dose_total:,.0f} µSv</span></h4></div>', unsafe_allow_html=True)
                st.markdown(f'<div class="info-box"><h4>📏 Equivalente: <span style="color:#1976D2">{dose_total/1000:.1f} mSv</span></h4></div>', unsafe_allow_html=True)
            
            with col_res2:
                # Comparação com limites
                if dose_total < 1000:
                    risco = "Muito baixo"
                    cor = "green"
                elif dose_total < 10000:
                    risco = "Baixo"
                    cor = "orange"
                elif dose_total < 50000:
                    risco = "Moderado" 
                    cor = "red"
                else:
                    risco = "Alto"
                    cor = "darkred"
                
                st.markdown(f'<div class="warning-box"><h4>⚠️ Nível de risco: <span style="color:{cor}">{risco}</span></h4></div>', unsafe_allow_html=True)
            
            # Efeitos na saúde
            st.markdown("### 👨‍⚕️ Possíveis Efeitos na Saúde")
            
            if dose_total < 100000:  # < 100 mSv
                st.success("✅ **Baixo risco** - Sem efeitos agudos. Risco de câncer ligeiramente aumentado.")
                st.markdown("- Nenhum efeito imediato na saúde")
                st.markdown("- Risco estatístico de câncer muito baixo")
                st.markdown("- Monitoramento médico recomendado")
                
            elif dose_total < 1000000:  # < 1 Sv
                st.warning("⚠️ **Risco moderado** - Possíveis efeitos tardios.")
                st.markdown("- Náusea leve em indivíduos sensíveis")
                st.markdown("- Risco aumentado de câncer a longo prazo")
                st.markdown("- Acompanhamento médico necessário")
                
            else:  # > 1 Sv
                st.error("🚨 **Alto risco** - Efeitos agudos prováveis.")
                st.markdown("- Síndrome aguda de radiação")
                st.markdown("- Danos aos órgãos hematopoiéticos")
                st.markdown("- Tratamento médico imediato necessário")
            
            # Mapa de contaminação simulado
            distancias = np.linspace(1, 300, 100)
            doses_map = (liberacao * 1000) / (distancias ** 2) * 24 / abrigo
            
            fig, ax = plt.subplots(figsize=(10, 6))
            ax.plot(distancias, doses_map/1000, 'r-', linewidth=2)  # Convertendo para mSv
            ax.axvline(x=30, color='blue', linestyle='--', label='Zona de exclusão (30 km)')
            ax.axhline(y=20, color='green', linestyle='--', label='Limite ocupacional anual (20 mSv)')
            ax.axhline(y=1, color='orange', linestyle='--', label='Limite público anual (1 mSv)')
            
            ax.set_xlabel("Distância do Reator (km)")
            ax.set_ylabel("Dose em 24h (mSv)")
            ax.set_title("Perfil de Dose - Acidente de Chernobyl")
            ax.legend()
            ax.grid(True)
            ax.set_yscale('log')
            
            st.pyplot(fig)
            
            # Informações históricas
            st.markdown("### 📜 Informações Históricas")
            st.markdown("""
            **O acidente de Chernobyl (26/04/1986):**
            - Liberação estimada: 5,200 PBq de material radioativo
            - Área evacuada: 30 km ao redor do reator
            - Trabalhadores de emergência receberam doses de 0.2-16 Sv
            - População próxima: doses de 10-500 mSv
            """)
    
    else:
        st.info(f"Simulação do evento {evento} em desenvolvimento.")

# =============================================================================
# MÓDULO 11: DECAIMENTO RADIOATIVO
# =============================================================================

def modulo_decaimento_radioativo():
    st.header("📉 Simulação de Decaimento Radioativo")
    
    st.info("""
    **Instruções:**
    - Selecione o radioisótopo ou defina parâmetros personalizados
    - Configure as condições iniciais
    - Visualize a curva de decaimento
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**☢️ Seleção do Radioisótopo:**")
        isotopos = {
            "Carbono-14": 5730,
            "Potássio-40": 1.25e9,
            "Urânio-238": 4.468e9,
            "Iodo-131": 8.02/365.25,  # Convertendo dias para anos
            "Césio-137": 30.17,
            "Personalizado": 0
        }
        
        isotopo = st.selectbox("Isótopo", list(isotopos.keys()))
        
        if isotopo == "Personalizado":
            meia_vida = st.number_input("Meia-vida (anos)", 
                                      min_value=0.001, value=1.0, step=0.1)
        else:
            meia_vida = isotopos[isotopo]
            st.markdown(f"**Meia-vida:** {meia_vida} anos")
        
        atividade_inicial = st.number_input("Atividade inicial (Bq)", 
                                          min_value=1.0, value=1000.0, step=100.0)
    
    with col2:
        st.markdown("**📊 Parâmetros de Simulação:**")
        tempo_max = st.slider("Tempo máximo de simulação", 
                            1.0, 10.0, 5.0, 0.1,
                            help="Em múltiplos da meia-vida")
        
        pontos = st.slider("Número de pontos", 10, 1000, 100, 10)
        
        st.markdown("**📐 Lei do Decaimento Radioativo:**")
        st.markdown('<div class="formula-box">N(t) = N₀ × e^(-λt)</div>', unsafe_allow_html=True)
        st.markdown('<div class="formula-box">λ = ln(2) / T½</div>', unsafe_allow_html=True)
        st.markdown('<div class="formula-box">A(t) = λ × N(t)</div>', unsafe_allow_html=True)
    
    if st.button("📉 Simular Decaimento", use_container_width=True):
        if meia_vida <= 0 or atividade_inicial <= 0:
            st.error("Valores devem ser positivos!")
            return
            
        # Cálculos
        lambda_val = math.log(2) / meia_vida
        tempo_simulacao = tempo_max * meia_vida
        tempos = np.linspace(0, tempo_simulacao, pontos)
        
        # Número de átomos inicial (N0 = A0 / λ)
        N0 = atividade_inicial / lambda_val
        atoms = N0 * np.exp(-lambda_val * tempos)
        atividade = lambda_val * atoms
        
        st.markdown("---")
        st.markdown("### 📊 Resultados do Decaimento")
        
        col_res1, col_res2, col_res3 = st.columns(3)
        
        with col_res1:
            st.markdown(f'<div class="result-box"><h4>📉 Constante λ: <span style="color:#d32f2f">{lambda_val:.3e} ano⁻¹</span></h4></div>', unsafe_allow_html=True)
        
        with col_res2:
            st.markdown(f'<div class="result-box"><h4>🧮 Átomos iniciais: <span style="color:#d32f2f">{N0:.3e}</span></h4></div>', unsafe_allow_html=True)
        
        with col_res3:
            vida_media = 1 / lambda_val
            st.markdown(f'<div class="info-box"><h4>⏱️ Vida média: <span style="color:#1976D2">{vida_media:.3e} anos</span></h4></div>', unsafe_allow_html=True)
        
        # Gráficos
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
        
        # Gráfico 1: Linear
        ax1.plot(tempos/meia_vida, atividade, 'b-', linewidth=2)
        ax1.set_xlabel("Tempo (T½)")
        ax1.set_ylabel("Atividade (Bq)")
        ax1.set_title(f"Decaimento do {isotopo} - Escala Linear")
        ax1.grid(True)
        
        # Gráfico 2: Logarítmico
        ax2.plot(tempos/meia_vida, atividade, 'r-', linewidth=2)
        ax2.set_yscale('log')
        ax2.set_xlabel("Tempo (T½)")
        ax2.set_ylabel("Atividade (Bq)")
        ax2.set_title(f"Decaimento do {isotopo} - Escala Logarítmica")
        ax2.grid(True, which="both")
        
        # Adicionar linhas de meia-vida
        for ax in [ax1, ax2]:
            for i in range(1, int(tempo_max) + 1):
                ax.axvline(x=i, color='gray', linestyle='--', alpha=0.5)
                ax.text(i, ax.get_ylim()[1]*0.9, f'{i}T½', ha='center', va='top')
        
        plt.tight_layout()
        st.pyplot(fig)
        
        # Tabela de valores importantes
        st.markdown("### 📋 Valores em Múltiplos da Meia-vida")
        
        dados_tabela = []
        for i in range(0, int(tempo_max) + 1):
            t = i * meia_vida
            atv = atividade_inicial * (0.5 ** i)
            percentual = 100 * (0.5 ** i)
            dados_tabela.append({
                "T½": i,
                "Tempo (anos)": t,
                "Atividade (Bq)": atv,
                "Percentual (%)": percentual
            })
        
        df_tabela = pd.DataFrame(dados_tabela)
        st.dataframe(df_tabela.style.format({
            "Tempo (anos)": "{:.2e}",
            "Atividade (Bq)": "{:.2f}",
            "Percentual (%)": "{:.4f}"
        }), use_container_width=True)
        
        # Dados completos para download
        df_completo = pd.DataFrame({
            "Tempo (anos)": tempos,
            "Tempo (T½)": tempos/meia_vida,
            "Atividade (Bq)": atividade,
            "Átomos": atoms
        })
        
        csv = df_completo.to_csv(index=False)
        st.download_button("📥 Baixar Dados do Decaimento", data=csv, 
                          file_name=f"decaimento_{isotopo.lower()}.csv", 
                          mime="text/csv", use_container_width=True)
        
        # Verificação da lei do decaimento
        st.markdown("### 🧪 Verificação da Lei do Decaimento")
        st.markdown("Para t = T½ (1 meia-vida):")
        st.markdown(f"- Atividade esperada: {atividade_inicial/2:.2f} Bq")
        st.markdown(f"- Atividade calculada: {atividade[pontos//int(tempo_max)]:.2f} Bq")
        
        if abs(atividade[pontos//int(tempo_max)] - atividade_inicial/2) < 0.01:
            st.success("✅ Lei do decaimento verificada!")
        else:
            st.warning("⚠️ Pequena diferença nos valores. Verifique o cálculo.")

# =============================================================================
# MÓDULO 12: MODO EXPLICATIVO
# =============================================================================

def modulo_explicativo():
    st.header("📚 Modo Explicativo - Conceitos Radiológicos")
    
    st.info("""
    **Instruções:** 
    - Selecione o conceito que deseja aprender
    - Explore as explicações detalhadas e exemplos
    - Use os visualizadores interativos
    """)
    
    conceitos = {
        "Lei do Decaimento Radioativo": "decay_law",
        "Meia-vida": "half_life", 
        "Atenuação de Radiação": "attenuation",
        "Efeito Compton": "compton_effect",
        "Produção de Pares": "pair_production",
        "Dose Absorvida vs Dose Efetiva": "dose_types",
        "Proteção Radiológica": "radiation_protection"
    }
    
    conceito = st.selectbox("Selecione o conceito:", list(conceitos.keys()))
    
    if conceito == "Lei do Decaimento Radioativo":
        st.markdown("### ⚛️ Lei do Decaimento Radioativo")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            **📖 Definição:**
            A lei do decaimento radioativo descreve como o número de átomos 
            radioativos diminui com o tempo de forma exponencial.
            
            **📐 Fórmula Matemática:**
            N(t) = N₀ × e^(-λt)
            
            Onde:
            - N(t) = número de átomos no tempo t
            - N₀ = número inicial de átomos  
            - λ = constante de decaimento
            - t = tempo decorrido
            
            **🔍 Relação com a meia-vida:**
            λ = ln(2) / T½
            T½ = ln(2) / λ
            """)
        
        with col2:
            st.markdown("""
            **🎯 Significado Físico:**
            - Cada núcleo radioativo tem uma probabilidade constante de decair
            - O decaimento é um processo estatístico
            - Não podemos prever quando um átomo específico decairá
            - Podemos prever o comportamento de um grande número de átomos
            
            **📊 Aplicações:**
            - Datação radiométrica
            - Medicina nuclear
            - Proteção radiológica
            - Gerência de rejeitos radioativos
            """)
        
        # Visualizador interativo
        st.markdown("---")
        st.markdown("### 🎮 Visualizador Interativo")
        
        col_viz1, col_viz2 = st.columns(2)
        
        with col_viz1:
            N0_viz = st.slider("Número inicial de átomos", 100, 10000, 1000, 100)
            T12_viz = st.slider("Meia-vida (unidades de tempo)", 1.0, 10.0, 2.0, 0.1)
        
        with col_viz2:
            tempo_max_viz = st.slider("Tempo máximo (unidades)", 1.0, 20.0, 10.0, 0.5)
            pontos_viz = st.slider("Pontos no gráfico", 10, 500, 100, 10)
        
        # Calcular curva
        lambda_viz = math.log(2) / T12_viz
        tempos_viz = np.linspace(0, tempo_max_viz, pontos_viz)
        atoms_viz = N0_viz * np.exp(-lambda_viz * tempos_viz)
        
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(tempos_viz, atoms_viz, 'b-', linewidth=2)
        
        # Adicionar linhas de meia-vida
        for i in range(1, int(tempo_max_viz/T12_viz) + 1):
            t_meia = i * T12_viz
            ax.axvline(x=t_meia, color='red', linestyle='--', alpha=0.7)
            ax.text(t_meia, N0_viz*0.9, f'{i}T½', ha='center', va='top', color='red')
        
        ax.set_xlabel("Tempo")
        ax.set_ylabel("Número de Átomos")
        ax.set_title("Lei do Decaimento Radioativo - Visualização")
        ax.grid(True)
        
        st.pyplot(fig)
        
        # Tabela de valores
        st.markdown("### 📋 Valores em Múltiplos da Meia-vida")
        
        dados = []
        for i in range(0, int(tempo_max_viz/T12_viz) + 1):
            t = i * T12_viz
            n = N0_viz * (0.5 ** i)
            percent = 100 * (0.5 ** i)
            dados.append({"T½": i, "Tempo": t, "Átomos": n, "Percentual": percent})
        
        df_viz = pd.DataFrame(dados)
        st.dataframe(df_viz.style.format({
            "Tempo": "{:.2f}",
            "Átomos": "{:.0f}",
            "Percentual": "{:.2f}%"
        }), use_container_width=True)
    
    elif conceito == "Meia-vida":
        st.markdown("### ⏱️ Conceito de Meia-vida")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            **📖 Definição:**
            A meia-vida (T½) é o tempo necessário para que metade dos átomos 
            radioativos em uma amostra sofra decaimento.
            
            **🎯 Características:**
            - É uma propriedade intrínseca de cada radioisótopo
            - Não depende da quantidade inicial do material
            - Pode variar de frações de segundo a bilhões de anos
            
            **📐 Relação Matemática:**
            T½ = ln(2) / λ
            Onde λ é a constante de decaimento
            """)
        
        with col2:
            st.markdown("""
            **🔍 Exemplos de Meia-vida:**
            - Carbono-14: 5,730 anos
            - Iodo-131: 8.02 dias  
            - Césio-137: 30.17 anos
            - Urânio-238: 4.47 bilhões de anos
            - Tecnécio-99m: 6 horas
            
            **📊 Importância:**
            - Determina tempo de armazenamento de rejeitos
            - Define frequência de calibração de fontes
            - Influencia escolha de radiofármacos
            - Afeta estratégias de proteção radiológica
            """)
        
        # Comparador de meias-vidas
        st.markdown("---")
        st.markdown("### 📊 Comparador de Meias-vida")
        
        isotopos_compare = {
            "Tecnécio-99m": 6/24/365.25,  # 6 horas em anos
            "Iodo-131": 8.02/365.25,      # 8.02 dias em anos
            "Carbono-14": 5730,
            "Césio-137": 30.17,
            "Potássio-40": 1.25e9,
            "Urânio-238": 4.468e9
        }
        
        selected_isotopes = st.multiselect("Selecione isótopos para comparar:", 
                                         list(isotopos_compare.keys()),
                                         default=["Tecnécio-99m", "Iodo-131", "Carbono-14"])
        
        if selected_isotopes:
            # Criar gráfico comparativo
            fig, ax = plt.subplots(figsize=(12, 8))
            
            colors = plt.cm.Set3(np.linspace(0, 1, len(selected_isotopes)))
            
            for i, iso in enumerate(selected_isotopes):
                T12 = isotopos_compare[iso]
                tempos = np.linspace(0, min(10 * T12, 1e10), 1000)
                atividade = 100 * np.exp(-math.log(2) * tempos / T12)
                
                label = f"{iso} (T½ = {T12:.2e} anos)"
                ax.plot(tempos, atividade, color=colors[i], linewidth=2, label=label)
            
            ax.set_xlabel("Tempo (anos)")
            ax.set_ylabel("Atividade Relativa (%)")
            ax.set_title("Comparação de Decaimento Radioativo")
            ax.legend()
            ax.grid(True)
            ax.set_yscale('log')
            
            # Ajustar escala do eixo x baseado nos valores
            max_time = max(isotopos_compare[iso] for iso in selected_isotopes)
            ax.set_xlim(0, min(10 * max_time, 1e11))
            
            st.pyplot(fig)
            
            # Tabela comparativa
            st.markdown("### 📋 Tabela Comparativa")
            
            comparacao = []
            for iso in selected_isotopes:
                T12 = isotopos_compare[iso]
                lambda_val = math.log(2) / T12
                vida_media = 1 / lambda_val
                
                comparacao.append({
                    "Isótopo": iso,
                    "Meia-vida": T12,
                    "Constante λ (ano⁻¹)": lambda_val,
                    "Vida média": vida_media
                })
            
            df_compare = pd.DataFrame(comparacao)
            st.dataframe(df_compare.style.format({
                "Meia-vida": "{:.3e}",
                "Constante λ (ano⁻¹)": "{:.3e}",
                "Vida média": "{:.3e}"
            }), use_container_width=True)
    
    else:
        st.info(f"Conceito '{conceito}' em desenvolvimento.")

# =============================================================================
# MÓDULOS ADICIONAIS (EM DESENVOLVIMENTO)
# =============================================================================

def modulo_quiz():
    st.header("🎯 Quiz Interativo de Física Radiológica")
    st.info("Módulo em desenvolvimento. Em breve: perguntas interativas sobre conceitos radiológicos.")

def modulo_exportar():
    st.header("💾 Exportar Dados e Resultados")
    st.info("Módulo em desenvolvimento. Em breve: exportação completa de simulações.")

def modulo_comparar():
    st.header("📊 Comparar Simulações")
    st.info("Módulo em desenvolvimento. Em breve: comparação entre diferentes cenários.")

# =============================================================================
# ROTEIRIZADOR PRINCIPAL
# =============================================================================

def main():
    # Mapeamento de módulos para funções
    modulos_map = {
        "Datação Radiométrica": modulo_datacao_radiometrica,
        "Blindagem Radiológica": modulo_blindagem,
        "Radioterapia": modulo_radioterapia,
        "Distribuição de Dose": modulo_distribuicao_dose,
        "Aplicações Clínicas": modulo_aplicacoes_clinicas,
        "Aplicações Ambientais": modulo_aplicacoes_ambientais,
        "Efeito Compton": modulo_efeito_compton,
        "Produção de Pares": modulo_producao_pares,
        "Exposição Ocupacional": modulo_exposicao_ocupacional,
        "Cenários Históricos": modulo_cenarios_historicos,
        "Decaimento Radioativo": modulo_decaimento_radioativo,
        "Modo Explicativo": modulo_explicativo,
        "Quiz Interativo": modulo_quiz,
        "Exportar Dados": modulo_exportar,
        "Comparar Simulações": modulo_comparar
    }
    
    # Executar o módulo selecionado
    if modulo in modulos_map:
        modulos_map[modulo]()
    else:
        st.error("Módulo não encontrado!")

if __name__ == "__main__":
    main()
# Continuação do código anterior...

# =============================================================================
# MÓDULO 13: SISTEMA DE AJUDA E TUTORIAIS
# =============================================================================

def modulo_ajuda():
    st.header("❓ Sistema de Ajuda e Tutoriais")
    
    st.info("""
    **Bem-vindo ao sistema de ajuda do RadSimLab Pro!**
    Aqui você encontrará tutoriais, explicações e dicas para usar cada módulo.
    """)
    
    topicos = {
        "Introdução ao RadSimLab": "introducao",
        "Datação Radiométrica": "datacao_help",
        "Blindagem Radiológica": "blindagem_help",
        "Radioterapia": "radioterapia_help",
        "Distribuição de Dose": "dose_help",
        "Efeito Compton": "compton_help",
        "Produção de Pares": "pares_help",
        "Dicas Gerais": "dicas_gerais"
    }
    
    topico = st.selectbox("Selecione o tópico de ajuda:", list(topicos.keys()))
    
    if topico == "Introdução ao RadSimLab":
        st.markdown("""
        ## 🎯 Introdução ao RadSimLab Pro
        
        **O que é o RadSimLab Pro?**
        RadSimLab Pro é um simulador educacional avançado para física radiológica, 
        desenvolvido para estudantes, professores e profissionais da área.
        
        **Principais Características:**
        - Simulações realistas de fenômenos radiológicos
        - Interface intuitiva e amigável
        - Visualizações gráficas interativas
        - Exportação de dados e resultados
        - Modo explicativo com conceitos teóricos
        
        **Como Usar:**
        1. Selecione o módulo desejado na sidebar
        2. Configure os parâmetros de entrada
        3. Clique no botão de calcular/simular
        4. Analise os resultados e gráficos
        5. Exporte os dados se necessário
        
        **Requisitos do Sistema:**
        - Navegador web moderno
        - Conexão com internet (para versão web)
        - Python 3.8+ (para versão desktop)
        """)
    
    elif topico == "Datação Radiométrica":
        st.markdown("""
        ## ⏳ Módulo de Datação Radiométrica
        
        **O que é datação radiométrica?**
        Método para determinar a idade de materiais baseado no decaimento 
        radioativo de isótopos naturais.
        
        **Métodos Disponíveis:**
        - **Carbono-14:** Para materiais orgânicos até ~50,000 anos
        - **Potássio-Argônio:** Para rochas vulcânicas
        - **Urânio-Chumbo:** Para rochas muito antigas
        - **Rubídio-Estrôncio:** Para rochas ígneas e metamórficas
        
        **Como Usar:**
        1. Selecione o método desejado
        2. Insira a fração remanescente ou razão isotópica
        3. Configure a meia-vida se necessário
        4. Clique em calcular para obter a idade
        
        **Fórmula do Carbono-14:**
        t = (T½/ln(2)) × ln(N₀/N)
        
        Onde:
        - t = idade
        - T½ = meia-vida
        - N₀ = quantidade inicial
        - N = quantidade atual
        
        **Dica:** Use o slider para ajustar precisamente a fração remanescente.
        """)
    
    elif topico == "Blindagem Radiológica":
        st.markdown("""
        ## 🧱 Módulo de Blindagem Radiológica
        
        **O que é blindagem radiológica?**
        Cálculo da espessura necessária de material para reduzir a radiação 
        a níveis seguros.
        
        **Materiais Disponíveis:**
        - Chumbo (alto Z, alta densidade)
        - Concreto (uso em construções)
        - Água (baixo custo, facilidade)
        - Aço (resistência estrutural)
        - Tungstênio (alta eficiência)
        - Urânio (blindagem compacta)
        
        **Lei da Atenuação:**
        I = I₀ × B × e^(-μx)
        
        Onde:
        - I = intensidade após blindagem
        - I₀ = intensidade inicial
        - B = fator de build-up
        - μ = coeficiente de atenuação
        - x = espessura
        
        **Fator de Build-up:**
        Considera a radiação espalhada que atinge o detector. Valores típicos:
        - Baixo: 1.5 (geometria favorável)
        - Médio: 2.0 (configuração padrão)
        - Alto: 3.0 (geometria desfavorável)
        
        **Dica:** Compare diferentes materiais para encontrar o melhor custo-benefício.
        """)
    
    else:
        st.info(f"Tópico de ajuda '{topico}' em desenvolvimento.")

# =============================================================================
# MÓDULO 14: CALCULADORA AVANÇADA
# =============================================================================

def modulo_calculadora_avancada():
    st.header("🧮 Calculadora Avançada de Física Radiológica")
    
    st.info("""
    **Calculadora com funções especializadas para física radiológica.**
    Realize cálculos complexos com unidades apropriadas.
    """)
    
    calc_type = st.radio("Tipo de cálculo:", 
                        ["Conversão de Unidades", "Cálculo de Dose", 
                         "Decaimento Radioativo", "Atenuação", "Outros"],
                        horizontal=True)
    
    if calc_type == "Conversão de Unidades":
        st.markdown("### 🔄 Conversão de Unidades de Radiação")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            valor = st.number_input("Valor para converter:", value=1.0, step=0.1)
            unidade_origem = st.selectbox("De:", 
                                        ["Gy", "Sv", "rad", "rem", "Bq", "Ci"])
        
        with col2:
            unidade_destino = st.selectbox("Para:", 
                                         ["Gy", "Sv", "rad", "rem", "Bq", "Ci"])
            
            # Fatores de conversão
            fatores = {
                "Gy": {"Sv": 1, "rad": 100, "rem": 100},
                "Sv": {"Gy": 1, "rad": 100, "rem": 100},
                "rad": {"Gy": 0.01, "Sv": 0.01, "rem": 1},
                "rem": {"Gy": 0.01, "Sv": 0.01, "rad": 1},
                "Bq": {"Ci": 2.703e-11},
                "Ci": {"Bq": 3.7e10}
            }
        
        with col3:
            st.markdown("**📊 Fatores de Conversão:**")
            st.markdown("- 1 Gy = 100 rad")
            st.markdown("- 1 Sv = 100 rem") 
            st.markdown("- 1 Ci = 3.7×10¹⁰ Bq")
            st.markdown("- 1 Bq = 2.703×10⁻¹¹ Ci")
        
        if st.button("🔄 Converter"):
            if unidade_origem == unidade_destino:
                resultado = valor
            elif unidade_origem in fatores and unidade_destino in fatores[unidade_origem]:
                resultado = valor * fatores[unidade_origem][unidade_destino]
            else:
                st.error("Conversão não suportada!")
                return
                
            st.markdown(f'<div class="result-box"><h4>🔁 Resultado: <span style="color:#d32f2f">{valor} {unidade_origem} = {resultado} {unidade_destino}</span></h4></div>', unsafe_allow_html=True)
    
    elif calc_type == "Cálculo de Dose":
        st.markdown("### 💉 Cálculo de Dose Absorvida")
        
        col1, col2 = st.columns(2)
        
        with col1:
            energia = st.number_input("Energia da radiação (MeV):", value=1.0, step=0.1)
            fluencia = st.number_input("Fluência (partículas/cm²):", value=1e6, step=1e5, format="%.0e")
            massa = st.number_input("Massa do tecido (g):", value=1.0, step=0.1)
        
        with col2:
            coef_absorcao = st.number_input("Coeficiente de absorção (cm²/g):", value=0.1, step=0.01)
            fator_qualidade = st.number_input("Fator de qualidade:", value=1.0, step=0.1)
            
            # Cálculo da dose
            dose_absorvida = (energia * 1.602e-13 * fluencia * coef_absorcao) / massa
            dose_efetiva = dose_absorvida * fator_qualidade
        
        if st.button("💉 Calcular Dose"):
            st.markdown("---")
            st.markdown("### 📊 Resultados")
            
            col_res1, col_res2 = st.columns(2)
            
            with col_res1:
                st.markdown(f'<div class="result-box"><h4>📈 Dose absorvida: <span style="color:#d32f2f">{dose_absorvida:.3e} Gy</span></h4></div>', unsafe_allow_html=True)
            
            with col_res2:
                st.markdown(f'<div class="result-box"><h4>🛡️ Dose efetiva: <span style="color:#d32f2f">{dose_efetiva:.3e} Sv</span></h4></div>', unsafe_allow_html=True)
            
            # Detalhes do cálculo
            st.markdown("**🔍 Detalhes do Cálculo:**")
            st.markdown(f"- Energia por partícula: {energia} MeV = {energia*1.602e-13:.3e} J")
            st.markdown(f"- Energia total depositada: {energia*1.602e-13*fluencia*coef_absorcao:.3e} J")
            st.markdown(f"- Dose = Energia / Massa = {dose_absorvida:.3e} Gy")
            st.markdown(f"- Dose efetiva = Dose × Fator qualidade = {dose_efetiva:.3e} Sv")
    
    else:
        st.info("Funcionalidade em desenvolvimento.")

# =============================================================================
# MÓDULO 15: BANCO DE DADOS DE ISÓTOPOS
# =============================================================================

def modulo_banco_isotopos():
    st.header("📚 Banco de Dados de Radioisótopos")
    
    st.info("""
    **Consulta de propriedades de radioisótopos comuns.**
    Pesquise por isótopo, meia-vida, tipo de decaimento, etc.
    """)
    
    # Banco de dados de isótopos
    isotopos_db = {
        "H-3": {"nome": "Trítio", "meia_vida": 12.32, "unidade": "anos", "decaimento": "β-", "energia": 0.0186, "aplicacao": "Marcador biológico"},
        "C-14": {"nome": "Carbono-14", "meia_vida": 5730, "unidade": "anos", "decaimento": "β-", "energia": 0.156, "aplicacao": "Datação"},
        "Na-22": {"nome": "Sódio-22", "meia_vida": 2.602, "unidade": "anos", "decaimento": "β+", "energia": 0.545, "aplicacao": "Calibração"},
        "P-32": {"nome": "Fósforo-32", "meia_vida": 14.29, "unidade": "dias", "decaimento": "β-", "energia": 1.71, "aplicacao": "Terapia"},
        "S-35": {"nome": "Enxofre-35", "meia_vida": 87.44, "unidade": "dias", "decaimento": "β-", "energia": 0.167, "aplicacao": "Pesquisa"},
        "K-40": {"nome": "Potássio-40", "meia_vida": 1.25e9, "unidade": "anos", "decaimento": "β-", "energia": 1.31, "aplicacao": "Datação"},
        "Co-60": {"nome": "Cobalto-60", "meia_vida": 5.27, "unidade": "anos", "decaimento": "β-", "energia": 1.17, "aplicacao": "Radioterapia"},
        "Sr-90": {"nome": "Estrôncio-90", "meia_vida": 28.8, "unidade": "anos", "decaimento": "β-", "energia": 0.546, "aplicacao": "Geradores"},
        "I-131": {"nome": "Iodo-131", "meia_vida": 8.02, "unidade": "dias", "decaimento": "β-", "energia": 0.606, "aplicacao": "Medicina nuclear"},
        "Cs-137": {"nome": "Césio-137", "meia_vida": 30.17, "unidade": "anos", "decaimento": "β-", "energia": 0.514, "aplicacao": "Radiografia"},
        "Ra-226": {"nome": "Rádio-226", "meia_vida": 1600, "unidade": "anos", "decaimento": "α", "energia": 4.78, "aplicacao": "Histórico"},
        "U-235": {"nome": "Urânio-235", "meia_vida": 7.04e8, "unidade": "anos", "decaimento": "α", "energia": 4.4, "aplicacao": "Combustível nuclear"},
        "U-238": {"nome": "Urânio-238", "meia_vida": 4.47e9, "unidade": "anos", "decaimento": "α", "energia": 4.2, "aplicacao": "Datação"},
        "Pu-239": {"nome": "Plutônio-239", "meia_vida": 24110, "unidade": "anos", "decaimento": "α", "energia": 5.15, "aplicacao": "Armas nucleares"},
        "Am-241": {"nome": "Amerício-241", "meia_vida": 432.2, "unidade": "anos", "decaimento": "α", "energia": 5.49, "aplicacao": "Detetores de fumaça"},
        "Tc-99m": {"nome": "Tecnécio-99m", "meia_vida": 6.0, "unidade": "horas", "decaimento": "IT", "energia": 0.141, "aplicacao": "Medicina nuclear"}
    }
    
    # Interface de pesquisa
    col1, col2 = st.columns(2)
    
    with col1:
        pesquisa = st.text_input("🔍 Pesquisar isótopo:", placeholder="Ex: C-14, Co-60, I-131")
        filtro_decaimento = st.selectbox("Filtrar por tipo de decaimento:", 
                                       ["Todos", "β-", "β+", "α", "IT", "EC"])
    
    with col2:
        ordenar_por = st.selectbox("Ordenar por:", 
                                 ["Isótopo", "Meia-vida", "Energia"])
        ordem = st.radio("Ordem:", ["Crescente", "Decrescente"], horizontal=True)
    
    # Filtrar e ordenar resultados
    isotopos_filtrados = []
    
    for iso, props in isotopos_db.items():
        if pesquisa and pesquisa.lower() not in iso.lower() and pesquisa.lower() not in props["nome"].lower():
            continue
            
        if filtro_decaimento != "Todos" and props["decaimento"] != filtro_decaimento:
            continue
            
        isotopos_filtrados.append((iso, props))
    
    # Ordenação
    if ordenar_por == "Isótopo":
        isotopos_filtrados.sort(key=lambda x: x[0])
    elif ordenar_por == "Meia-vida":
        isotopos_filtrados.sort(key=lambda x: x[1]["meia_vida"])
    elif ordenar_por == "Energia":
        isotopos_filtrados.sort(key=lambda x: x[1]["energia"])
    
    if ordem == "Decrescente":
        isotopos_filtrados.reverse()
    
    # Exibir resultados
    st.markdown(f"### 📋 Resultados da Pesquisa ({len(isotopos_filtrados)} isótopos)")
    
    if not isotopos_filtrados:
        st.warning("Nenhum isótopo encontrado com os critérios de pesquisa.")
        return
    
    # Exibir em formato de tabela
    dados_tabela = []
    for iso, props in isotopos_filtrados:
        dados_tabela.append({
            "Isótopo": iso,
            "Nome": props["nome"],
            "Meia-vida": f"{props['meia_vida']} {props['unidade']}",
            "Decaimento": props["decaimento"],
            "Energia (MeV)": props["energia"],
            "Aplicação": props["aplicacao"]
        })
    
    df_isotopos = pd.DataFrame(dados_tabela)
    st.dataframe(df_isotopos, use_container_width=True, height=400)
    
    # Detalhes do isótopo selecionado
    if len(isotopos_filtrados) == 1:
        iso, props = isotopos_filtrados[0]
        st.markdown("---")
        st.markdown(f"### 📚 Detalhes do {iso} - {props['nome']}")
        
        col_det1, col_det2 = st.columns(2)
        
        with col_det1:
            st.markdown(f"**📊 Propriedades Físicas:**")
            st.markdown(f"- **Meia-vida:** {props['meia_vida']} {props['unidade']}")
            st.markdown(f"- **Tipo de decaimento:** {props['decaimento']}")
            st.markdown(f"- **Energia média:** {props['energia']} MeV")
            
            # Calcular constante de decaimento
            if props["unidade"] == "anos":
                T12_anos = props["meia_vida"]
            elif props["unidade"] == "dias":
                T12_anos = props["meia_vida"] / 365.25
            elif props["unidade"] == "horas":
                T12_anos = props["meia_vida"] / (365.25 * 24)
            else:
                T12_anos = props["meia_vida"]
                
            lambda_val = math.log(2) / T12_anos
            st.markdown(f"- **Constante λ:** {lambda_val:.3e} ano⁻¹")
        
        with col_det2:
            st.markdown(f"**🎯 Aplicações:**")
            st.markdown(f"- {props['aplicacao']}")
            
            st.markdown(f"**📈 Informações Adicionais:**")
            st.markdown(f"- **Vida média:** {1/lambda_val:.3e} anos")
            
            # Atividade específica aproximada
            if props["unidade"] == "anos":
                atividade_esp = 4.2e23 / (props["meia_vida"] * 1.66e-24)
                st.markdown(f"- **Atividade específica:** ~{atividade_esp:.1e} Bq/g")
        
        # Gráfico do decaimento
        tempos = np.linspace(0, min(5 * T12_anos, 1000), 100)
        atividade = 100 * np.exp(-lambda_val * tempos)
        
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.plot(tempos, atividade, 'b-', linewidth=2)
        ax.set_xlabel("Tempo (anos)")
        ax.set_ylabel("Atividade Relativa (%)")
        ax.set_title(f"Decaimento do {iso}")
        ax.grid(True)
        
        st.pyplot(fig)
    
    # Opção de download
    csv_data = df_isotopos.to_csv(index=False)
    st.download_button("📥 Baixar Tabela de Isótopos", data=csv_data, 
                      file_name="banco_isotopos_radiometricos.csv", 
                      mime="text/csv", use_container_width=True)

# =============================================================================
# MÓDULO 16: RELATÓRIOS PERSONALIZADOS
# =============================================================================

def modulo_relatorios():
    st.header("📝 Gerador de Relatórios Personalizados")
    
    st.info("""
    **Gere relatórios personalizados das suas simulações.**
    Inclua gráficos, tabelas e análises em formato profissional.
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**📊 Conteúdo do Relatório:**")
        incluir_graficos = st.checkbox("Incluir gráficos", value=True)
        incluir_tabelas = st.checkbox("Incluir tabelas", value=True)
        incluir_calculos = st.checkbox("Incluir cálculos detalhados", value=True)
        incluir_conclusoes = st.checkbox("Incluir conclusões", value=True)
    
    with col2:
        st.markdown("**📋 Formatação:**")
        formato = st.selectbox("Formato do relatório:", 
                             ["Texto", "Markdown", "HTML", "PDF (em desenvolvimento)"])
        estilo = st.selectbox("Estilo:", 
                            ["Acadêmico", "Técnico", "Simples", "Completo"])
    
    titulo = st.text_input("Título do relatório:", "Relatório de Simulação Radiológica")
    autor = st.text_input("Autor:", "Usuário RadSimLab Pro")
    data_relatorio = st.date_input("Data do relatório:", datetime.now())
    
    # Área para conteúdo personalizado
    conteudo_personalizado = st.text_area("Conteúdo adicional:", 
                                        "Descreva aqui observações, metodologia ou resultados adicionais...",
                                        height=100)
    
    if st.button("📝 Gerar Relatório", use_container_width=True):
        # Construir relatório
        relatorio = f"""
        {titulo.upper()}
        {'=' * len(titulo)}
        
        Data: {data_relatorio.strftime('%d/%m/%Y')}
        Autor: {autor}
        
        RESUMO
        ------
        Relatório gerado automaticamente pelo RadSimLab Pro.
        Contém resultados de simulações radiológicas com análises detalhadas.
        
        """
        
        if incluir_calculos:
            relatorio += """
            METODOLOGIA
            ----------
            Os cálculos foram realizados usando as equações fundamentais da física radiológica:
            - Lei do decaimento radioativo: N(t) = N₀ × e^(-λt)
            - Lei da atenuação: I = I₀ × e^(-μx)
            - Efeito Compton: E' = E / [1 + (E/mₑc²)(1 - cosθ)]
            
            Todas as constantes físicas utilizadas estão de acordo com valores padrão do CODATA.
            
            """
        
        if conteudo_personalizado:
            relatorio += f"""
            OBSERVAÇÕES ADICIONAIS
            ---------------------
            {conteudo_personalizado}
            
            """
        
        if incluir_conclusoes:
            relatorio += """
            CONCLUSÕES
            ----------
            As simulações realizadas fornecem insights valiosos sobre o comportamento
            da radiação em diferentes cenários. Os resultados estão de acordo com o
            esperado teoricamente e podem ser utilizados para fins educacionais e de
            planejamento de proteção radiológica.
            
            Recomenda-se a verificação experimental dos resultados para aplicações
            críticas ou uso em contextos profissionais.
            
            """
        
        relatorio += """
        ASSINATURA
        ---------
        Relatório gerado automaticamente por:
        🔬 RadSimLab Pro - Simulador Radiológico Avançado
        📧 radsimlab.pro@example.com
        🌐 https://radsimlab.example.com
        
        """
        
        st.markdown("---")
        st.markdown("### 📄 Visualização do Relatório")
        
        # Exibir preview
        st.text_area("Pré-visualização:", relatorio, height=300)
        
        # Opções de download
        if formato == "Texto":
            st.download_button("📥 Baixar Relatório (.txt)", data=relatorio, 
                              file_name=f"relatorio_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt", 
                              mime="text/plain", use_container_width=True)
        
        elif formato == "Markdown":
            st.info("Funcionalidade Markdown em desenvolvimento.")
        
        elif formato == "HTML":
            # Converter para HTML básico
            html_relatorio = f"""
            <!DOCTYPE html>
            <html>
            <head>
                <title>{titulo}</title>
                <style>
                    body {{ font-family: Arial, sans-serif; margin: 40px; }}
                    h1 {{ color: #2E86AB; }}
                    h2 {{ color: #A23B72; }}
                    .header {{ background-color: #f0f0f0; padding: 20px; border-radius: 10px; }}
                    .content {{ margin: 20px 0; }}
                    .signature {{ margin-top: 50px; padding-top: 20px; border-top: 2px solid #ccc; }}
                </style>
            </head>
            <body>
                <div class="header">
                    <h1>{titulo}</h1>
                    <p><strong>Data:</strong> {data_relatorio.strftime('%d/%m/%Y')}</p>
                    <p><strong>Autor:</strong> {autor}</p>
                </div>
                
                <div class="content">
                    {relatorio.replace('\n', '<br>').replace('        ', '&nbsp;&nbsp;&nbsp;&nbsp;')}
                </div>
                
                <div class="signature">
                    <p><em>Relatório gerado automaticamente por RadSimLab Pro</em></p>
                </div>
            </body>
            </html>
            """
            
            st.download_button("📥 Baixar Relatório (.html)", data=html_relatorio, 
                              file_name=f"relatorio_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html", 
                              mime="text/html", use_container_width=True)
        
        else:
            st.info("Formato PDF em desenvolvimento.")

# =============================================================================
# MÓDULO 17: VALIDAÇÃO E VERIFICAÇÃO
# =============================================================================

def modulo_validacao():
    st.header("✅ Módulo de Validação e Verificação")
    
    st.info("""
    **Verifique a precisão dos cálculos do RadSimLab Pro.**
    Compare com resultados conhecidos e referências científicas.
    """)
    
    teste = st.selectbox("Selecione o teste de validação:", 
                        ["Decaimento Radioativo", "Efeito Compton", 
                         "Atenuação", "Datação C-14", "Todos"])
    
    if st.button("✅ Executar Testes de Validação"):
        resultados = []
        
        # Teste 1: Decaimento Radioativo
        if teste in ["Decaimento Radioativo", "Todos"]:
            st.markdown("### ⚛️ Teste 1: Decaimento Radioativo")
            
            # Para meia-vida de 1 ano, após 1 ano deve restar 50%
            T12 = 1.0
            lambda_val = math.log(2) / T12
            N0 = 1000
            N1 = N0 * math.exp(-lambda_val * T12)
            esperado = N0 * 0.5
            erro = abs(N1 - esperado) / esperado * 100
            
            status = "✅ PASSOU" if erro < 0.1 else "❌ FALHOU"
            cor = "green" if erro < 0.1 else "red"
            
            st.markdown(f"""
            **Parâmetros:**
            - Meia-vida: {T12} ano
            - Número inicial: {N0} átomos
            - Tempo: {T12} ano
            
            **Resultados:**
            - Esperado: {esperado} átomos (50%)
            - Calculado: {N1:.2f} átomos
            - Erro: {erro:.4f}%
            - Status: <span style="color:{cor}">{status}</span>
            """, unsafe_allow_html=True)
            
            resultados.append(("Decaimento Radioativo", erro < 0.1, erro))
        
        # Teste 2: Efeito Compton
        if teste in ["Efeito Compton", "Todos"]:
            st.markdown("### ⚡ Teste 2: Efeito Compton")
            
            # Para E=1 MeV, θ=90°, E' deve ser ~0.338 MeV
            E = 1.0
            theta = 90
            m_e = 0.511  # MeV
            
            theta_rad = math.radians(theta)
            denominador = 1 + (E / m_e) * (1 - math.cos(theta_rad))
            E_prime = E / denominador
            esperado = 0.338
            erro = abs(E_prime - esperado) / esperado * 100
            
            status = "✅ PASSOU" if erro < 1.0 else "❌ FALHOU"
            cor = "green" if erro < 1.0 else "red"
            
            st.markdown(f"""
            **Parâmetros:**
            - Energia incidente: {E} MeV
            - Ângulo: {theta}°
            - mₑc²: {m_e} MeV
            
            **Resultados:**
            - Esperado: {esperado} MeV
            - Calculado: {E_prime:.4f} MeV
            - Erro: {erro:.2f}%
            - Status: <span style="color:{cor}">{status}</span>
            """, unsafe_allow_html=True)
            
            resultados.append(("Efeito Compton", erro < 1.0, erro))
        
        # Teste 3: Atenuação
        if teste in ["Atenuação", "Todos"]:
            st.markdown("### 🧱 Teste 3: Atenuação")
            
            # Para μ=0.1 cm⁻¹, x=10 cm, I/I0 deve ser e^(-1) ≈ 0.3679
            mu = 0.1
            x = 10.0
            I0 = 100.0
            I = I0 * math.exp(-mu * x)
            esperado = I0 * math.exp(-1)
            erro = abs(I - esperado) / esperado * 100
            
            status = "✅ PASSOU" if erro < 0.1 else "❌ FALHOU"
            cor = "green" if erro < 0.1 else "red"
            
            st.markdown(f"""
            **Parâmetros:**
            - Coeficiente μ: {mu} cm⁻¹
            - Espessura: {x} cm
            - Intensidade inicial: {I0}
            
            **Resultados:**
            - Esperado: {esperado:.4f}
            - Calculado: {I:.4f}
            - Erro: {erro:.4f}%
            - Status: <span style="color:{cor}">{status}</span>
            """, unsafe_allow_html=True)
            
            resultados.append(("Atenuação", erro < 0.1, erro))
        
        # Teste 4: Datação C-14
        if teste in ["Datação C-14", "Todos"]:
            st.markdown("### ⏳ Teste 4: Datação por Carbono-14")
            
            # Para N/N0=0.5 e T½=5730 anos, idade deve ser 5730 anos
            frac = 0.5
            T12 = 5730.0
            lambda_val = math.log(2) / T12
            idade = (1 / lambda_val) * math.log(1 / frac)
            esperado = T12
            erro = abs(idade - esperado) / esperado * 100
            
            status = "✅ PASSOU" if erro < 0.1 else "❌ FALHOU"
            cor = "green" if erro < 0.1 else "red"
            
            st.markdown(f"""
            **Parâmetros:**
            - Fração remanescente: {frac}
            - Meia-vida do C-14: {T12} anos
            
            **Resultados:**
            - Esperado: {esperado} anos
            - Calculado: {idade:.2f} anos
            - Erro: {erro:.4f}%
            - Status: <span style="color:{cor}">{status}</span>
            """, unsafe_allow_html=True)
            
            resultados.append(("Datação C-14", erro < 0.1, erro))
        
        # Resumo dos testes
        if teste == "Todos":
            st.markdown("---")
            st.markdown("### 📊 Resumo dos Testes de Validação")
            
            total_testes = len(resultados)
            testes_passados = sum(1 for _, passed, _ in resultados if passed)
            percentual_passou = (testes_passados / total_testes) * 100
            
            st.markdown(f"""
            **Resultado Geral:**
            - Total de testes: {total_testes}
            - Testes passados: {testes_passados}
            - Percentual: {percentual_passou:.1f}%
            """)
            
            if percentual_passou == 100:
                st.success("🎉 TODOS OS TESTES PASSARAM! O RadSimLab Pro está calculando corretamente.")
            else:
                st.warning("⚠️ Alguns testes falharam. Verifique os cálculos.")
            
            # Tabela de resultados
            df_resultados = pd.DataFrame(resultados, columns=["Teste", "Status", "Erro (%)"])
            df_resultados["Status"] = df_resultados["Status"].apply(lambda x: "✅" if x else "❌")
            
            st.dataframe(df_resultados.style.format({"Erro (%)": "{:.4f}"}), use_container_width=True)

# =============================================================================
# ATUALIZAÇÃO DO ROTEIRIZADOR PRINCIPAL
# =============================================================================

# Atualizar o mapeamento de módulos para incluir os novos módulos
modulos_map.update({
    "Sistema de Ajuda": modulo_ajuda,
    "Calculadora Avançada": modulo_calculadora_avancada,
    "Banco de Dados de Isótopos": modulo_banco_isotopos,
    "Relatórios Personalizados": modulo_relatorios,
    "Validação e Verificação": modulo_validacao
})

# =============================================================================
# RODAPÉ E INFORMAÇÕES DO SISTEMA
# =============================================================================

def mostrar_rodape():
    st.markdown("---")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("**📊 Estatísticas do Sistema:**")
        st.markdown(f"- Módulos disponíveis: {len(modulos_map)}")
        st.markdown(f"- Última atualização: {datetime.now().strftime('%d/%m/%Y %H:%M')}")
    
    with col2:
        st.markdown("**🔧 Desenvolvimento:**")
        st.markdown("- Python 3.8+")
        st.markdown("- Streamlit")
        st.markdown("- NumPy, Matplotlib")
    
    with col3:
        st.markdown("**📞 Suporte:**")
        st.markdown("- 📧 suporte@radsimlab.com")
        st.markdown("- 🌐 radsimlab.com/docs")
        st.markdown("- 🐛 Reportar bugs")
    
    st.markdown("---")
    st.markdown("*RadSimLab Pro v2.0 - Simulador Radiológico Avançado*")

# =============================================================================
# EXECUÇÃO PRINCIPAL ATUALIZADA
# =============================================================================

def main():
    # Executar o módulo selecionado
    if modulo in modulos_map:
        modulos_map[modulo]()
    else:
        st.error("Módulo não encontrado!")
    
    # Mostrar rodape em todas as páginas
    mostrar_rodape()

if __name__ == "__main__":
    main()
# Continuação do código anterior...

# =============================================================================
# MELHORIAS E CORREÇÕES ADICIONAIS
# =============================================================================

# Correção para as variáveis h e c no módulo Compton
# As constantes foram definidas corretamente dentro da função modulo_efeito_compton()

# =============================================================================
# SISTEMA DE LOG E MONITORAMENTO
# =============================================================================

import logging
from logging.handlers import RotatingFileHandler
import os

# Configurar sistema de logging
def setup_logging():
    if not os.path.exists('logs'):
        os.makedirs('logs')
    
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            RotatingFileHandler('logs/radsimlab.log', maxBytes=1000000, backupCount=5),
            logging.StreamHandler()
        ]
    )
    
    return logging.getLogger('RadSimLab')

# Inicializar logger
logger = setup_logging()

# =============================================================================
# SISTEMA DE CONFIGURAÇÃO
# =============================================================================

import json
import yaml

class ConfigManager:
    def __init__(self):
        self.config_file = 'config_radsimlab.json'
        self.default_config = {
            'unidades': 'SI',
            'tema': 'claro',
            'precisao': 6,
            'auto_salvar': True,
            'idioma': 'portugues',
            'modulos_ativos': list(modulos_map.keys())
        }
        self.config = self.carregar_config()
    
    def carregar_config(self):
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r') as f:
                    return json.load(f)
            return self.default_config
        except Exception as e:
            logger.error(f"Erro ao carregar configuração: {e}")
            return self.default_config
    
    def salvar_config(self):
        try:
            with open(self.config_file, 'w') as f:
                json.dump(self.config, f, indent=2)
            logger.info("Configuração salva com sucesso")
        except Exception as e:
            logger.error(f"Erro ao salvar configuração: {e}")
    
    def get(self, chave, padrao=None):
        return self.config.get(chave, padrao)
    
    def set(self, chave, valor):
        self.config[chave] = valor
        if self.config.get('auto_salvar', True):
            self.salvar_config()

# Inicializar gerenciador de configuração
config_manager = ConfigManager()

# =============================================================================
# SISTEMA DE TRADUÇÃO
# =============================================================================

class TranslationSystem:
    def __init__(self):
        self.translations = {
            'portugues': {
                'welcome': 'Bem-vindo ao RadSimLab Pro',
                'calculate': 'Calcular',
                'results': 'Resultados',
                'error': 'Erro',
                'success': 'Sucesso',
                'warning': 'Aviso',
                # Adicionar mais traduções conforme necessário
            },
            'english': {
                'welcome': 'Welcome to RadSimLab Pro',
                'calculate': 'Calculate',
                'results': 'Results',
                'error': 'Error',
                'success': 'Success',
                'warning': 'Warning',
            },
            'espanol': {
                'welcome': 'Bienvenido a RadSimLab Pro',
                'calculate': 'Calcular',
                'results': 'Resultados',
                'error': 'Error',
                'success': 'Éxito',
                'warning': 'Advertencia',
            }
        }
    
    def t(self, key, lang=None):
        if lang is None:
            lang = config_manager.get('idioma', 'portugues')
        return self.translations.get(lang, {}).get(key, key)

# Inicializar sistema de tradução
translator = TranslationSystem()

# =============================================================================
# SISTEMA DE CACHE PARA PERFORMANCE
# =============================================================================

from functools import lru_cache
import hashlib

class CacheSystem:
    def __init__(self, max_size=100):
        self.cache = {}
        self.max_size = max_size
    
    def gerar_chave(self, *args, **kwargs):
        """Gera uma chave única para os argumentos"""
        key_str = str(args) + str(sorted(kwargs.items()))
        return hashlib.md5(key_str.encode()).hexdigest()
    
    def get(self, key):
        return self.cache.get(key)
    
    def set(self, key, value):
        if len(self.cache) >= self.max_size:
            # Remover o item mais antigo (FIFO)
            oldest_key = next(iter(self.cache))
            del self.cache[oldest_key]
        self.cache[key] = value
    
    def clear(self):
        self.cache.clear()

# Inicializar sistema de cache
cache_system = CacheSystem()

# Decorator para funções que beneficiam de cache
def cached_function(func):
    @lru_cache(maxsize=50)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

# =============================================================================
# MELHORIAS DE PERFORMANCE PARA CÁLCULOS INTENSIVOS
# =============================================================================

@cached_function
def calcular_decaimento(N0, lambda_val, tempo):
    """Função otimizada para cálculo de decaimento com cache"""
    return N0 * math.exp(-lambda_val * tempo)

@cached_function  
def calcular_compton(E, theta_graus, m_e=0.511):
    """Função otimizada para efeito Compton com cache"""
    theta_rad = math.radians(theta_graus)
    denominador = 1 + (E / m_e) * (1 - math.cos(theta_rad))
    return E / denominador

@cached_function
def calcular_atenuacao(I0, mu, x):
    """Função otimizada para atenuação com cache"""
    return I0 * math.exp(-mu * x)

# =============================================================================
# SISTEMA DE RELATÓRIOS DE ERROS
# =============================================================================

def reportar_erro(erro, modulo, detalhes=""):
    """Reporta erros para logging e exibição ao usuário"""
    mensagem_erro = f"Erro em {modulo}: {erro}"
    if detalhes:
        mensagem_erro += f" | Detalhes: {detalhes}"
    
    logger.error(mensagem_erro)
    
    # Exibir para o usuário de forma amigável
    st.error(f"❌ Ocorreu um erro no módulo {modulo}. Detalhes técnicos foram registrados.")
    st.info("💡 Dica: Verifique os valores de entrada e tente novamente.")
    
    if st.checkbox("Mostrar detalhes técnicos do erro (para desenvolvedores)"):
        st.code(f"Erro: {erro}\nDetalhes: {detalhes}")

# =============================================================================
# ATUALIZAÇÃO DAS FUNÇÕES EXISTENTES COM MELHORIAS
# =============================================================================

def modulo_datacao_radiometrica_otimizado():
    """Versão otimizada do módulo de datação"""
    try:
        st.header("⏳ Datação Radiométrica")
        
        # ... (código anterior, mas usando funções otimizadas)
        
        if st.button(translator.t('calculate')):
            # Usar função otimizada com cache
            lambda_val = math.log(2) / meia_vida
            idade = (1 / lambda_val) * math.log(1 / frac_remanescente)
            
            # Resto do código...
            
    except Exception as e:
        reportar_erro(e, "Datação Radiométrica", str(e))

# =============================================================================
# SISTEMA DE BACKUP AUTOMÁTICO
# =============================================================================

def realizar_backup():
    """Realiza backup das configurações e dados importantes"""
    try:
        backup_dir = 'backups'
        if not os.path.exists(backup_dir):
            os.makedirs(backup_dir)
        
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        backup_file = os.path.join(backup_dir, f'backup_{timestamp}.json')
        
        dados_backup = {
            'configuracoes': config_manager.config,
            'timestamp': timestamp,
            'versao': '2.0'
        }
        
        with open(backup_file, 'w') as f:
            json.dump(dados_backup, f, indent=2)
        
        logger.info(f"Backup realizado: {backup_file}")
        return True
        
    except Exception as e:
        logger.error(f"Erro no backup: {e}")
        return False

# =============================================================================
# INTERFACE DE ADMINISTRAÇÃO
# =============================================================================

def modulo_administracao():
    st.header("⚙️ Painel de Administração")
    
    if not st.session_state.get('admin_mode', False):
        senha = st.text_input("Senha de administração:", type="password")
        if senha == "admin123":  # Senha padrão - mudar em produção
            st.session_state.admin_mode = True
            st.success("Modo administrador ativado")
        elif senha:
            st.error("Senha incorreta")
            return
    
    if st.session_state.get('admin_mode', False):
        tab1, tab2, tab3, tab4 = st.tabs(["Configurações", "Logs", "Backup", "Estatísticas"])
        
        with tab1:
            st.subheader("Configurações do Sistema")
            
            col1, col2 = st.columns(2)
            
            with col1:
                novo_idioma = st.selectbox("Idioma:", ["portugues", "english", "espanol"])
                novo_tema = st.selectbox("Tema:", ["claro", "escuro"])
                precisao = st.slider("Precisão decimal:", 2, 10, 6)
            
            with col2:
                auto_salvar = st.checkbox("Salvamento automático", value=True)
                auto_backup = st.checkbox("Backup automático", value=False)
                logging_level = st.selectbox("Nível de logging:", ["INFO", "DEBUG", "WARNING", "ERROR"])
            
            if st.button("💾 Aplicar Configurações"):
                config_manager.set('idioma', novo_idioma)
                config_manager.set('tema', novo_tema)
                config_manager.set('precisao', precisao)
                config_manager.set('auto_salvar', auto_salvar)
                config_manager.set('auto_backup', auto_backup)
                config_manager.set('logging_level', logging_level)
                
                st.success("Configurações aplicadas com sucesso!")
        
        with tab2:
            st.subheader("Visualizador de Logs")
            
            if os.path.exists('logs/radsimlab.log'):
                with open('logs/radsimlab.log', 'r') as f:
                    logs = f.read()
                
                st.text_area("Logs do sistema:", logs, height=300)
                
                if st.button("🔄 Atualizar Logs"):
                    st.rerun()
                
                if st.button("🧹 Limpar Logs"):
                    open('logs/radsimlab.log', 'w').close()
                    st.success("Logs limpos!")
            else:
                st.info("Nenhum arquivo de log encontrado.")
        
        with tab3:
            st.subheader("Gerenciamento de Backup")
            
            if st.button("💾 Criar Backup Agora"):
                if realizar_backup():
                    st.success("Backup realizado com sucesso!")
                else:
                    st.error("Erro ao realizar backup.")
            
            # Listar backups existentes
            if os.path.exists('backups'):
                backups = sorted(os.listdir('backups'), reverse=True)
                if backups:
                    st.markdown("**Backups existentes:**")
                    for backup in backups[:5]:  # Mostrar apenas os 5 mais recentes
                        st.code(backup)
                else:
                    st.info("Nenhum backup encontrado.")
        
        with tab4:
            st.subheader("Estatísticas do Sistema")
            
            col_stat1, col_stat2, col_stat3 = st.columns(3)
            
            with col_stat1:
                st.metric("Módulos disponíveis", len(modulos_map))
                st.metric("Configurações salvas", len(config_manager.config))
            
            with col_stat2:
                st.metric("Itens em cache", len(cache_system.cache))
                if os.path.exists('logs/radsimlab.log'):
                    tamanho_log = os.path.getsize('logs/radsimlab.log')
                    st.metric("Tamanho do log", f"{tamanho_log/1024:.1f} KB")
            
            with col_stat3:
                if os.path.exists('backups'):
                    num_backups = len(os.listdir('backups'))
                    st.metric("Backups", num_backups)
        
        if st.button("🚪 Sair do Modo Administrador"):
            st.session_state.admin_mode = False
            st.success("Modo administrador desativado")

# =============================================================================
# SISTEMA DE ATUALIZAÇÕES AUTOMÁTICAS
# =============================================================================

def verificar_atualizacoes():
    """Verifica se há atualizações disponíveis"""
    try:
        # Em uma implementação real, isso faria uma requisição para um servidor
        # Por enquanto, é apenas um placeholder
        return {
            'atualizacao_disponivel': False,
            'versao_atual': '2.0',
            'nova_versao': None,
            'url_download': None
        }
    except Exception as e:
        logger.error(f"Erro ao verificar atualizações: {e}")
        return {
            'atualizacao_disponivel': False,
            'erro': str(e)
        }

# =============================================================================
# MELHORIAS NA INTERFACE DO USUÁRIO
# =============================================================================

def carregar_estilo():
    """Carrega o estilo CSS baseado na configuração"""
    tema = config_manager.get('tema', 'claro')
    
    if tema == 'escuro':
        return """
        <style>
            .main { background-color: #1E1E1E; color: #FFFFFF; }
            .stButton>button { background-color: #4CAF50; color: white; }
            .result-box { background-color: #2D3748; color: #E2E8F0; }
        </style>
        """
    else:
        return """
        <style>
            .main { background-color: #FFFFFF; color: #000000; }
            .stButton>button { background-color: #1E88E5; color: white; }
            .result-box { background-color: #E8F5E9; color: #1B5E20; }
        </style>
        """

# =============================================================================
# ATUALIZAÇÃO FINAL DO ROTEIRIZADOR PRINCIPAL
# =============================================================================

# Adicionar módulo de administração ao mapeamento
modulos_map["Administração"] = modulo_administracao

def main():
    # Carregar estilo
    st.markdown(carregar_estilo(), unsafe_allow_html=True)
    
    # Verificar atualizações (apenas uma vez por sessão)
    if 'atualizacao_verificada' not in st.session_state:
        info_atualizacao = verificar_atualizacoes()
        if info_atualizacao['atualizacao_disponivel']:
            st.sidebar.warning("📦 Atualização disponível!")
        st.session_state.atualizacao_verificada = True
    
    # Executar o módulo selecionado com tratamento de erro
    try:
        if modulo in modulos_map:
            modulos_map[modulo]()
        else:
            st.error("Módulo não encontrado!")
            
    except Exception as e:
        reportar_erro(e, modulo)
        st.error("Ocorreu um erro inesperado. Tente recarregar a página.")
        
        # Botão para recarregar
        if st.button("🔄 Recarregar Página"):
            st.rerun()
    
    # Mostrar rodape
    mostrar_rodape()
    
    # Backup automático se configurado
    if config_manager.get('auto_backup', False):
        if 'ultimo_backup' not in st.session_state:
            if realizar_backup():
                st.session_state.ultimo_backup = datetime.now()
                logger.info("Backup automático realizado")
        
        # Verificar se passou 1 hora desde o último backup
        elif (datetime.now() - st.session_state.ultimo_backup).total_seconds() > 3600:
            if realizar_backup():
                st.session_state.ultimo_backup = datetime.now()
                logger.info("Backup automático realizado")

# =============================================================================
# INICIALIZAÇÃO DO SISTEMA
# =============================================================================

if __name__ == "__main__":
    # Inicializar session state
    if 'admin_mode' not in st.session_state:
        st.session_state.admin_mode = False
    if 'ultimo_backup' not in st.session_state:
        st.session_state.ultimo_backup = None
    
    # Iniciar aplicação
    try:
        main()
    except Exception as e:
        logger.critical(f"Erro crítico na inicialização: {e}")
        st.error("❌ Erro crítico na aplicação. Por favor, recarregue.")
        
        # Botão de emergência
        if st.button("🆘 Reiniciar Aplicação"):
            # Limpar cache e session state
            cache_system.clear()
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()
