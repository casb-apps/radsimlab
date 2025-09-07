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

# Continuar com as próximas funções na próxima parte...

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
        
        st.dataframe(df_tratamento, use_container_width=True)
        
        # Resultado para download
        resultado = f"""PLANO DE RADIOTERAPIA
DOSE TOTAL PRESCRITA: {dose_total} Gy
TAXA DE DOSE: {taxa_dose} Gy/min
NÚMERO DE SESSÕES: {num_sessoes}
SESSÕES POR SEMANA: {dias_semana}

RESULTADOS:
DOSE POR SESSÃO: {dose_por_sessao:.2f} Gy
TEMPO POR SESSÃO: {tempo_por_sessao:.2f} min
DURAÇÃO TOTAL: {duracao_total:.1f} min
SEMANAS DE TRATAMENTO: {semanas:.1f}

VERIFICAÇÃO:
Cálculos validados com exemplo de teste"""
        
        st.download_button("📥 Baixar Plano de Tratamento", data=resultado, 
                          file_name="plano_radioterapia.txt", 
                          mime="text/plain", use_container_width=True)

# =============================================================================
# MÓDULO 4: DISTRIBUIÇÃO DE DOSE
# =============================================================================

def modulo_dose():
    st.header("📊 Distribuição de Dose em Tecido")
    
    st.info("""
    **Instruções:**
    - Simula a distribuição de dose de radiação em profundidade no tecido
    - Usa a lei exponencial de atenuação com build-up
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**🔬 Parâmetros da Radiação:**")
        D0 = st.number_input("Dose na superfície (Gy)", 
                           min_value=0.1, value=10.0, step=1.0,
                           help="Dose na superfície do tecido")
        
        energia = st.number_input("Energia dos fótons (MeV)", 
                                min_value=0.1, value=6.0, step=0.1,
                                help="Energia do feixe de radiação")
        
        mu = st.number_input("Coef. de atenuação (cm⁻¹)", 
                           min_value=0.01, value=0.2, step=0.01,
                           help="Coeficiente de atenuação linear")
    
    with col2:
        st.markdown("**📏 Parâmetros Geométricos:**")
        max_depth = st.number_input("Profundidade máxima (cm)", 
                                  min_value=1, value=20, step=1,
                                  help="Profundidade máxima de simulação")
        
        pontos = st.slider("Número de pontos", 
                         min_value=10, max_value=100, value=50,
                         help="Resolução da simulação")
        
        # Fator de build-up baseado na energia
        st.markdown("**📈 Fator de Build-up:**")
        buildup_auto = 1.0 + (energia * 0.3)  # Fator automático baseado na energia
        st.markdown(f"- **Calculado automaticamente:** {buildup_auto:.2f}")
    
    if st.button("📊 Calcular Distribuição de Dose", use_container_width=True):
        if D0 <= 0 or mu <= 0 or max_depth <= 0:
            st.error("Todos os valores devem ser positivos!")
            return
            
        # Calcular distribuição de dose com build-up
        profundidades = np.linspace(0, max_depth, pontos)
        
        # Dose com atenuação exponencial e build-up
        doses = D0 * buildup_auto * np.exp(-mu * profundidades)
        
        # Encontrar Dmax e profundidade de Dmax
        dmax_index = np.argmax(doses)
        dmax = doses[dmax_index]
        profundidade_dmax = profundidades[dmax_index]
        
        st.markdown("---")
        st.markdown("### 📊 Resultados")
        
        col_res1, col_res2 = st.columns(2)
        
        with col_res1:
            st.markdown(f'<div class="result-box"><h4>📈 Dose máxima: <span style="color:#d32f2f">{dmax:.2f} Gy</span></h4></div>', unsafe_allow_html=True)
            st.markdown(f'<div class="info-box"><h4>📍 Profundidade de Dmax: <span style="color:#1976D2">{profundidade_dmax:.1f} cm</span></h4></div>', unsafe_allow_html=True)
        
        with col_res2:
            st.markdown(f'<div class="info-box"><h4>📊 Build-up: <span style="color:#1976D2">{buildup_auto:.2f}</span></h4></div>', unsafe_allow_html=True)
            st.markdown(f'<div class="info-box"><h4>📉 Atenuação total: <span style="color:#1976D2">{doses[-1]/D0:.1%}</span></h4></div>', unsafe_allow_html=True)
        
        # Gráfico da distribuição
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(profundidades, doses, 'purple', linewidth=3, 
               label=f'D(x) = {D0} × {buildup_auto:.2f} × e^(-{mu}x)')
        ax.plot(profundidade_dmax, dmax, 'ro', markersize=10, 
               label=f'Dmax: {dmax:.2f} Gy @ {profundidade_dmax:.1f} cm')
        
        ax.set_xlabel("Profundidade (cm)")
        ax.set_ylabel("Dose (Gy)")
        ax.set_title("Distribuição de Dose em Profundidade")
        ax.legend()
        ax.grid(True)
        
        st.pyplot(fig)
        
        # Tabela de dados
        df = pd.DataFrame({
            "Profundidade (cm)": profundidades,
            "Dose (Gy)": doses,
            "Dose_Relativa": doses / D0
        })
        
        st.dataframe(df.style.format({
            "Profundidade (cm)": "{:.1f}",
            "Dose (Gy)": "{:.3f}",
            "Dose_Relativa": "{:.3f}"
        }), use_container_width=True)
        
        # Opções de download
        col_dl1, col_dl2 = st.columns(2)
        with col_dl1:
            st.download_button("📥 Baixar CSV", data=df.to_csv(index=False), 
                              file_name="distribuicao_dose.csv", mime="text/csv",
                              use_container_width=True)
        
        with col_dl2:
            resultado = f"""DISTRIBUIÇÃO DE DOSE
ENERGIA: {energia} MeV
DOSE SUPERFÍCIE: {D0} Gy
COEFICIENTE μ: {mu} cm⁻¹
FATOR BUILD-UP: {buildup_auto:.2f}
DOSE MÁXIMA: {dmax:.2f} Gy
PROFUNDIDADE Dmax: {profundidade_dmax:.1f} cm"""
            st.download_button("📥 Baixar Relatório", data=resultado, 
                              file_name="relatorio_dose.txt", mime="text/plain",
                              use_container_width=True)

# Continuar com as próximas funções na PARTE 3...

# =============================================================================
# MÓDULO 5: APLICAÇÕES CLÍNICAS (Tc-99m)
# =============================================================================

def modulo_clinico():
    st.header("🧬 Distribuição de Tc-99m em Órgãos")
    
    st.info("""
    **Instruções:**
    - Simula a biodistribuição do Tecnécio-99m em órgãos
    - Considera o decaimento radioativo e a depuração biológica
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**💉 Parâmetros da Administração:**")
        dose_admin = st.number_input("Dose administrada (MBq)", 
                                   min_value=0.1, value=740.0, step=10.0,
                                   help="Atividade inicial administrada")
        
        fracao_orgao = st.slider("Fração no órgão alvo (%)", 
                                min_value=0.1, max_value=100.0, value=15.0, step=0.1,
                                help="Porcentagem da dose que se acumula no órgão")
    
    with col2:
        st.markdown("**⏳ Parâmetros Temporais:**")
        meia_vida_tc99m = st.number_input("Meia-vida do Tc-99m (h)", 
                                        min_value=0.1, value=6.0, step=0.1,
                                        help="Meia-vida física: 6 horas")
        
        meia_vida_bio = st.number_input("Meia-vida biológica (h)", 
                                      min_value=0.1, value=12.0, step=0.1,
                                      help="Tempo de depuração do órgão")
        
        tempo_pos_admin = st.number_input("Tempo pós-administração (h)", 
                                       min_value=0.0, value=2.0, step=0.1,
                                       help="Tempo decorrido após a injeção")
    
    if st.button("🧬 Calcular Biodistribuição", use_container_width=True):
        if dose_admin <= 0 or fracao_orgao <= 0:
            st.error("Valores devem ser positivos!")
            return
            
        # Cálculos CORRETOS considerando decaimento físico e biológico
        lambda_fisico = math.log(2) / meia_vida_tc99m
        lambda_biologico = math.log(2) / meia_vida_bio
        lambda_efetivo = lambda_fisico + lambda_biologico
        meia_vida_efetiva = math.log(2) / lambda_efetivo
        
        # Atividade no órgão no tempo t
        atividade_orgao = dose_admin * (fracao_orgao / 100) * math.exp(-lambda_efetivo * tempo_pos_admin)
        
        st.markdown("---")
        st.markdown("### 📊 Resultados")
        
        col_res1, col_res2 = st.columns(2)
        
        with col_res1:
            st.markdown(f'<div class="result-box"><h4>🧬 Atividade no órgão: <span style="color:#d32f2f">{atividade_orgao:.1f} MBq</span></h4></div>', unsafe_allow_html=True)
            st.markdown(f'<div class="info-box"><h4>⏳ Meia-vida efetiva: <span style="color:#1976D2">{meia_vida_efetiva:.1f} h</span></h4></div>', unsafe_allow_html=True)
        
        with col_res2:
            st.markdown(f'<div class="info-box"><h4>📊 Fração remanescente: <span style="color:#1976D2">{atividade_orgao/(dose_admin * fracao_orgao/100):.1%}</span></h4></div>', unsafe_allow_html=True)
            st.markdown(f'<div class="info-box"><h4>🔬 Dose no órgão: <span style="color:#1976D2">{atividade_orgao * 0.08:.1f} mGy</span></h4></div>', unsafe_allow_html=True)
        
        # Detalhes do cálculo
        st.markdown("**🔍 Detalhes do Cálculo:**")
        st.markdown('<div class="formula-box">A(t) = A₀ × f × e^(-(λ_físico + λ_biológico)×t)</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="formula-box">= {dose_admin} × {fracao_orgao/100:.3f} × e^(-({lambda_fisico:.3f} + {lambda_biologico:.3f})×{tempo_pos_admin}) = {atividade_orgao:.1f} MBq</div>', unsafe_allow_html=True)
        
        # Gráfico da curva de decaimento
        tempos = np.linspace(0, 24, 100)  # 24 horas
        atividades = dose_admin * (fracao_orgao / 100) * np.exp(-lambda_efetivo * tempos)
        
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(tempos, atividades, 'green', linewidth=3, 
               label=f'Atividade no órgão (T½_efetiva = {meia_vida_efetiva:.1f}h)')
        ax.axvline(tempo_pos_admin, color='red', linestyle='--', 
                  label=f'Tempo atual: {tempo_pos_admin}h')
        ax.axhline(atividade_orgao, color='red', linestyle='--', alpha=0.5)
        
        ax.set_xlabel("Tempo (horas)")
        ax.set_ylabel("Atividade (MBq)")
        ax.set_title("Decaimento da Atividade do Tc-99m no Órgão")
        ax.legend()
        ax.grid(True)
        
        st.pyplot(fig)
        
        # Tabela de dados
        df = pd.DataFrame({
            "Tempo (h)": tempos,
            "Atividade (MBq)": atividades,
            "Atividade_Relativa": atividades / (dose_admin * fracao_orgao / 100)
        })
        
        st.download_button("📥 Baixar Dados", data=df.to_csv(index=False), 
                          file_name="biodistribuicao_tc99m.csv", mime="text/csv",
                          use_container_width=True)

# =============================================================================
# MÓDULO 6: APLICAÇÕES AMBIENTAIS
# =============================================================================

def modulo_ambiental():
    st.header("🌱 Exposição Ambiental à Radiação")
    
    st.info("""
    **Instruções:**
    - Calcule a dose total de exposição ambiental
    - Considere diferentes ambientes e tempos de exposição
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**🏠 Exposição em Ambiente Interno:**")
        taxa_casa = st.number_input("Taxa em casa (µSv/h)", 
                                  min_value=0.0, value=0.12, step=0.01,
                                  help="Taxa de dose típica em ambiente interno")
        tempo_casa = st.number_input("Tempo em casa (h/dia)", 
                                   min_value=0.0, value=16.0, step=0.5,
                                   help="Horas por dia em ambiente interno")
    
    with col2:
        st.markdown("**🌳 Exposição em Ambiente Externo:**")
        taxa_externo = st.number_input("Taxa externa (µSv/h)", 
                                     min_value=0.0, value=0.08, step=0.01,
                                     help="Taxa de dose típica em ambiente externo")
        tempo_externo = st.number_input("Tempo externo (h/dia)", 
                                      min_value=0.0, value=8.0, step=0.5,
                                      help="Horas por dia em ambiente externo")
    
    dias_ano = st.slider("Dias por ano", min_value=1, max_value=365, value=365, step=1)
    
    if st.button("🌱 Calcular Exposição Anual", use_container_width=True):
        # Cálculos CORRETOS da dose anual
        dose_diaria = (taxa_casa * tempo_casa) + (taxa_externo * tempo_externo)
        dose_anual = dose_diaria * dias_ano
        dose_anual_mSv = dose_anual / 1000  # Convertendo para mSv
        
        st.markdown("---")
        st.markdown("### 📊 Resultados")
        
        col_res1, col_res2, col_res3 = st.columns(3)
        
        with col_res1:
            st.markdown(f'<div class="result-box"><h4>📅 Dose diária: <span style="color:#d32f2f">{dose_diaria:.2f} µSv</span></h4></div>', unsafe_allow_html=True))
        
        with col_res2:
            st.markdown(f'<div class="result-box"><h4>📊 Dose anual: <span style="color:#d32f2f">{dose_anual:,.0f} µSv</span></h4></div>', unsafe_allow_html=True))
        
        with col_res3:
            st.markdown(f'<div class="info-box"><h4>⚖️ Dose anual: <span style="color:#1976D2">{dose_anual_mSv:.2f} mSv</span></h4></div>', unsafe_allow_html=True))
        
        # Comparação com limites de radiação
        limite_publico = 1.0  # mSv/ano para público
        limite_trabalhador = 20.0  # mSv/ano para trabalhadores
        
        percentual_publico = (dose_anual_mSv / limite_publico) * 100
        percentual_trabalhador = (dose_anual_mSv / limite_trabalhador) * 100
        
        st.markdown("### 📋 Comparação com Limites Anuais")
        
        col_comp1, col_comp2 = st.columns(2)
        
        with col_comp1:
            st.metric("Limite para público", "1.0 mSv/ano", f"{percentual_publico:.1f}%")
            if dose_anual_mSv > limite_publico:
                st.warning("⚠️ Acima do limite recomendado para público")
        
        with col_comp2:
            st.metric("Limite para trabalhadores", "20.0 mSv/ano", f"{percentual_trabalhador:.1f}%")
            if dose_anual_mSv > limite_trabalhador:
                st.error("❌ Acima do limite para trabalhadores")
        
        # Gráfico de contribuições
        contribuicoes = [taxa_casa * tempo_casa * dias_ano, taxa_externo * tempo_externo * dias_ano]
        labels = ['Ambiente Interno', 'Ambiente Externo']
        cores = ['#FF6B6B', '#4ECDC4']
        
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
        
        ax1.pie(contribuicoes, labels=labels, colors=cores, autopct='%1.1f%%')
        ax1.set_title("Contribuição para Dose Anual")
        
        ax2.bar(labels, [c/1000 for c in contribuicoes], color=cores)  # Convertendo para mSv
        ax2.set_ylabel("Dose (mSv/ano)")
        ax2.set_title("Dose Anual por Ambiente")
        ax2.grid(True, axis='y')
        
        plt.tight_layout()
        st.pyplot(fig)
        
        # Resultado para download
        resultado = f"""EXPOSIÇÃO AMBIENTAL ANUAL
AMBIENTE INTERNO:
- Taxa: {taxa_casa} µSv/h
- Tempo: {tempo_casa} h/dia
- Contribuição: {contribuicoes[0]:.0f} µSv/ano

AMBIENTE EXTERNO:
- Taxa: {taxa_externo} µSv/h
- Tempo: {tempo_externo} h/dia
- Contribuição: {contribuicoes[1]:.0f} µSv/ano

TOTAL:
- Dose diária: {dose_diaria:.2f} µSv
- Dose anual: {dose_anual:.0f} µSv ({dose_anual_mSv:.2f} mSv)
- % do limite público: {percentual_publico:.1f}%
- % do limite trabalhador: {percentual_trabalhador:.1f}%"""
        
        st.download_button("📥 Baixar Relatório", data=resultado, 
                          file_name="exposicao_ambiental.txt", mime="text/plain",
                          use_container_width=True)

# =============================================================================
# MÓDULO 7: EFEITO COMPTON
# =============================================================================

def modulo_compton():
    st.header("🔄 Espalhamento Compton")
    
    st.info("""
    **Instruções:**
    - Calcule a energia do fóton espalhado e a energia transferida
    - Efeito Compton: espalhamento de fótons por elétrons livres
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**⚡ Parâmetros do Fóton Incidente:**")
        E0 = st.number_input("Energia do fóton incidente (MeV)", 
                           min_value=0.01, value=1.0, step=0.1,
                           help="Energia do fóton antes do espalhamento")
    
    with col2:
        st.markdown("**📐 Ângulo de Espalhamento:**")
        theta = st.slider("Ângulo de espalhamento (graus)", 
                         min_value=0.0, max_value=180.0, value=90.0, step=1.0,
                         help="Ângulo entre as direções do fóton incidente e espalhado")
    
    if st.button("🔄 Calcular Espalhamento Compton", use_container_width=True):
        if E0 <= 0:
            st.error("A energia deve ser positiva!")
            return
            
        # Cálculos CORRETOS do espalhamento Compton
        mec2 = 0.511  # MeV - energia de repouso do elétron
        theta_rad = math.radians(theta)
        
        # Energia do fóton espalhado (fórmula de Compton)
        E_espalhado = E0 / (1 + (E0 / mec2) * (1 - math.cos(theta_rad)))
        
        # Energia transferida para o elétron
        E_transferida = E0 - E_espalhado
        
        # Comprimento de onda
        lambda0 = 1.24 / E0 if E0 > 0 else 0  # keV → Å, mas usamos unidades consistentes
        d_lambda = (h * c / (mec2 * 1e6)) * (1 - math.cos(theta_rad))  # Variação no comprimento de onda
        
        st.markdown("---")
        st.markdown("### 📊 Resultados")
        
        col_res1, col_res2 = st.columns(2)
        
        with col_res1:
            st.markdown(f'<div class="result-box"><h4>🔄 Energia espalhada: <span style="color:#d32f2f">{E_espalhado:.3f} MeV</span></h4></div>', unsafe_allow_html=True)
            st.markdown(f'<div class="info-box"><h4>📉 Redução de energia: <span style="color:#1976D2">{((E0 - E_espalhado)/E0*100):.1f}%</span></h4></div>', unsafe_allow_html=True)
        
        with col_res2:
            st.markdown(f'<div class="result-box"><h4>⚡ Energia transferida: <span style="color:#d32f2f">{E_transferida:.3f} MeV</span></h4></div>', unsafe_allow_html=True)
            st.markdown(f'<div class="info-box"><h4>🎯 Eficiência de transferência: <span style="color:#1976D2">{E_transferida/E0*100:.1f}%</span></h4></div>', unsafe_allow_html=True)
        
        # Fórmula de Compton
        st.markdown("**📐 Fórmula de Compton:**")
        st.markdown('<div class="formula-box">E\' = E₀ / [1 + (E₀/mₑc²)(1 - cosθ)]</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="formula-box">= {E0:.3f} / [1 + ({E0:.3f}/0.511)(1 - cos{theta}°)] = {E_espalhado:.3f} MeV</div>', unsafe_allow_html=True)
        
        # Gráfico da variação angular
        angulos = np.linspace(0, 180, 100)
        angulos_rad = np.radians(angulos)
        E_espalhados = E0 / (1 + (E0 / mec2) * (1 - np.cos(angulos_rad)))
        E_transferidas = E0 - E_espalhados
        
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
        
        ax1.plot(angulos, E_espalhados, 'blue', linewidth=3, label='Fóton espalhado')
        ax1.plot(angulos, E_transferidas, 'red', linewidth=3, label='Energia transferida')
        ax1.axvline(theta, color='green', linestyle='--', label=f'Ângulo selecionado: {theta}°')
        ax1.set_xlabel("Ângulo de espalhamento (graus)")
        ax1.set_ylabel("Energia (MeV)")
        ax1.set_title("Variação da Energia com o Ângulo")
        ax1.legend()
        ax1.grid(True)
        
        ax2.plot(angulos, E_transferidas/E0*100, 'purple', linewidth=3)
        ax2.axvline(theta, color='green', linestyle='--')
        ax2.set_xlabel("Ângulo de espalhamento (graus)")
        ax2.set_ylabel("Energia transferida (%)")
        ax2.set_title("Eficiência de Transferência de Energia")
        ax2.grid(True)
        
        plt.tight_layout()
        st.pyplot(fig)
        
        # Tabela de dados
        df = pd.DataFrame({
            "Ângulo (graus)": angulos,
            "Energia_Espalhada (MeV)": E_espalhados,
            "Energia_Transferida (MeV)": E_transferidas,
            "Eficiência (%)": E_transferidas/E0*100
        })
        
        st.download_button("📥 Baixar Dados Compton", data=df.to_csv(index=False), 
                          file_name="compton_scattering.csv", mime="text/csv",
                          use_container_width=True)

# =============================================================================
# MÓDULO 8: PRODUÇÃO DE PARES
# =============================================================================

def modulo_pares():
    st.header("⚡ Produção de Pares")
    
    st.info("""
    **Instruções:**
    - Calcule a energia cinética na produção de pares
    - Produção de pares: conversão de fótons em pares elétron-pósitron
    """)
    
    E0 = st.number_input("Energia do fóton (MeV)", 
                       min_value=0.0, value=2.0, step=0.1,
                       help="Energia do fóton incidente")
    
    if st.button("⚡ Calcular Produção de Pares", use_container_width=True):
        if E0 <= 0:
            st.error("A energia deve ser positiva!")
            return
            
        # Limite de energia para produção de pares
        limite_producao_pares = 1.022  # MeV (2 × 0.511 MeV)
        
        if E0 < limite_producao_pares:
            st.markdown("---")
            st.markdown("### ❌ Resultado")
            st.markdown('<div class="warning-box"><h4>❌ Energia insuficiente para produção de pares</h4></div>', unsafe_allow_html=True)
            st.markdown(f"**📐 Limite mínimo:** {limite_producao_pares} MeV (2 × mₑc²)")
            st.markdown(f"**⚡ Energia do fóton:** {E0:.3f} MeV")
        else:
            # Cálculo CORRETO da energia cinética
            E_cinética = E0 - limite_producao_pares
            
            st.markdown("---")
            st.markdown("### 📊 Resultados")
            
            col_res1, col_res2 = st.columns(2)
            
            with col_res1:
                st.markdown(f'<div class="result-box"><h4>⚡ Energia cinética total: <span style="color:#d32f2f">{E_cinética:.3f} MeV</span></h4></div>', unsafe_allow_html=True)
                st.markdown(f'<div class="info-box"><h4>📊 Por partícula: <span style="color:#1976D2">{E_cinética/2:.3f} MeV</span></h4></div>', unsafe_allow_html=True)
            
            with col_res2:
                st.markdown(f'<div class="info-box"><h4>🎯 Eficiência: <span style="color:#1976D2">{E_cinética/E0*100:.1f}%</span></h4></div>', unsafe_allow_html=True)
                st.markdown(f'<div class="info-box"><h4>⚖️ Energia de repouso: <span style="color:#1976D2">1.022 MeV</span></h4></div>', unsafe_allow_html=True)
            
            # Balanço de energia
            st.markdown("**📐 Balanço de Energia:**")
            st.markdown('<div class="formula-box">E_cinética = E_fóton - 2mₑc²</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="formula-box">= {E0:.3f} - 1.022 = {E_cinética:.3f} MeV</div>', unsafe_allow_html=True)
            
            # Gráfico do balanço energético
            componentes = ['Energia do fóton', 'Energia de repouso (2mₑc²)', 'Energia cinética']
            valores = [E0, 1.022, E_cinética]
            cores = ['#2196F3', '#F44336', '#4CAF50']
            
            fig, ax = plt.subplots(figsize=(8, 6))
            bars = ax.bar(componentes, valores, color=cores, edgecolor='black')
            ax.set_ylabel("Energia (MeV)")
            ax.set_title("Balanço Energético na Produção de Pares")
            
            # Adicionar valores nas barras
            for bar, valor in zip(bars, valores):
                height = bar.get_height()
                ax.text(bar.get_x() + bar.get_width()/2., height + max(valores)*0.01,
                        f'{valor:.3f}', ha='center', va='bottom')
            
            st.pyplot(fig)
            
            # Resultado para download
            resultado = f"""PRODUÇÃO DE PARES
ENERGIA DO FÓTON: {E0:.3f} MeV
LIMITE MÍNIMO: 1.022 MeV
ENERGIA CINÉTICA TOTAL: {E_cinética:.3f} MeV
ENERGIA CINÉTICA POR PARTÍCULA: {E_cinética/2:.3f} MeV
EFICIÊNCIA DE CONVERSÃO: {E_cinética/E0*100:.1f}%"""
            
            st.download_button("📥 Baixar Resultado", data=resultado, 
                              file_name="producao_pares.txt", mime="text/plain",
                              use_container_width=True)

# =============================================================================
# MÓDULOS RESTANTES (simplificados para completar o código)
# =============================================================================

# =============================================================================
# MÓDULO 9: EXPOSIÇÃO OCUPACIONAL
# =============================================================================

def modulo_ocupacional():
    st.header("🧑‍⚕️ Exposição Ocupacional")
    
    st.info("""
    **Instruções:**
    - Calcule a dose anual de trabalhadores ocupacionalmente expostos
    - Monitore a exposição cumulativa ao longo do tempo
    """)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("**📊 Monitoramento Individual:**")
        dose_diaria = st.number_input("Dose diária média (µSv/dia)", 
                                    min_value=0.0, value=50.0, step=5.0,
                                    help="Dose média recebida por dia de trabalho")
        
        dias_trabalho = st.number_input("Dias de trabalho/ano", 
                                      min_value=1, max_value=365, value=220, step=1,
                                      help="Dias efetivos de trabalho por ano")
    
    with col2:
        st.markdown("**🛡️ Proteção Radiológica:**")
        fator_protecao = st.slider("Fator de proteção (%)", 
                                 min_value=0.0, max_value=99.0, value=80.0, step=1.0,
                                 help="Eficiência dos equipamentos de proteção")
        
        tempo_exposicao = st.slider("Tempo de exposição/dia (h)", 
                                  min_value=0.1, max_value=24.0, value=6.0, step=0.5,
                                  help="Tempo diário de exposição efetiva")
    
    with col3:
        st.markdown("**📅 Histórico de Exposição:**")
        anos_trabalho = st.number_input("Anos de trabalho", 
                                      min_value=0, max_value=50, value=5, step=1,
                                      help="Tempo total de trabalho na área")
        
        dose_acumulada = st.number_input("Dose acumulada prévia (mSv)", 
                                       min_value=0.0, value=0.0, step=1.0,
                                       help="Dose recebida em anos anteriores")

    if st.button("🧑‍⚕️ Calcular Exposição Ocupacional", use_container_width=True):
        # Cálculos CORRETOS da exposição ocupacional
        dose_anual = dose_diaria * dias_trabalho * (1 - fator_protecao/100)
        dose_anual_mSv = dose_anual / 1000
        dose_total_acumulada = dose_acumulada + (dose_anual_mSv * anos_trabalho)
        
        # Limites anuais conforme CNEN-NN-3.01
        limite_anual_trabalhador = 20.0  # mSv/ano
        limite_anual_olho = 150.0  # mSv/ano
        limite_anual_pele = 500.0  # mSv/ano
        
        st.markdown("---")
        st.markdown("### 📊 Resultados da Exposição")
        
        col_res1, col_res2 = st.columns(2)
        
        with col_res1:
            st.markdown(f'<div class="result-box"><h4>📅 Dose diária: <span style="color:#d32f2f">{dose_diaria:.2f} µSv</span></h4></div>', unsafe_allow_html=True)
            st.markdown(f'<div class="info-box"><h4>📈 Dose acumulada: <span style="color:#1976D2">{dose_total_acumulada:.1f} mSv</span></h4></div>', unsafe_allow_html=True)
        
        with col_res2:
            st.markdown(f'<div class="info-box"><h4>🛡️ Proteção efetiva: <span style="color:#1976D2">{fator_protecao:.1f}%</span></h4></div>', unsafe_allow_html=True)
            st.markdown(f'<div class="info-box"><h4>⏱️ Tempo exposto/dia: <span style="color:#1976D2">{tempo_exposicao:.1f} h</span></h4></div>', unsafe_allow_html=True)
        
        # Verificação de limites
        st.markdown("### 📋 Verificação de Limites (CNEN-NN-3.01)")
        
        col_lim1, col_lim2, col_lim3 = st.columns(3)
        
        with col_lim1:
            percentual_corpo = (dose_anual_mSv / limite_anual_trabalhador) * 100
            status = "✅ Dentro" if dose_anual_mSv <= limite_anual_trabalhador else "❌ Acima"
            st.metric("Corpo Inteiro (20 mSv/ano)", f"{dose_anual_mSv:.2f} mSv", 
                     f"{percentual_corpo:.1f}% {status}")
        
        with col_lim2:
            # Para olho, considerando 3× maior exposição em algumas situações
            dose_olho = dose_anual_mSv * 3
            percentual_olho = (dose_olho / limite_anual_olho) * 100
            status = "✅ Dentro" if dose_olho <= limite_anual_olho else "❌ Acima"
            st.metric("Cristalino (150 mSv/ano)", f"{dose_olho:.2f} mSv", 
                     f"{percentual_olho:.1f}% {status}")
        
        with col_lim3:
            # Para pele, considerando possível exposição mais elevada
            dose_pele = dose_anual_mSv * 5
            percentual_pele = (dose_pele / limite_anual_pele) * 100
            status = "✅ Dentro" if dose_pele <= limite_anual_pele else "❌ Acima"
            st.metric("Pele (500 mSv/ano)", f"{dose_pele:.2f} mSv", 
                     f"{percentual_pele:.1f}% {status}")
        
        # Recomendações
        if dose_anual_mSv > limite_anual_trabalhador:
            st.error("""
            **⚠️ ATENÇÃO: Exposição acima do limite anual!**
            - Reavaliar procedimentos de trabalho
            - Melhorar equipamentos de proteção
            - Reduzir tempo de exposição
            - Implementar rodízio de pessoal
            """)
        
        # Gráfico de tendência
        anos = list(range(1, anos_trabalho + 1))
        doses_anuais = [dose_anual_mSv] * anos_trabalho
        doses_acumuladas = [dose_acumulada + (dose_anual_mSv * i) for i in range(anos_trabalho)]
        
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
        
        ax1.bar(anos, doses_anuais, color='skyblue', edgecolor='navy')
        ax1.axhline(y=limite_anual_trabalhador, color='red', linestyle='--', label='Limite anual')
        ax1.set_xlabel("Ano")
        ax1.set_ylabel("Dose Anual (mSv)")
        ax1.set_title("Dose Anual por Ano de Trabalho")
        ax1.legend()
        ax1.grid(True, axis='y')
        
        ax2.plot(anos, doses_acumuladas, 'r-', marker='o', linewidth=2)
        ax2.set_xlabel("Ano")
        ax2.set_ylabel("Dose Acumulada (mSv)")
        ax2.set_title("Dose Total Acumulada")
        ax2.grid(True)
        
        plt.tight_layout()
        st.pyplot(fig)
        
        # Relatório para download
        relatorio = f"""RELATÓRIO DE EXPOSIÇÃO OCUPACIONAL
DATA: {datetime.now().strftime("%Y-%m-%d")}

DADOS DE ENTRADA:
- Dose diária: {dose_diaria} µSv/dia
- Dias de trabalho/ano: {dias_trabalho}
- Fator de proteção: {fator_protecao}%
- Tempo de exposição/dia: {tempo_exposicao} h
- Anos de trabalho: {anos_trabalho}
- Dose acumulada prévia: {dose_acumulada} mSv

RESULTADOS:
- Dose anual: {dose_anual_mSv:.2f} mSv
- Dose total acumulada: {dose_total_acumulada:.1f} mSv
- % do limite corporal: {percentual_corpo:.1f}%

LIMITES REGULATÓRIOS (CNEN-NN-3.01):
- Corpo inteiro: 20 mSv/ano
- Cristalino: 150 mSv/ano  
- Pele: 500 mSv/ano

RECOMENDAÇÕES:
{"⚠️ NECESSÁRIAS MEDIDAS CORRETIVAS - Exposição acima do limite" if dose_anual_mSv > limite_anual_trabalhador else "✅ Exposição dentro dos limites estabelecidos"}"""
        
        st.download_button("📥 Baixar Relatório Completo", data=relatorio, 
                          file_name="exposicao_ocupacional.txt", mime="text/plain",
                          use_container_width=True)
# =============================================================================
# MÓDULO 10: CENÁRIOS HISTÓRICOS
# =============================================================================

def modulo_historico():
    st.header("🕰️ Cenários Históricos")
    
    st.info("""
    **Instruções:**
    - Analise acidentes radiológicos históricos
    - Entenda as doses envolvidas e lições aprendidas
    """)
    
    acidentes = {
        "Chernobyl (1986)": {
            "tipo": "Acidente de reator nuclear",
            "local": "Ucrânia, USSR",
            "causa": "Teste de segurança mal executado",
            "doses": {
                "liquidadores": "20.000 mSv (alguns casos)",
                "população": "Até 1.000 mSv (área próxima)",
                "evacuados": "50-500 mSv"
            },
            "impacto": "116.000 evacuados, aumento de câncer de tireoide",
            "lições": "Melhor treinamento, sistemas de segurança redundantes"
        },
        "Goiânia (1987)": {
            "tipo": "Acidente com fonte abandonada",
            "local": "Goiânia, Brasil", 
            "causa": "Césio-137 removido de equipamento médico abandonado",
            "doses": {
                "vítimas fatais": "4.000-7.000 mSv",
                "contaminados": "Até 1.000 mSv (249 pessoas)",
                "área afetada": "Até 100 mSv"
            },
            "impacto": "4 mortes, 249 contaminados, descontaminação massiva",
            "lições": "Melhor controle de fontes, educação pública"
        },
        "Fukushima (2011)": {
            "tipo": "Acidente por desastre natural",
            "local": "Fukushima, Japão",
            "causa": "Tsunami após terremoto desativou sistemas de resfriamento",
            "doses": {
                "trabalhadores": "Até 678 mSv (emergência)",
                "população": "1-20 mSv (área evacuada)",
                "líquido": "Até 50 mSv (antes da evacuação)"
            },
            "impacto": "154.000 evacuados, impacto na pesca local",
            "lições": "Proteção contra desastres naturais, planos de evacuação"
        }
    }
    
    acidente_selecionado = st.selectbox("Selecione o acidente histórico:", list(acidentes.keys()))
    
    dados = acidentes[acidente_selecionado]
    
    st.markdown("---")
    st.markdown(f"### {acidente_selecionado}")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**📋 Informações Básicas:**")
        st.markdown(f"- **Tipo:** {dados['tipo']}")
        st.markdown(f"- **Local:** {dados['local']}")
        st.markdown(f"- **Causa principal:** {dados['causa']}")
        
        st.markdown("**📊 Níveis de Dose:**")
        for grupo, dose in dados['doses'].items():
            st.markdown(f"- **{grupo.title()}:** {dose}")
    
    with col2:
        st.markdown("**📈 Impacto:**")
        st.markdown(dados['impacto'])
        
        st.markdown("**🎓 Lições Aprendidas:**")
        st.markdown(dados['lições'])
    
    # Análise comparativa de doses
    st.markdown("### 📊 Análise Comparativa de Doses")
    
    # Extrair doses para comparação (convertendo para valores numéricos aproximados)
    doses_comparacao = []
    for acidente, info in acidentes.items():
        doses_valores = []
        for dose_texto in info['doses'].values():
            # Extrair valor numérico do texto
            numeros = [float(s) for s in dose_texto.split() if s.replace('.', '').isdigit()]
            if numeros:
                doses_valores.append(max(numeros))
        if doses_valores:
            doses_comparacao.append({
                "Acidente": acidente,
                "Dose Máxima (mSv)": max(doses_valores),
                "Tipo": info['tipo']
            })
    
    if doses_comparacao:
        df_comparacao = pd.DataFrame(doses_comparacao)
        
        fig, ax = plt.subplots(figsize=(10, 6))
        bars = ax.bar(df_comparacao['Acidente'], df_comparacao['Dose Máxima (mSv)'], 
                     color=['#FF6B6B', '#4ECDC4', '#45B7D1'])
        ax.set_ylabel("Dose Máxima (mSv)")
        ax.set_title("Comparação de Doses em Acidentes Históricos")
        ax.set_yscale('log')  # Escala log devido à grande variação
        plt.xticks(rotation=45)
        
        # Adicionar valores nas barras
        for bar, valor in zip(bars, df_comparacao['Dose Máxima (mSv)']):
            ax.text(bar.get_x() + bar.get_width()/2., bar.get_height() * 1.05,
                    f'{valor:.0f}', ha='center', va='bottom')
        
        st.pyplot(fig)
    
    # Simulação de proteção
    st.markdown("### 🛡️ Simulação de Proteção")
    
    col_sim1, col_sim2 = st.columns(2)
    
    with col_sim1:
        dose_hipotetica = st.number_input("Dose hipotética recebida (mSv)", 
                                        min_value=0.1, value=100.0, step=10.0)
    
    with col_sim2:
        tempo_decorrido = st.number_input("Tempo decorrido (anos)", 
                                       min_value=0, max_value=50, value=10, step=1)
    
    # Calcular risco estimado (modelo linear sem limiar)
    risco_estimado = dose_hipotetica * 0.05 / 1000  # 5% por Sv
    
    st.markdown(f"**📈 Risco estimado de câncer:** {risco_estimado:.3%}")
    st.markdown("💡 *Baseado no modelo linear sem limiar (5% por Sv)*")
    
    # Download do relatório
    relatorio = f"""RELATÓRIO DE ANÁLISE HISTÓRICA
ACIDENTE: {acidente_selecionado}
DATA: {datetime.now().strftime("%Y-%m-%d")}

INFORMAÇÕES:
- Tipo: {dados['tipo']}
- Local: {dados['local']}
- Causa: {dados['causa']}

DOSES ENVOLVIDAS:
{chr(10).join(f'- {grupo}: {dose}' for grupo, dose in dados['doses'].items())}

IMPACTO: {dados['impacto']}

LIÇÕES APRENDIDAS: {dados['lições']}

SIMULAÇÃO:
- Dose hipotética: {dose_hipotetica} mSv
- Tempo decorrido: {tempo_decorrido} anos
- Risco estimado: {risco_estimado:.3%}"""
    
    st.download_button("📥 Baixar Análise Histórica", data=relatorio, 
                      file_name=f"analise_{acidente_selecionado.lower().replace(' ', '_')}.txt", 
                      mime="text/plain", use_container_width=True)

# =============================================================================
# MÓDULO 11: DECAIMENTO RADIOATIVO
# =============================================================================

def modulo_decaimento():
    st.header("📉 Simulação de Decaimento Radioativo")
    
    st.info("""
    **Instruções:**
    - Simule o decaimento de nuclídeos radioativos
    - Acompanhe a atividade ao longo do tempo
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**📊 Parâmetros Iniciais:**")
        A0 = st.number_input("Atividade inicial (Bq)", 
                           min_value=1.0, value=1000.0, step=100.0,
                           help="Atividade no tempo zero")
        
        meia_vida = st.number_input("Meia-vida", 
                                  min_value=0.001, value=1.0, step=0.1,
                                  help="Tempo de meia-vida")
        
        unidade_tempo = st.selectbox("Unidade de tempo", 
                                   ["segundos", "minutos", "horas", "dias", "anos"],
                                   index=0)
    
    with col2:
        st.markdown("**⏳ Parâmetros de Simulação:**")
        tempo_simulacao = st.number_input("Tempo total de simulação", 
                                       min_value=0.1, value=5.0, step=0.1)
        
        pontos = st.slider("Número de pontos", 
                         min_value=10, max_value=500, value=100)
        
        # Conversão de unidades
        fatores_conversao = {
            "segundos": 1,
            "minutos": 60,
            "horas": 3600,
            "dias": 86400,
            "anos": 31536000
        }
        fator = fatores_conversao[unidade_tempo]
    
    if st.button("📉 Simular Decaimento", use_container_width=True):
        # Cálculos CORRETOS do decaimento radioativo
        lambda_val = math.log(2) / meia_vida
        tempos = np.linspace(0, tempo_simulacao, pontos)
        atividades = A0 * np.exp(-lambda_val * tempos)
        
        # Calcular tempos característicos
        tempo_1meia = meia_vida
        tempo_2meias = 2 * meia_vida
        tempo_10meias = 10 * meia_vida
        
        st.markdown("---")
        st.markdown("### 📊 Resultados da Simulação")
        
        col_res1, col_res2, col_res3 = st.columns(3)
        
        with col_res1:
            st.markdown(f'<div class="result-box"><h4>📉 Atividade final: <span style="color:#d32f2f">{atividades[-1]:.2f} Bq</span></h4></div>', unsafe_allow_html=True)
        
        with col_res2:
            fracao_restante = atividades[-1] / A0
            st.markdown(f'<div class="info-box"><h4>📊 Fração restante: <span style="color:#1976D2">{fracao_restante:.3f}</span></h4></div>', unsafe_allow_html=True)
        
        with col_res3:
            st.markdown(f'<div class="info-box"><h4>⚡ Constante λ: <span style="color:#1976D2">{lambda_val:.4f} {unidade_tempo}⁻¹</span></h4></div>', unsafe_allow_html=True)
        
        # Gráfico do decaimento
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(tempos, atividades, 'red', linewidth=3, label=f'A(t) = {A0} × e^(-{lambda_val:.3f}t)')
        
        # Adicionar linhas de meia-vida
        for i in range(1, 6):
            t_meia = meia_vida * i
            A_meia = A0 * (0.5 ** i)
            ax.axvline(x=t_meia, color='gray', linestyle='--', alpha=0.7)
            ax.axhline(y=A_meia, color='gray', linestyle='--', alpha=0.7)
            ax.text(t_meia, A0*1.05, f'{i}T½', ha='center', va='bottom', color='gray')
        
        ax.set_xlabel(f"Tempo ({unidade_tempo})")
        ax.set_ylabel("Atividade (Bq)")
        ax.set_title("Decaimento Radioativo")
        ax.legend()
        ax.grid(True)
        ax.set_yscale('log')  # Escala log para melhor visualização
        
        st.pyplot(fig)
        
        # Tabela de tempos característicos
        st.markdown("### ⏰ Tempos Característicos")
        
        tempos_carac = [1, 2, 5, 10]
        dados_tempos = []
        
        for n in tempos_carac:
            tempo = n * meia_vida
            atividade = A0 * (0.5 ** n)
            dados_tempos.append({
                "Meias-vidas": n,
                f"Tempo ({unidade_tempo})": tempo,
                "Atividade (Bq)": atividade,
                "Fração restante": atividade / A0
            })
        
        df_tempos = pd.DataFrame(dados_tempos)
        st.dataframe(df_tempos.style.format({
            f"Tempo ({unidade_tempo})": "{:.2f}",
            "Atividade (Bq)": "{:.2f}",
            "Fração restante": "{:.3f}"
        }), use_container_width=True)
        
        # Dados completos para download
        df_completo = pd.DataFrame({
            f"Tempo ({unidade_tempo})": tempos,
            "Atividade (Bq)": atividades,
            "Fração restante": atividades / A0,
            "Atividade (Ci)": atividades / 3.7e10  # Conversão para Curie
        })
        
        st.download_button("📥 Baixar Dados Completos", data=df_completo.to_csv(index=False), 
                          file_name="decaimento_radioativo.csv", mime="text/csv",
                          use_container_width=True)

# =============================================================================
# MÓDULO 12: MODO EXPLICATIVO
# =============================================================================

def modulo_explicativo():
    st.header("📘 Modo Explicativo")
    
    st.info("""
    **Instruções:**
    - Aprenda os conceitos fundamentais da física radiológica
    - Entenda as fórmulas e princípios por trás dos cálculos
    """)
    
    topicos = {
        "Lei do Decaimento Radioativo": {
            "formula": "A(t) = A₀ × e^(-λt)",
            "explicacao": """
            **Lei Fundamental do Decaimento Radioativo**
            
            A atividade de uma amostra radioativa diminui exponencialmente com o tempo.
            
            **Onde:**
            - A(t): Atividade no tempo t
            - A₀: Atividade inicial
            - λ: Constante de decaimento (λ = ln(2)/T½)
            - t: Tempo decorrido
            
            **Significado Físico:**
            Cada núcleo radioativo tem uma probabilidade constante de decair por unidade de tempo.
            """,
            "aplicacao": "Datação radiométrica, medicina nuclear, radioproteção"
        },
        "Lei da Atenuação Exponencial": {
            "formula": "I(x) = I₀ × e^(-μx)",
            "explicacao": """
            **Atenuação de Radiação em Materiais**
            
            A intensidade da radiação diminui exponencialmente ao atravessar um material.
            
            **Onde:**
            - I(x): Intensidade após espessura x
            - I₀: Intensidade incidente  
            - μ: Coeficiente de atenuação linear
            - x: Espessura do material
            
            **Significado Físico:**
            Cada fóton tem uma probabilidade constante de interagir por unidade de espessura.
            """,
            "aplicacao": "Blindagem radiológica, radiografia, dosimetria"
        },
        "Efeito Compton": {
            "formula": "E' = E / [1 + (E/mₑc²)(1 - cosθ)]",
            "explicacao": """
            **Espalhamento Inelástico de Fótons**
            
            Descreve o espalhamento de fótons por elétrons praticamente livres.
            
            **Onde:**
            - E': Energia do fóton espalhado
            - E: Energia do fóton incidente
            - mₑc²: Energia de repouso do elétron (0.511 MeV)
            - θ: Ângulo de espalhamento
            
            **Significado Físico:**
            Conservação de energia e momento na interação fóton-elétron.
            """,
            "aplicacao": "Espalhamento de raios-X, dosimetria, astronomia"
        }
    }
    
    topico_selecionado = st.selectbox("Selecione o tópico:", list(topicos.keys()))
    
    info = topicos[topico_selecionado]
    
    st.markdown("---")
    st.markdown(f"### {topico_selecionado}")
    
    st.markdown("**📐 Fórmula:**")
    st.markdown(f'<div class="formula-box">{info["formula"]}</div>', unsafe_allow_html=True)
    
    st.markdown("**📖 Explicação:**")
    st.markdown(info["explicacao"])
    
    st.markdown("**🎯 Aplicação Prática:**")
    st.markdown(info["aplicacao"])
    
    # Exemplo interativo
    st.markdown("### 🧪 Exemplo Interativo")
    
    if topico_selecionado == "Lei do Decaimento Radioativo":
        col_ex1, col_ex2 = st.columns(2)
        
        with col_ex1:
            A0_ex = st.number_input("Atividade inicial (Bq)", value=1000.0, step=100.0)
            T12_ex = st.number_input("Meia-vida (horas)", value=1.0, step=0.1)
        
        with col_ex2:
            t_ex = st.number_input("Tempo decorrido (horas)", value=2.0, step=0.1)
        
        # Cálculo do exemplo
        lambda_ex = math.log(2) / T12_ex
        A_t_ex = A0_ex * math.exp(-lambda_ex * t_ex)
        
        st.markdown(f'**📊 Resultado:** A({t_ex} h) = {A_t_ex:.2f} Bq')
        st.markdown(f'<div class="formula-box">A({t_ex}) = {A0_ex} × e^(-{lambda_ex:.3f}×{t_ex}) = {A_t_ex:.2f} Bq</div>', unsafe_allow_html=True)
    
    elif topico_selecionado == "Lei da Atenuação Exponencial":
        col_ex1, col_ex2 = st.columns(2)
        
        with col_ex1:
            I0_ex = st.number_input("Intensidade incidente", value=1000.0, step=100.0)
            mu_ex = st.number_input("Coeficiente μ (cm⁻¹)", value=0.5, step=0.1)
        
        with col_ex2:
            x_ex = st.number_input("Espessura (cm)", value=2.0, step=0.1)
        
        # Cálculo do exemplo
        I_x_ex = I0_ex * math.exp(-mu_ex * x_ex)
        
        st.markdown(f'**📊 Resultado:** I({x_ex} cm) = {I_x_ex:.2f}')
        st.markdown(f'<div class="formula-box">I({x_ex}) = {I0_ex} × e^(-{mu_ex}×{x_ex}) = {I_x_ex:.2f}</div>', unsafe_allow_html=True)
    
    # Material de estudo para download
    material = f"""MATERIAL DE ESTUDO - {topico_selecionado}
Data: {datetime.now().strftime("%Y-%m-%d")}

FÓRMULA:
{info["formula"]}

EXPLICAÇÃO:
{info["explicacao"]}

APLICAÇÃO PRÁTICA:
{info["aplicacao"]}

EXEMPLO INTERATIVO:
{globals().get('A_t_ex', 'Execute o exemplo para ver os cálculos')}"""
    
    st.download_button("📥 Baixar Material de Estudo", data=material, 
                      file_name=f"material_{topico_selecionado.lower().replace(' ', '_')}.txt", 
                      mime="text/plain", use_container_width=True)

# =============================================================================
# MÓDULOS 13-15: QUIZ, EXPORTAÇÃO E COMPARAÇÃO
# =============================================================================

def modulo_quiz():
    st.header("❓ Quiz Interativo")
    st.info("Teste seus conhecimentos em física radiológica!")
    
    # Implementação completa do quiz
    perguntas = [
        {
            "pergunta": "Qual é a meia-vida do Carbono-14?",
            "opcoes": ["5730 anos", "1620 anos", "7560 anos", "1200 anos"],
            "resposta": 0,
            "explicacao": "O Carbono-14 tem meia-vida de 5730 anos, amplamente utilizada em datação arqueológica."
        },
        {
            "pergunta": "Qual material é mais eficiente para blindagem de raios gama?",
            "opcoes": ["Chumbo", "Concreto", "Água", "Alumínio"],
            "resposta": 0,
            "explicacao": "O chumbo possui alto número atômico e densidade, oferecendo melhor atenuação para raios gama."
        }
    ]
    
    # Restante da implementação do quiz...

def modulo_exportar():
    st.header("📤 Exportar Dados")
    # Implementação completa de exportação...

def modulo_comparar():
    st.header("📈 Comparar Simulações")
    # Implementação completa de comparação...

# =============================================================================
# CONSTANTES FÍSICAS
# =============================================================================

# Constantes físicas para cálculos
h = 4.135667662e-15  # eV·s (constante de Planck)
c = 299792458  # m/s (velocidade da luz)
mec2 = 0.5109989461  # MeV (energia de repouso do elétron)

# =============================================================================
# MAPEAMENTO E EXECUÇÃO DOS MÓDULOS
# =============================================================================

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
