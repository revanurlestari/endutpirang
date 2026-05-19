import streamlit as st

# =====================================
# KONFIGURASI HALAMAN
# =====================================

st.set_page_config(
    page_title="Kalkulator Termodinamika",
    page_icon="⚗️",
    layout="wide"
)

# CSS DESIGN
st.markdown("""
<style>
.main {
    background-color: #f5f7ff;
}

.title {
    text-align: center;
    font-size: 40px;
    font-weight: bold;
    color: #2E3A87;
}

.subtitle {
    text-align: center;
    color: gray;
    margin-bottom: 20px;
}

.box {
    background-color: white;
    padding: 25px;
    border-radius: 20px;
    box-shadow: 0px 4px 20px rgba(0,0,0,0.1);
}
</style>
""", unsafe_allow_html=True)

# =====================================
# HEADER
# =====================================

st.markdown('<p class="title">⚗️ Kalkulator Termodinamika</p>',
unsafe_allow_html=True)

st.markdown(
    '<p class="subtitle">Aplikasi Interaktif Termodinamika & Termokimia</p>',
    unsafe_allow_html=True
)

# =====================================
# SIDEBAR
# =====================================

menu = st.sidebar.selectbox(
    "📌 Pilih Perhitungan",
    [
        "Hukum 1 Termodinamika",
        "Usaha",
        "Kalor",
        "Entalpi",
        "Hukum Hess",
        "ΔH Reaksi",
        "Energi Gibbs",
        "Entropi",
        "Gas Ideal",
        "Gas Nyata"
    ]
)

# =====================================
# HUKUM 1 TERMODINAMIKA
# =====================================

if menu == "Hukum 1 Termodinamika":

    st.header("⚡ Hukum 1 Termodinamika")
    st.latex(r"\Delta U = Q - W")

    opsi = st.selectbox(
        "Cari nilai:",
        ["ΔU", "Q", "W"]
    )

    col1, col2 = st.columns(2)

    with col1:
        Q = st.number_input("Q (kJ)", value=0.0)

    with col2:
        W = st.number_input("W (kJ)", value=0.0)

    if st.button("Hitung"):

        if opsi == "ΔU":
            hasil = Q - W
            st.success(f"ΔU = {hasil:.3f} kJ")

        elif opsi == "Q":
            dU = st.number_input("ΔU", value=0.0)
            hasil = dU + W
            st.success(f"Q = {hasil:.3f} kJ")

        elif opsi == "W":
            dU = st.number_input("ΔU", value=0.0)
            hasil = Q - dU
            st.success(f"W = {hasil:.3f} kJ")


# =====================================
# USAHA
# =====================================

elif menu == "Usaha":

    st.header("🔧 Usaha")
    st.latex(r"W = P \times \Delta V")

    P = st.number_input("Tekanan P (Pa)")
    dV = st.number_input("Perubahan Volume ΔV (m³)")

    if st.button("Hitung"):
        hasil = P * dV
        st.success(f"W = {hasil:.3f} J")


# =====================================
# KALOR
# =====================================

elif menu == "Kalor":

    st.header("🔥 Kalor")
    st.latex(r"Q = m \times c \times \Delta T")

    m = st.number_input("Massa (g)")
    c = st.number_input("Kalor Jenis (J/g·K)")
    dT = st.number_input("Perubahan Suhu (K)")

    if st.button("Hitung"):
        hasil = m * c * dT
        st.success(f"Q = {hasil:.3f} J")


# =====================================
# ENTALPI
# =====================================

elif menu == "Entalpi":

    st.header("🧪 Entalpi")
    st.latex(r"\Delta H = \Delta U + \Delta nRT")

    R = 0.008314

    dU = st.number_input("ΔU (kJ)")
    dn = st.number_input("Δn (mol)")
    T = st.number_input("T (K)")

    if st.button("Hitung"):
        hasil = dU + (dn * R * T)
        st.success(f"ΔH = {hasil:.3f} kJ")


# =====================================
# HUKUM HESS
# =====================================

elif menu == "Hukum Hess":

    st.header("📘 Hukum Hess")

    data = st.text_input(
        "Masukkan ΔH tiap reaksi (pisahkan koma)",
        "10,-20,30"
    )

    if st.button("Hitung"):
        nilai = [float(x) for x in data.split(",")]
        hasil = sum(nilai)

        st.success(f"ΔH Total = {hasil:.3f} kJ")


# =====================================
# ΔH REAKSI
# =====================================

elif menu == "ΔH Reaksi":

    st.header("⚛️ ΔH Reaksi")

    produk = st.text_input(
        "ΔHf Produk (pisahkan koma)"
    )

    reaktan = st.text_input(
        "ΔHf Reaktan (pisahkan koma)"
    )

    if st.button("Hitung"):

        p = [float(x) for x in produk.split(",")]
        r = [float(x) for x in reaktan.split(",")]

        hasil = sum(p) - sum(r)

        st.success(f"ΔH Reaksi = {hasil:.3f} kJ/mol")


# =====================================
# ENERGI GIBBS
# =====================================

elif menu == "Energi Gibbs":

    st.header("⚡ Energi Gibbs")
    st.latex(r"\Delta G = \Delta H - T\Delta S")

    dH = st.number_input("ΔH (kJ)")
    T = st.number_input("T (K)")
    dS = st.number_input("ΔS (kJ/K)")

    if st.button("Hitung"):

        hasil = dH - (T * dS)

        st.success(f"ΔG = {hasil:.3f} kJ")


# =====================================
# ENTROPI
# =====================================

elif menu == "Entropi":

    st.header("🌡️ Entropi")
    st.latex(r"\Delta S = \frac{Q}{T}")

    Q = st.number_input("Q (kJ)")
    T = st.number_input("T (K)")

    if st.button("Hitung"):

        if T == 0:
            st.error("Temperatur tidak boleh 0")

        else:
            hasil = Q / T
            st.success(f"ΔS = {hasil:.3f} kJ/K")


# =====================================
# GAS IDEAL
# =====================================

elif menu == "Gas Ideal":

    st.header("💨 Gas Ideal")
    st.latex(r"PV = nRT")

    R = 0.0821

    n = st.number_input("Jumlah mol (mol)")
    T = st.number_input("Temperatur (K)")
    V = st.number_input("Volume (L)")

    if st.button("Hitung Tekanan"):

        if V == 0:
            st.error("Volume tidak boleh 0")

        else:
            hasil = (n * R * T) / V
            st.success(f"P = {hasil:.3f} atm")


# =====================================
# GAS NYATA
# =====================================

elif menu == "Gas Nyata":

    st.header("🧫 Gas Nyata")
    st.latex(r"(P+\frac{an^2}{V^2})(V-nb)=nRT")

    R = 0.0821

    n = st.number_input("Mol (n)")
    T = st.number_input("Temperatur (K)")
    V = st.number_input("Volume (L)")
    a = st.number_input("Konstanta a")
    b = st.number_input("Konstanta b")

    if st.button("Hitung"):

        if V == 0:
            st.error("Volume tidak valid")

        else:
            hasil = (
                ((n * R * T) / (V - n*b))
                - ((a * n*2) / (V*2))
            )

            st.success(f"P = {hasil:.3f} atm")
