import streamlit as st

st.set_page_config(
    page_title="Food Product Demand Forecasting Dashboard", 
    layout="wide",
    page_icon="📊"
)

# ============================================
# CSS SIMPLE - ELEGANT PURPLE
# ============================================

st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #f8f4ff 0%, #f0ebff 50%, #e8e0ff 100%);
        font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
    }
    
    h1, h2, h3 {
        color: #6A11CB !important;
    }
    
    .stButton > button {
        background: linear-gradient(135deg, #6A11CB 0%, #9D4EDD 100%);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 12px 24px;
        font-weight: 600;
        width: 100%;
        margin-top: 10px;
    }
    
    .stButton > button:hover {
        background: linear-gradient(135deg, #5a0db8 0%, #8a45d0 100%);
    }
    
    .card {
        background: white;
        border-radius: 16px;
        padding: 25px;
        border: 1px solid #e6d9ff;
        box-shadow: 0 4px 12px rgba(106, 17, 203, 0.1);
        text-align: center;
        margin-bottom: 20px;
    }
    
    .icon-container {
        width: 70px;
        height: 70px;
        background: linear-gradient(135deg, #6A11CB 0%, #9D4EDD 100%);
        border-radius: 16px;
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 0 auto 15px;
        font-size: 30px;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# ============================================
# HEADER - BAHASA INDONESIA
# ============================================

# Header dengan icon dan judul
col_icon, col_title = st.columns([0.1, 0.9])
with col_icon:
    st.markdown("<div style='margin-top: 10px; font-size: 40px; color: #6A11CB;'>📊</div>", unsafe_allow_html=True)
with col_title:
    st.title("Food Product Demand Forecasting Dashboard")

st.markdown("""
<div style='text-align: center; padding: 10px 0 30px;'>
    <h2 style='color: #6A11CB; margin-bottom: 10px;'>Sistem Analisis & Peramalan Produksi</h2>
    <p style='color: #666; font-size: 16px;'>
        Platform profesional untuk peramalan permintaan dengan algoritma SES dan Moving Average
    </p>
</div>
""", unsafe_allow_html=True)

# ============================================
# MENU UTAMA - 3 MODUL
# ============================================

st.markdown("## 📋 Menu Utama")

col1, col2, col3 = st.columns(3)

with col1:
    # Card Peramalan
    st.markdown("""
    <div class="card">
        <div class="icon-container">📈</div>
        <h3>Peramalan</h3>
        <p style="color: #666; font-size: 14px; line-height: 1.5;">
            Analisis peramalan menggunakan metode SES dan Moving Average dengan optimasi parameter otomatis
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("Buka Modul Peramalan", key="forecast"):
        st.switch_page("pages/1_Forecasting.py")

with col2:
    # Card Grafik
    st.markdown("""
    <div class="card">
        <div class="icon-container">📊</div>
        <h3>Grafik Per Produk</h3>
        <p style="color: #666; font-size: 14px; line-height: 1.5;">
            Visualisasi data dan tren permintaan untuk setiap produk secara interaktif
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("Buka Modul Grafik", key="grafik"):
        st.switch_page("pages/2_Grafik_Per_Produk.py")

with col3:
    # Card Upload
    st.markdown("""
    <div class="card">
        <div class="icon-container">📁</div>
        <h3>Unggah Data</h3>
        <p style="color: #666; font-size: 14px; line-height: 1.5;">
            Unggah file Excel untuk analisis dengan format produk, tanggal, permintaan
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("Buka Modul Upload", key="upload"):
        st.switch_page("pages/3_Upload_Data.py")

# ============================================
# INFORMASI SISTEM
# ============================================

st.markdown("---")
st.markdown("## ℹ️ Informasi Sistem")

# Metrics dalam 3 kolom
col_info1, col_info2, col_info3 = st.columns(3)

with col_info1:
    st.metric("Versi Sistem", "v2.1.0")
    
with col_info2:
    st.metric("Status", "✅ Aktif")
    
with col_info3:
    st.metric("Akurasi", "Setara Minitab")

# ============================================
# PETUNJUK PENGGUNAAN
# ============================================

with st.expander("📚 Panduan Penggunaan"):
    st.markdown("""
    ### Cara Menggunakan Sistem:
    
    1. **Unggah Data** - Gunakan menu "Unggah Data" untuk mengupload file Excel
    2. **Analisis Peramalan** - Buka menu "Peramalan" untuk analisis SES dan MA
    3. **Lihat Grafik** - Gunakan menu "Grafik Per Produk" untuk visualisasi
    
    ### Format Data yang Didukung:
    - File Excel (.xlsx) dengan multi sheet
    - Kolom wajib: `produk`, `tanggal`, `permintaan`
    - Format tanggal: YYYY-MM-DD
    
    ### Algoritma yang Tersedia:
    - **SES (Single Exponential Smoothing)** - Optimasi alpha otomatis
    - **MA (Moving Average)** - Optimasi window otomatis
    
    ### Fitur Utama:
    - Optimasi parameter otomatis
    - Perhitungan MAPE (Mean Absolute Percentage Error)
    - Ekspor hasil dalam format CSV dan PNG
    - Dashboard visualisasi interaktif
    """)

# ============================================
# FOOTER
# ============================================

st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; font-size: 14px; padding: 20px;'>
    <strong>Sistem Forecasting Food Product v2.1</strong> • Dikembangkan oleh Kelompok 17 APTEK © 2025
</div>
""", unsafe_allow_html=True)
