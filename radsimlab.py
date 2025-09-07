import streamlit as st
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="RadSimLab", layout="centered")
st.title("🔬 RadSimLab – Simulador Radiológico")

modulos = {
    "Datação Radiométrica": "datacao_radiometrica",
    "Blindagem": "blindagem",
    "Radioterapia": "radioterapia",
    "Distribuição de Dose": "dose",
    "Aplicações Clínicas": "clinico",
    "Aplicações Ambientais": "ambiental",
    "Compton": "compton",
    "Produção de Pares": "pares",
    "Exposição Ocupacional": "ocupacional",
    "Cenários Históricos": "historico",
    "Modo Explicativo": "explicativo",
    "Quiz Interativo": "quiz",
    "Exportar Dados": "exportar",
    "Comparar Simulações": "comparar"
}

modulo = st.sidebar.selectbox("📁 Escolha o módulo", list(modulos.keys()))

def carregar_modulo(nome):
    if nome == "datacao_radiometrica": modulo_datacao_radiometrica()
    elif nome == "blindagem": modulo_blindagem()
    elif nome == "radioterapia": modulo_radioterapia()
    elif nome == "dose": modulo_dose()
    elif nome == "clinico": modulo_clinico()
    elif nome == "ambiental": modulo_ambiental()
    elif nome == "compton": modulo_compton()
    elif nome == "pares": modulo_pares()
    elif nome == "ocupacional": modulo_ocupacional()
    elif nome == "historico": modulo_historico()
    elif nome == "explicativo": modulo_explicativo()
    elif nome == "quiz": modulo_quiz()
    elif nome == "exportar": modulo_exportar()
    elif nome == "comparar": modulo_comparar()

# ⏳ Datação Radiométrica com submenu
def modulo_datacao_radiometrica():
    st.subheader("⏳ Datação Radiométrica")
    metodo = st.radio("Escolha o método:", ["Carbono-14", "Potássio-Argônio", "Urânio-Chumbo"])
    if metodo == "Carbono-14": modulo_carbono14()
    elif metodo == "Potássio-Argônio": modulo_potassio_argonio()
    elif metodo == "Urânio-Chumbo": modulo_uranio_chumbo()

def modulo_carbono14():
    st.markdown("### 🧪 Carbono-14")
    f = st.number_input("Fração atual de C-14 (0 < f < 1)", min_value=0.0001, max_value=0.9999, value=0.5)
    l = st.number_input("Constante de decaimento λ (anos⁻¹)", min_value=0.000001, value=0.000121)
    if st.button("Calcular Carbono-14"):
        idade = -math.log(f) / l
        st.success(f"🧪 Idade estimada: {idade:.2f} anos")
        st.markdown("📐 Equação: `t = -ln(f) / λ`")

def modulo_potassio_argonio():
    st.markdown("### ⛏️ Potássio-Argônio")
    R = st.number_input("Razão Ar/K medida", min_value=0.01, value=0.5)
    l = st.number_input("Constante de decaimento λ (anos⁻¹)", min_value=0.000001, value=0.000125)
    if st.button("Calcular Potássio-Argônio"):
        idade = (1 / l) * math.log(1 + R)
        st.success(f"⛏️ Idade estimada: {idade:.2f} anos")
        st.markdown("📐 Equação: `t = (1 / λ) · ln(1 + R)`")

def modulo_uranio_chumbo():
    st.markdown("### ⛏️ Urânio-Chumbo")
    R = st.number_input("Razão Pb/U medida", min_value=0.01, value=0.5)
    l = st.number_input("Constante de decaimento λ (anos⁻¹)", min_value=0.000001, value=0.000155)
    if st.button("Calcular Urânio-Chumbo"):
        idade = (1 / l) * math.log(R + 1)
        st.success(f"⛏️ Idade estimada: {idade:.2f} anos")
        st.markdown("📐 Equação: `t = (1 / λ) · ln(R + 1)`")

def modulo_blindagem():
    st.subheader("🧱 Cálculo de Blindagem Radiológica")
    I0 = st.number_input("Dose inicial (µSv/h)", min_value=0.01, value=100.0)
    I = st.number_input("Dose desejada (µSv/h)", min_value=0.01, value=10.0)
    mu = st.number_input("Coeficiente de atenuação μ (cm⁻¹)", min_value=0.001, value=0.15)
    if st.button("Calcular Blindagem"):
        x = (1 / mu) * math.log(I0 / I)
        st.success(f"🧱 Espessura mínima: {x:.2f} cm")
        st.markdown("📐 Equação: `x = (1 / μ) · ln(I₀ / I)`")

def modulo_radioterapia():
    st.subheader("📅 Planejamento Radioterápico")
    D = st.number_input("Dose prescrita (Gy)", min_value=0.1, value=60.0)
    R = st.number_input("Taxa de dose (Gy/min)", min_value=0.01, value=2.0)
    N = st.number_input("Número de sessões", min_value=1, value=30)
    if st.button("Calcular Radioterapia"):
        dps = D / N
        tps = dps / R
        st.success(f"💉 Dose por sessão: {dps:.2f} Gy")
        st.info(f"⏱️ Tempo por sessão: {tps:.2f} min")

def modulo_dose():
    st.subheader("📊 Distribuição de Dose em Tecido")
    D0 = st.number_input("Dose na superfície (Gy)", min_value=0.1, value=10.0)
    mu = st.number_input("Coef. de atenuação (cm⁻¹)", min_value=0.01, value=0.2)
    max_depth = st.number_input("Profundidade máxima (cm)", min_value=1, value=10)
    if st.button("Calcular Distribuição"):
        profundidades = list(range(0, int(max_depth)+1))
        doses = [D0 * math.exp(-mu * x) for x in profundidades]
        for x, d in zip(profundidades, doses):
            st.write(f"x = {x} cm → Dose = {d:.2f} Gy")
        st.markdown("📐 Equação: `D(x) = D₀ · e^(–μx)`")
        fig, ax = plt.subplots()
        ax.plot(profundidades, doses, marker='o')
        ax.set_title("Distribuição de Dose")
        ax.set_xlabel("Profundidade (cm)")
        ax.set_ylabel("Dose (Gy)")
        st.pyplot(fig)

def modulo_clinico():
    st.subheader("🧬 Distribuição de Tc-99m em Órgãos")
    D = st.number_input("Dose administrada (MBq)", min_value=0.1, value=100.0)
    F = st.number_input("Fração fixa (%)", min_value=0.1, max_value=100.0, value=20.0)
    H = st.number_input("Meia-vida (h)", min_value=0.1, value=6.0)
    T = st.number_input("Tempo após administração (h)", min_value=0.0, value=2.0)
    if st.button("Calcular Tc-99m"):
        lambda_ = math.log(2) / H
        A = D * (F / 100) * math.exp(-lambda_ * T)
        st.success(f"🧬 Atividade no órgão: {A:.2f} MBq")
        st.markdown("📐 Equação: `A = D · F · e^(–λt)`")

def modulo_ambiental():
    st.subheader("🌱 Exposição Ambiental à Radiação")
    taxa_solo = st.number_input("Taxa no solo (µSv/h)", min_value=0.0, value=1.0)
    tempo_solo = st.number_input("Tempo no solo (h)", min_value=0.0, value=5.0)
    taxa_ar = st.number_input("Taxa no ar (µSv/h)", min_value=0.0, value=0.5)
    tempo_ar = st.number_input("Tempo no ar (h)", min_value=0.0, value=3.0)

    if st.button("Calcular Exposição Ambiental"):
        dose_solo = taxa_solo * tempo_solo
        dose_ar = taxa_ar * tempo_ar
        total = dose_solo + dose_ar
        st.success(f"🌱 Dose no solo: {dose_solo:.2f} µSv")
        st.info(f"🌬️ Dose no ar: {dose_ar:.2f} µSv")
        st.write(f"📊 Dose total: {total:.2f} µSv")
def modulo_compton():
    st.subheader("🔄 Espalhamento Compton")
    E = st.number_input("Energia do fóton (MeV)", min_value=0.01, value=1.0)
    angulo = st.number_input("Ângulo de espalhamento (°)", min_value=0.0, max_value=180.0, value=90.0)
    if st.button("Calcular Compton"):
        mec2 = 0.511
        theta_rad = math.radians(angulo)
        Efinal = E / (1 + (E / mec2) * (1 - math.cos(theta_rad)))
        transferida = E - Efinal
        st.success(f"🔄 Energia espalhada: {Efinal:.3f} MeV")
        st.info(f"⚡ Energia transferida: {transferida:.3f} MeV")
        st.markdown("📐 Equação: `E' = E / [1 + (E / 0.511)(1 – cosθ)]`")

def modulo_pares():
    st.subheader("⚡ Produção de Pares")
    E = st.number_input("Energia do fóton (MeV)", min_value=0.0, value=2.0)
    if st.button("Calcular Pares"):
        if E <= 1.022:
            st.error("❌ Energia insuficiente para produção de pares")
        else:
            Ecin = E - 1.022
            st.success(f"⚡ Energia cinética total: {Ecin:.3f} MeV")
            st.markdown("📐 Equação: `Eₖ = E – 1.022`")

def modulo_ocupacional():
    st.subheader("🧑‍⚕️ Exposição Ocupacional")
    taxa = st.number_input("Taxa diária (µSv/dia)", min_value=0.0, value=5.0)
    dias = st.number_input("Dias por ano", min_value=1, value=250)
    fator = st.slider("Fator de proteção (0–1)", min_value=0.0, max_value=1.0, value=0.2)
    if st.button("Calcular Ocupacional"):
        dose = taxa * dias * (1 - fator)
        st.success(f"🧑‍⚕️ Dose anual estimada: {dose:.2f} µSv")

def modulo_historico():
    st.subheader("🕰️ Cenários Históricos")
    evento = st.selectbox("Escolha o evento", ["Chernobyl", "Goiânia", "Fukushima"])
    dados = {
        "Chernobyl": "1986: Liberação de 5.2 milhões de curies. Zona de exclusão de 30 km.",
        "Goiânia": "1987: Acidente com Césio-137. 249 contaminados, 4 mortes.",
        "Fukushima": "2011: Vazamento após tsunami. Evacuação em massa."
    }
    st.info(f"{evento}: {dados[evento]}")

def modulo_explicativo():
    st.subheader("📘 Modo Explicativo")
    tema = st.selectbox("Escolha o tema", ["Carbono-14", "Blindagem", "Compton"])
    explicacoes = {
        "Carbono-14": "Isótopo usado para datação. Meia-vida ≈ 5730 anos.",
        "Blindagem": "Uso de materiais densos para atenuar radiação exponencialmente.",
        "Compton": "Espalhamento de fótons por elétrons com perda de energia."
    }
    st.markdown(f"📚 {tema}: {explicacoes[tema]}")

def modulo_quiz():
    st.subheader("❓ Quiz Interativo")
    r1 = st.text_input("Carbono-14: Qual é a meia-vida?")
    r2 = st.text_input("Blindagem: Material mais eficiente?")
    if st.button("Verificar Quiz"):
        acertos = 0
        if r1.strip() == "5730": acertos += 1
        if r2.strip().lower() == "chumbo": acertos += 1
        st.success(f"✅ Você acertou {acertos} de 2 perguntas.")

def modulo_exportar():
    st.subheader("📤 Exportar Dados")
    texto = st.text_area("Insira os dados para exportar")
    if texto:
        linhas = texto.strip().split("\n")
        preview = "\n".join(linhas[:5])
        st.write(f"📄 Preview:\n{preview}")
        st.download_button("📥 Baixar TXT", data=texto, file_name="dados.txt", mime="text/plain")

def modulo_comparar():
    st.subheader("📈 Comparar Simulações")
    A = st.text_input("Simulação A (valores separados por vírgula)")
    B = st.text_input("Simulação B (valores separados por vírgula)")
    if st.button("Comparar Simulações"):
        try:
            listaA = [float(x) for x in A.split(",") if x.strip()]
            listaB = [float(x) for x in B.split(",") if x.strip()]
            mA = np.mean(listaA)
            mB = np.mean(listaB)
            st.success(f"📈 Média A: {mA:.2f}")
            st.info(f"📉 Média B: {mB:.2f}")
            st.write(f"🔍 Diferença: {(mA - mB):.2f}")
        except:
            st.error("❌ Dados inválidos. Use números separados por vírgula.")

# Executa o módulo selecionado
carregar_modulo(modulos[modulo])
